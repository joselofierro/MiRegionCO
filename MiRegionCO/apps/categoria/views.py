from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.cache import caches
from django.urls import reverse_lazy
from django.views.generic import *

from MiRegionCO import settings
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
    login_url = reverse_lazy('user:index')
    redirect_field_name = 'redirect_to'

    def form_valid(self, form):
        caches[settings.CACHE_API_CATEGORIA_NOTICIAS].clear()
        return super(CategoriaCreate, self).form_valid(form)


class CategoriaList(ListView):
    model = Categoria
    template_name = 'categoria/categoria_list.html'
    permission_required = ('categoria.add_categoria', 'categoria.change_categoria')
    raise_exception = False
    login_url = reverse_lazy('user:index')
    redirect_field_name = 'redirect_to'

    def get_queryset(self):
        return Categoria.objects.order_by('nombre')


class CategoriaUpdate(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categoria/categoria_form.html'
    success_url = reverse_lazy('categorias:categoria_listar')
    success_message = 'Se ha actualizado la categoria.'
    permission_required = ('categoria.add_categoria', 'categoria.change_categoria')
    raise_exception = False
    login_url = reverse_lazy('user:index')
    redirect_field_name = 'redirect_to'

    def form_valid(self, form):
        caches[settings.CACHE_API_CATEGORIA_NOTICIAS].clear()
        return super(CategoriaUpdate, self).form_valid(form)


class CategoriaDelete(PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Categoria
    template_name = 'categoria/categoria_delete.html'
    success_url = reverse_lazy('categorias:categoria_listar')
    success_message = 'Se ha eliminado la categoria.'
    permission_required = ('categoria.add_categoria', 'categoria.change_categoria')
    raise_exception = False
    login_url = reverse_lazy('user:index')
    redirect_field_name = 'redirect_to'

    def post(self, request, *args, **kwargs):
        caches[settings.CACHE_API_CATEGORIA_NOTICIAS].clear()
        return super(CategoriaDelete, self).post(args, kwargs)
