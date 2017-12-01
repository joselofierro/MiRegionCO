from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import *

from apps.ventas.detalle.forms import DetalleForm
from apps.ventas.detalle.models import Detalle


class DetalleCreate(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Detalle
    form_class = DetalleForm
    template_name = 'ventas/detalle/detalle_form.html'
    success_url = reverse_lazy('detalle:listar_detalle')
    success_message = "Se ha creado el detalle satisfactoriamente."
    permission_required = ('detalle.add_detalle', 'noticia.change_detalle')
    # me devuelve al login si es falso y si es true arroja un exceptionError
    raise_exception = False
    # si no tengo los permisos me redirige al login
    login_url = reverse_lazy('user:index')
    redirect_field_name = 'redirect_to'


class DetalleList(ListView, SuccessMessageMixin):
    model = Detalle
    template_name = 'ventas/detalle/detalle_list.html'
    permission_required = ('detalle.add_detalle', 'detalle.change_detalle')
    # me devuelve al login si es falso y si es true arroja un exceptionError
    raise_exception = False
    # si no tengo los permisos me redirige al login
    login_url = reverse_lazy('user:index')
    redirect_field_name = 'redirect_to'


class DetalleUpdate(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Detalle
    form_class = DetalleForm
    template_name = 'ventas/detalle/detalle_form.html'
    success_url = reverse_lazy('detalle:listar_detalle')
    success_message = "Se ha actualizado el detalle satisfactoriamente."
    permission_required = ('detalle.add_detalle', 'detalle.change_detalle')
    # me devuelve al login si es falso y si es true arroja un exceptionError
    raise_exception = False
    # si no tengo los permisos me redirige al login
    login_url = reverse_lazy('user:index')
    redirect_field_name = 'redirect_to'


class DetalleDelete(PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Detalle
    template_name = 'ventas/detalle/detalle_delete.html'
    success_url = reverse_lazy('detalle:listar_detalle')
    success_message = "Se ha eliminado el detalle satisfactoriamente."
    permission_required = ('detalle.add_detalle', 'detalle.change_detalle')
    # me devuelve al login si es falso y si es true arroja un exceptionError
    raise_exception = False
    # si no tengo los permisos me redirige al login
    login_url = reverse_lazy('user:index')
    redirect_field_name = 'redirect_to'



