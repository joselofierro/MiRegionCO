from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import *

from apps.sitio.forms import SitioForm
from apps.sitio.models import Sitio


class SitioCreate(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Sitio
    form_class = SitioForm
    template_name = 'sitio/sitio_form.html'
    success_url = reverse_lazy('sitio:listar_sitio')
    success_message = 'Se ha creado el sitio correctamente.'
    permission_required = ('sitio.add_sitio', 'sitio.change_sitio')
    raise_exception = False
    login_url = reverse_lazy('grupo:login')
    redirect_field_name = 'redirect_to'


class SitioList(PermissionRequiredMixin, ListView):
    model = Sitio
    template_name = 'sitio/sitio_list.html'
    permission_required = ('sitio.add_sitio', 'sitio.change_sitio')
    raise_exception = False
    login_url = reverse_lazy('grupo:login')
    redirect_field_name = 'redirect_to'


class SitioUpdate(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Sitio
    form_class = SitioForm
    template_name = 'sitio/sitio_form.html'
    success_url = reverse_lazy('sitio:listar_sitio')
    success_message = 'Se ha actualizado el sitio correctamente.'
    permission_required = ('sitio.add_sitio', 'sitio.change_sitio')
    raise_exception = False
    login_url = reverse_lazy('grupo:login')
    redirect_field_name = 'redirect_to'


class SitioDelete(PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Sitio
    template_name = 'sitio/sitio_delete.html'
    success_url = reverse_lazy('sitio:listar_sitio')
    success_message = 'Se ha eliminado el sitio correctamente.'
    permission_required = ('sitio.add_sitio', 'sitio.change_sitio')
    raise_exception = False
    login_url = reverse_lazy('grupo:login')
    redirect_field_name = 'redirect_to'
