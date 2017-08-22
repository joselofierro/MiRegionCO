from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import *

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
    success_url = reverse_lazy('noticia:listar_noticia')
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
        files = request.FILES.getlist('imagen')

        if form.is_valid() and form2.is_valid():
            list_id_imagenes = []
            for f in files:
                imagen = Imagen(nombre=form.data['titular'], imagen=f)
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
            return HttpResponseRedirect(self.get_success_url())

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
            return Noticia.objects.all()

        elif self.request.user.groups.filter(name="SupervisorEscritor"):
            return Noticia.objects.all()
        else:
            return Noticia.objects.filter(autor=self.request.user)


class NoticiaUpdate(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Noticia
    second_model = Imagen
    form_class = NoticiaForm
    second_form_class = ImagenForm
    template_name = 'noticia/noticia_form.html'
    success_url = reverse_lazy('noticia:listar_noticia')
    success_message = "Se ha actualizado  la noticia satisfactoriamente."
    permission_required = ('noticia.add_noticia', 'noticia.change_noticia')
    # me devuelve al login si es falso y si es true arroja un exceptionError
    raise_exception = False
    # si no tengo los permisos me redirige al login
    login_url = reverse_lazy('grupo:login')
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super(NoticiaUpdate, self).get_context_data(**kwargs)
        # noticia = self.model.objects.get()
        # imagen = self.second_model.objects.get()

        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class()

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_noticia = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)

        if form_noticia.is_valid() and form2.is_valid():
            # tags que vienen del formulario
            tags = request.POST['tags']
            # cortaré los tags por coma y espacio ', '
            list_tags = tags.split(', ')

            # Obtengo la noticia
            noticia = Noticia.objects.get(id=self.kwargs['pk'])
            noticia.autor = self.request.user

            # si los tags del formulario son menores a los tags de la noticia en la BD
            if len(list_tags) < noticia.tag.count():
                # recorro los tags de la noticia en la BD
                for tag_noticia in noticia.tag.all():
                    # si el tag de la BD no esta en la lista de tags
                    if tag_noticia.nombre not in list_tags:
                        # borre el tag de la BD
                        noticia.tag.remove(tag_noticia)
            else:
                for tag in list_tags:
                    tag = tag.title()

                    # busco si el Tag está creado
                    try:
                        tag_object = Tag.objects.get(nombre=tag)
                        noticia.tag.add(tag_object)
                    # si no esta creado
                    except Tag.DoesNotExist:
                        tag_creado = Tag(nombre=tag)
                        tag_creado.save()
                        noticia.tag.add(tag_creado)

            noticia = form_noticia.save(commit=False)
            noticia.autor = self.request.user
            form2.save()

            return HttpResponseRedirect(self.get_success_url())

        else:
            return render(request, self.template_name, {'form': form_noticia, 'form2': form2})


class NoticiaDelete(PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Noticia
    template_name = 'noticia/noticia_delete.html'
    success_url = reverse_lazy('noticia:listar_noticia')
    success_message = "Se ha eliminado la noticia satisfactoriamente."
    permission_required = ('noticia.add_noticia', 'noticia.change_noticia')
    # me devuelve al login si es falso y si es true arroja un exceptionError
    raise_exception = False
    # si no tengo los permisos me redirige al login
    login_url = reverse_lazy('grupo:login')
    redirect_field_name = 'redirect_to'
