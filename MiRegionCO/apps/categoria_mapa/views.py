from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.cache import caches

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import *

from MiRegionCO import settings
from apps.categoria_mapa.forms import MapaForm
from apps.categoria_mapa.models import CategoriaMapa


class CategoriaMapaCreate(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = CategoriaMapa
    form_class = MapaForm
    template_name = 'categoria_mapa/categoria_mapa_form.html'
    success_url = reverse_lazy('mapa:categoria_listar')
    success_message = 'Se ha creado la categoria del mapa.'
    permission_required = (
        'categoriamapa.add_categoriamapa', 'categoriamapa.change_categoriamapa')
    raise_exception = False
    login_url = reverse_lazy('grupo:login')
    redirect_field_name = 'redirect_to'

    def form_valid(self, form):
        caches[settings.CACHE_API_CATEGORIA_MAPA].clear()
        return super(CategoriaMapaCreate, self).form_valid(form)


class CategoriaMapaList(PermissionRequiredMixin, ListView):
    model = CategoriaMapa
    template_name = 'categoria_mapa/categoria_mapa_list.html'
    permission_required = (
        'categoriamapa.add_categoriamapa', 'categoriamapa.change_categoriamapa')
    raise_exception = False
    login_url = reverse_lazy('grupo:login')
    redirect_field_name = 'redirect_to'


class CategoriaMapaUpdate(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = CategoriaMapa
    form_class = MapaForm
    template_name = 'categoria_mapa/categoria_mapa_form.html'
    success_url = reverse_lazy('mapa:categoria_listar')
    success_message = 'Se ha actualizado la categoria del mapa.'
    permission_required = (
        'categoriamapa.add_categoriamapa', 'categoriamapa.change_categoriamapa')
    raise_exception = False
    login_url = reverse_lazy('grupo:login')
    redirect_field_name = 'redirect_to'

    def form_valid(self, form):
        caches[settings.CACHE_API_CATEGORIA_MAPA].clear()
        return super(CategoriaMapaUpdate, self).form_valid(self)


class CategoriaMapaDelete(PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = CategoriaMapa
    template_name = 'categoria_mapa/categoria_mapa_delete.html'
    success_url = reverse_lazy('mapa:categoria_listar')
    success_message = 'Se ha eliminado la categoria del mapa.'
    permission_required = (
        'categoriamapa.add_categoriamapa', 'categoriamapa.change_categoriamapa')
    raise_exception = False
    login_url = reverse_lazy('grupo:login')
    redirect_field_name = 'redirect_to'

    def post(self, request, *args, **kwargs):
        pass
