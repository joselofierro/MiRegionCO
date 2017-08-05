from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import *

from apps.noticia.forms import NoticiaForm
from apps.noticia.models import Noticia


class NoticiaCreate(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Noticia
    form_class = NoticiaForm
    template_name = 'noticia/noticia_form.html'
    success_url = reverse_lazy('noticia:listar_noticia')
    success_message = "Se ha creado la noticia satisfactoriamente."
    permission_required = ('noticia.add_noticia', 'noticia.change_noticia')
    # me devuelve al login si es falso y si es true arroja un exceptionError
    raise_exception = False
    # si no tengo los permisos me redirige al login
    login_url = reverse_lazy('grupo:login')
    redirect_field_name = 'redirect_to'


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
