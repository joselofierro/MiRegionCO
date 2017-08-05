from django.shortcuts import render

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import *

from apps.ventas.categoria_producto.forms import CategoriaProductoForm
from apps.ventas.categoria_producto.models import CategoriaProducto


class CategoriaProductoCreate(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = CategoriaProducto
    form_class = CategoriaProductoForm
    template_name = 'ventas/categoria_producto/categoria_producto_form.html'
    success_url = reverse_lazy('categoria_producto:listar_categoria_producto')
    success_message = "Se ha creado la categoria del producto satisfactoriamente."
    permission_required = (
        'categoriaproducto.add_categoria', 'categoriaproducto.change_categoria')
    # me devuelve al login si es falso y si es true arroja un exceptionError
    raise_exception = False
    # si no tengo los permisos me redirige al login
    login_url = reverse_lazy('grupo:login')
    redirect_field_name = 'redirect_to'


class CategoriaProductoList(PermissionRequiredMixin, ListView):
    model = CategoriaProducto
    template_name = 'ventas/categoria_producto/categoria_producto_list.html'
    permission_required = ('categoriaproducto.add_categoria', 'categoriaproducto.change_categoria')
    raise_exception = False
    login_url = reverse_lazy('grupo:login')
    redirect_field_name = 'redirect_to'


class CategoriaProductoUpdate(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = CategoriaProducto
    form_class = CategoriaProductoForm
    template_name = 'ventas/categoria_producto/categoria_producto_form.html'
    success_url = reverse_lazy('categoria_producto:listar_categoria_producto')
    success_message = "Se ha actualizado la categoria del producto satisfactoriamente."
    permission_required = (
        'categoriaproducto.add_categoria', 'categoriaproducto.change_categoria')
    # me devuelve al login si es falso y si es true arroja un exceptionError
    raise_exception = False
    # si no tengo los permisos me redirige al login
    login_url = reverse_lazy('grupo:login')
    redirect_field_name = 'redirect_to'


class CategoriaProductoDelete(PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = CategoriaProducto
    template_name = 'ventas/categoria_producto/categoria_producto_delete.html'
    success_url = reverse_lazy('categoria_producto:listar_categoria_producto')
    success_message = "Se ha Eliminado la categoria del producto satisfactoriamente."
    permission_required = (
        'categoriaproducto.add_categoria', 'categoriaproducto.change_categoria', 'categoriaproducto.delete_categoria')
    # me devuelve al login si es falso y si es true arroja un exceptionError
    raise_exception = False
    # si no tengo los permisos me redirige al login
    login_url = reverse_lazy('grupo:login')
    redirect_field_name = 'redirect_to'
