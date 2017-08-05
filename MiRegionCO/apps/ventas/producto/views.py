from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import *

from apps.ventas.producto.forms import ProductoForm
from apps.ventas.producto.models import Producto


class ProductoCreate(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'ventas/producto/producto_form.html'
    success_url = reverse_lazy('producto:listar_producto')
    success_message = 'Se ha creado el producto con exito'
    permission_required = ('producto.add_producto', 'producto.change_producto')
    # me devuelve al login si es falso y si es true arroja un exceptionError
    raise_exception = False
    # si no tengo los permisos me redirige al login
    login_url = reverse_lazy('grupo:login')
    redirect_field_name = 'redirect_to'


class ProductoList(PermissionRequiredMixin, ListView):
    model = Producto
    template_name = 'ventas/producto/producto_list.html'
    permission_required = ('producto.add_producto', 'producto.change_producto')
    # me devuelve al login si es falso y si es true arroja un exceptionError
    raise_exception = False
    # si no tengo los permisos me redirige al login
    login_url = reverse_lazy('grupo:login')
    redirect_field_name = 'redirect_to'


class ProductoUpdate(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'ventas/producto/producto_form.html'
    success_url = reverse_lazy('producto:listar_producto')
    success_message = 'Se ha actualizado el producto con exito'
    permission_required = ('producto.add_producto', 'producto.change_producto')
    # me devuelve al login si es falso y si es true arroja un exceptionError
    raise_exception = False
    # si no tengo los permisos me redirige al login
    login_url = reverse_lazy('grupo:login')
    redirect_field_name = 'redirect_to'


class ProductoDelete(PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Producto
    template_name = 'ventas/producto/producto_delete.html'
    success_url = reverse_lazy('producto:listar_producto')
    success_message = 'Se ha eliminado el producto con exito'
    permission_required = ('producto.add_producto', 'producto.change_producto')
    # me devuelve al login si es falso y si es true arroja un exceptionError
    raise_exception = False
    # si no tengo los permisos me redirige al login
    login_url = reverse_lazy('grupo:login')
    redirect_field_name = 'redirect_to'
