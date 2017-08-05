from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import *

from apps.ventas.subcategoria_producto.forms import SubcategoriaProductoForm
from apps.ventas.subcategoria_producto.models import Subcategoria


class SubcategoriaCreate(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Subcategoria
    form_class = SubcategoriaProductoForm
    template_name = 'ventas/subcategoria_producto/subcategoria_producto_form.html'
    success_url = reverse_lazy('subcategoria_producto:listar_subcategoria')
    success_message = 'Se ha creado la subcategoria exitosamente'
    permission_required = ('subcategoria.add_subcategoria', 'subcategoria.change_subcategoria')
    # me devuelve al login si es falso y si es true arroja un exceptionError
    raise_exception = False
    # si no tengo los permisos me redirige al login
    login_url = reverse_lazy('grupo:login')
    redirect_field_name = 'redirect_to'


class SubcategoriaList(SuccessMessageMixin, ListView):
    model = Subcategoria
    template_name = 'ventas/subcategoria_producto/subcategoria_producto_list.html'
    permission_required = ('subcategoria.add_subcategoria', 'subcategoria.change_subcategoria')
    # me devuelve al login si es falso y si es true arroja un exceptionError
    raise_exception = False
    # si no tengo los permisos me redirige al login
    login_url = reverse_lazy('grupo:login')
    redirect_field_name = 'redirect_to'


class SubcategoriaUpdate(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Subcategoria
    form_class = SubcategoriaProductoForm
    template_name = 'ventas/subcategoria_producto/subcategoria_producto_form.html'
    success_url = reverse_lazy('subcategoria_producto:listar_subcategoria')
    success_message = 'Se ha actualizado la subcategoria exitosamente'
    permission_required = ('subcategoria.add_subcategoria', 'subcategoria.change_subcategoria')
    # me devuelve al login si es falso y si es true arroja un exceptionError
    raise_exception = False
    # si no tengo los permisos me redirige al login
    login_url = reverse_lazy('grupo:login')
    redirect_field_name = 'redirect_to'


class SubcategoriaDelete(PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Subcategoria
    template_name = 'ventas/subcategoria_producto/subcategoria_producto_delete.html'
    success_url = reverse_lazy('subcategoria_producto:listar_subcategoria')
    success_message = 'Se ha eliminado la subcategoria exitosamente'
    permission_required = ('subcategoria.add_subcategoria', 'subcategoria.change_subcategoria')
    # me devuelve al login si es falso y si es true arroja un exceptionError
    raise_exception = False
    # si no tengo los permisos me redirige al login
    login_url = reverse_lazy('grupo:login')
    redirect_field_name = 'redirect_to'

