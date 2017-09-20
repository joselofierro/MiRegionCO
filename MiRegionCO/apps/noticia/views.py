from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.cache import caches
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import *

from MiRegionCO import settings
from apps.imagen.forms import ImagenForm
from apps.imagen.models import Imagen
from apps.noticia.forms import NoticiaForm
from apps.noticia.models import Noticia
from apps.tag.forms import TagForm
from apps.tag.models import Tag


class NoticiaCreate(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Noticia
    form_class = NoticiaForm
    second_form_class = ImagenForm
    template_name = 'noticia/noticia_form.html'
    success_url = reverse_lazy('noticia:listar')
    success_message = "Se ha creado la noticia satisfactoriamente."
    permission_required = ('noticia.add_noticia', 'noticia.change_noticia')
    # me devuelve al login si es falso y si es true arroja un exceptionError
    raise_exception = False
    # si no tengo los permisos me redirige al login
    login_url = reverse_lazy('grupo:login')
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super(NoticiaCreate, self).get_context_data(**kwargs)

        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        # guardamos las imagenes del formulario
        files = request.FILES.getlist('imagen')

        # si la noticia es valida
        if form.is_valid() and form2.is_valid():
            # si tiene imagenes
            if len(request.FILES) != 0:
                list_id_imagenes = []
                for index, f in enumerate(files):
                    imagen = Imagen(nombre=form.data['titular'] + "_" + str(index), imagen=f)
                    imagen.save()
                    list_id_imagenes.append(imagen)

                noticia = form.save(commit=False)
                usuario_sesion = request.user
                noticia.autor = usuario_sesion

                noticia.save()

                tags = request.POST['tags']
                # cortaré los tags por coma y espacio ', '
                list_tags = tags.split(', ')
                for tag in list_tags:
                    tag = tag.title()

                    # busco si el Tag está creado
                    try:
                        tag_object = Tag.objects.get(nombre=tag)
                        noticia.tag.add(tag_object)
                    except Tag.DoesNotExist:
                        tag_creado = Tag(nombre=tag)
                        tag_creado.save()
                        noticia.tag.add(tag_creado)

                for imagen_id in list_id_imagenes:
                    noticia.imagenes.add(imagen_id)

                caches[settings.CACHE_API_NOTICIAS].clear()
                caches[settings.CACHE_API_NOTICIAS2].clear()
                caches[settings.CACHE_API_NOTICIAS_DESTACADAS].clear()
                caches[settings.CACHE_API_NOTICIAS_DESTACADAS_CATEGORIA].clear()
                caches[settings.CACHE_API_NOTICIASXCATEGORIA].clear()
                caches[settings.CACHE_API_NOTICIASXCATEGORIA2].clear()
                return HttpResponseRedirect(self.get_success_url())
            else:
                return render(request, self.template_name,
                              {'form': form, 'form2': form2, 'error': '¡La noticia no tiene imagen!'})
        else:
            return render(request, self.template_name, {'form': form, 'form2': form2})


class NoticiaList(PermissionRequiredMixin, ListView):
    model = Noticia
    template_name = 'noticia/noticia_list.html'
    permission_required = ('noticia.add_noticia', 'noticia.change_noticia')
    raise_exception = False
    login_url = reverse_lazy('grupo:login')
    redirect_field_name = 'redirect_to'

    def get_queryset(self):
        if self.request.user.groups.filter(name="Administrador"):
            return Noticia.objects.filter(visible=True).order_by('-fecha', '-hora')

        elif self.request.user.groups.filter(name="SupervisorEscritor"):
            return Noticia.objects.filter(visible=True).order_by('-fecha', '-hora')

        elif self.request.user.groups.filter(name='Escritor'):
            return Noticia.objects.filter(autor=self.request.user, visible=True).order_by('-fecha', '-hora')
        else:
            return Noticia.objects.filter(autor=self.request.user, visible=True)


class NoticiaUpdate(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Noticia
    second_model = Imagen
    third_model = Tag
    form_class = NoticiaForm
    second_form_class = ImagenForm
    third_form_class = TagForm
    template_name = 'noticia/noticia_form.html'
    success_url = reverse_lazy('noticia:listar')
    success_message = "Se ha actualizado  la noticia satisfactoriamente."
    permission_required = ('noticia.add_noticia', 'noticia.change_noticia')
    # me devuelve al login si es falso y si es true arroja un exceptionError
    raise_exception = False
    # si no tengo los permisos me redirige al login
    login_url = reverse_lazy('grupo:login')
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super(NoticiaUpdate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        noticia_id = self.kwargs['pk']
        noticia = self.model.objects.get(id=noticia_id)
        form_noticia = self.form_class(request.POST, instance=noticia)
        form2 = self.second_form_class(request.POST)

        if form_noticia.is_valid() and form2.is_valid():
            # Obtenemos los tags que vienen del form = String
            tags = request.POST['tags']
            # Los convertimos a una lista de strings cortándolos por la coma y espacio (', ')
            list_tags = tags.split(', ')

            # Este listado nos servirá para tener las instancias de tag de la BD
            list_tags_bd = []

            # Recorremos el listado de tags string para consultar si existen en la BD y si no crearlos
            for tag in list_tags:
                try:
                    tag_bd = Tag.objects.get(nombre=tag.title())
                    # Si existe el tag lo agrego al listado de tags de la BD
                    list_tags_bd.append(tag_bd)
                except Tag.DoesNotExist:
                    # Si no existe el tag lo creo
                    tag_bd = Tag(nombre=tag.title())
                    tag_bd.save()
                    # Lo agrego al listado de tags de la BD
                    list_tags_bd.append(tag_bd)

            # Borramos los tags de la noticia
            noticia.tag.clear()

            # Asignamos los tags a la noticia
            for tag in list_tags_bd:
                noticia.tag.add(tag)

            form_noticia.save()
            form2.save()

            caches[settings.CACHE_API_NOTICIAS].clear()
            caches[settings.CACHE_API_NOTICIAS2].clear()
            caches[settings.CACHE_API_NOTICIAS_DESTACADAS].clear()
            caches[settings.CACHE_API_NOTICIAS_DESTACADAS_CATEGORIA].clear()
            caches[settings.CACHE_API_NOTICIASXCATEGORIA].clear()
            caches[settings.CACHE_API_NOTICIASXCATEGORIA2].clear()
            return HttpResponseRedirect(self.get_success_url())

        else:
            return render(request, self.template_name, {'form': form_noticia, 'form2': form2})


class NoticiaDelete(PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Noticia
    template_name = 'noticia/noticia_delete.html'
    success_url = reverse_lazy('noticia:listar')
    success_message = "Se ha eliminado la noticia satisfactoriamente."
    permission_required = ('noticia.add_noticia', 'noticia.change_noticia')
    # me devuelve al login si es falso y si es true arroja un exceptionError
    raise_exception = False
    # si no tengo los permisos me redirige al login
    login_url = reverse_lazy('grupo:login')
    redirect_field_name = 'redirect_to'

    def post(self, request, *args, **kwargs):
        caches[settings.CACHE_API_NOTICIAS].clear()
        caches[settings.CACHE_API_NOTICIAS2].clear()
        caches[settings.CACHE_API_NOTICIAS_DESTACADAS].clear()
        caches[settings.CACHE_API_NOTICIAS_DESTACADAS_CATEGORIA].clear()
        caches[settings.CACHE_API_NOTICIASXCATEGORIA].clear()
        caches[settings.CACHE_API_NOTICIASXCATEGORIA2].clear()
        return super(NoticiaDelete, self).post(args, kwargs)


# ACCION PARA OCULTAR NOTICIA
@permission_required(login_url='/', perm='noticia.delete_noticia',
                     raise_exception=False)
def eliminarnoticia(request, pk):
    if request.method == 'POST':
        caches[settings.CACHE_API_NOTICIAS].clear()
        caches[settings.CACHE_API_NOTICIAS2].clear()
        caches[settings.CACHE_API_NOTICIAS_DESTACADAS].clear()
        caches[settings.CACHE_API_NOTICIAS_DESTACADAS_CATEGORIA].clear()
        caches[settings.CACHE_API_NOTICIASXCATEGORIA].clear()
        caches[settings.CACHE_API_NOTICIASXCATEGORIA2].clear()

        noticia_obj = Noticia.objects.get(id=pk)
        noticia_obj.visible = False
        noticia_obj.destacada = False
        noticia_obj.save()
        return redirect('noticia:listar')
