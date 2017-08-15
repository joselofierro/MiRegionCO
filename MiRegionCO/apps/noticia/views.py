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
    third_form_class = TagForm
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
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class()

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        files = request.FILES.getlist('imagen')

        if form.is_valid() and form2.is_valid():
            list_id_imagenes = []
            for index, f in enumerate(files):
                imagen = Imagen(nombre=form.data['titular'], imagen=f)
                imagen.save()
                list_id_imagenes.append(imagen)

            noticia = form.save(commit=False)
            usuario_sesion = request.user
            noticia.autor = usuario_sesion

            noticia.save()

            tags = request.POST['tags']
            # cortaré los tags por cona y espacio ', '
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

        """form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('imagenes')
        list_id_imagenes = []
        for index, f in enumerate(files):
            imagen = Imagen(nombre=form.data['titular'], imagen=f)
            imagen.save()
            list_id_imagenes.append(imagen.id)
        print(list_id_imagenes)
        if form.is_valid():
            print("form valido")
            return self.form_valid(form)
        else:
            return self.form_invalid(form)"""


class NoticiaList(PermissionRequiredMixin, ListView):
    model = Noticia
    template_name = 'noticia/noticia_list.html'
    permission_required = ('noticia.add_noticia', 'noticia.change_noticia')
    raise_exception = False
    login_url = reverse_lazy('grupo:login')
    redirect_field_name = 'redirect_to'


class NoticiaUpdate(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Noticia
    form_class = NoticiaForm
    template_name = 'noticia/noticia_form.html'
    success_url = reverse_lazy('noticia:listar_noticia')
    success_message = "Se ha actualizado  la noticia satisfactoriamente."
    permission_required = ('noticia.add_noticia', 'noticia.change_noticia')
    # me devuelve al login si es falso y si es true arroja un exceptionError
    raise_exception = False
    # si no tengo los permisos me redirige al login
    login_url = reverse_lazy('grupo:login')
    redirect_field_name = 'redirect_to'


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
