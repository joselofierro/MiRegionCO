from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import *

from apps.categoria.forms import CategoriaForm
from apps.categoria.models import Categoria


class CategoriaCreate(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categoria/categoria_form.html'
    success_url = reverse_lazy('categorias:categoria_listar')
    success_message = 'Se ha creado la categoria.'
    permission_required = ('categoria.add_categoria', 'categoria.change_categoria')
    raise_exception = False
    login_url = reverse_lazy('grupo:login')
    redirect_field_name = 'redirect_to'


class CategoriaList(ListView):
    model = Categoria
    template_name = 'categoria/categoria_list.html'
    permission_required = ('categoria.add_categoria', 'categoria.change_categoria')
    raise_exception = False
    login_url = reverse_lazy('grupo:login')
    redirect_field_name = 'redirect_to'


class CategoriaUpdate(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categoria/categoria_form.html'
    success_url = reverse_lazy('categorias:categoria_listar')
    success_message = 'Se ha actualizado la categoria.'
    permission_required = ('categoria.add_categoria', 'categoria.change_categoria')
    raise_exception = False
    login_url = reverse_lazy('grupo:login')
    redirect_field_name = 'redirect_to'


class CategoriaDelete(PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Categoria
    template_name = 'categoria/categoria_delete.html'
    success_url = reverse_lazy('categorias:categoria_listar')
    success_message = 'Se ha eliminado la categoria.'
    permission_required = ('categoria.add_categoria', 'categoria.change_categoria')
    raise_exception = False
    login_url = reverse_lazy('grupo:login')
    redirect_field_name = 'redirect_to'
