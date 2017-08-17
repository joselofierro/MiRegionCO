from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import *

from apps.subcategoria_mapa.forms import SubcategoriaMapaForm
from apps.subcategoria_mapa.models import SubcategoriaMapa


class SubcategoriaMapaCreate(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = SubcategoriaMapa
    form_class = SubcategoriaMapaForm
    template_name = 'subcategoria_mapa/subcategoria_mapa_form.html'
    success_url = reverse_lazy('sub_mapa:listar_subcategoria_mapa')
    success_message = 'Se ha creado la subcategoria del mapa exitosamente'
    permission_required = ('subcategoriamapa.add_subcategoriamapa', 'subcategoriamapa.change_subcategoriamapa')
    raise_exception = False
    login_url = reverse_lazy('grupo:login')
    redirect_field_name = 'redirect_to'


class SubcategoriaMapaList(PermissionRequiredMixin, ListView):
    model = SubcategoriaMapa
    template_name = 'subcategoria_mapa/subcategoria_mapa_list.html'
    permission_required = ('subcategoriamapa.add_subcategoriamapa', 'subcategoriamapa.change_subcategoriamapa')
    raise_exception = False
    login_url = reverse_lazy('grupo:login')
    redirect_field_name = 'redirect_to'


class SubcategoriaMapaUpdate(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = SubcategoriaMapa
    form_class = SubcategoriaMapaForm
    template_name = 'subcategoria_mapa/subcategoria_mapa_form.html'
    success_url = reverse_lazy('sub_mapa:listar_subcategoria_mapa')
    success_message = 'Se ha actualizado la subcategoria del mapa exitosamente'
    permission_required = ('subcategoriamapa.add_subcategoriamapa', 'subcategoriamapa.change_subcategoriamapa')
    raise_exception = False
    login_url = reverse_lazy('grupo:login')
    redirect_field_name = 'redirect_to'


class SubcategoriaMapaDelete(PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = SubcategoriaMapa
    template_name = 'subcategoria_mapa/subcategoria_mapa_delete.html'
    success_url = reverse_lazy('sub_mapa:listar_subcategoria_mapa')
    success_message = 'Se ha eliminado la subcategoria del mapa exitosamente'
    permission_required = ('subcategoriamapa.add_subcategoriamapa', 'subcategoriamapa.change_subcategoriamapa')
    raise_exception = False
    login_url = reverse_lazy('grupo:login')
    redirect_field_name = 'redirect_to'

