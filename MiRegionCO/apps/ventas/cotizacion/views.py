from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.cache import caches
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import *

from MiRegionCO import settings
from apps.ventas.cotizacion.forms import CotizacionForm
from apps.ventas.cotizacion.models import Cotizacion
from apps.ventas.detalle.models import Detalle


class CotizacionCreate(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Cotizacion
    form_class = CotizacionForm
    template_name = 'ventas/cotizacion/cotizacion_form.html'
    success_url = reverse_lazy('cotizacion:listar_cotizacion')
    success_message = 'Se ha creado la cotización con exito'
    permission_required = ('cotizacion.add_cotizacion', 'cotizacion.change_cotizacion')
    # me devuelve al login si es falso y si es true arroja un exceptionError
    raise_exception = False
    # si no tengo los permisos me redirige al login
    login_url = reverse_lazy('user:index')
    redirect_field_name = 'redirect_to'

    def form_valid(self, form):
        caches[settings.CACHE_API_COTIZACIONES].clear()
        return super(CotizacionCreate, self).form_valid(form)


class CotizacionList(PermissionRequiredMixin, ListView):
    model = Cotizacion
    template_name = 'ventas/cotizacion/cotizacion_list.html'
    permission_required = ('cotizacion.add_cotizacion', 'cotizacion.change_cotizacion')
    # me devuelve al login si es falso y si es true arroja un exceptionError
    raise_exception = False
    # si no tengo los permisos me redirige al login
    login_url = reverse_lazy('user:index')
    redirect_field_name = 'redirect_to'


class CotizacionUpdate(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Cotizacion
    form_class = CotizacionForm
    template_name = 'ventas/cotizacion/cotizacion_form.html'
    success_url = reverse_lazy('cotizacion:listar_cotizacion')
    success_message = 'Se ha actualizado la cotización con exito'
    permission_required = ('cotizacion.add_cotizacion', 'cotizacion.change_cotizacion')
    # me devuelve al login si es falso y si es true arroja un exceptionError
    raise_exception = False
    # si no tengo los permisos me redirige al login
    login_url = reverse_lazy('user:index')
    redirect_field_name = 'redirect_to'

    def form_valid(self, form):
        caches[settings.CACHE_API_COTIZACIONES].clear()
        return super(CotizacionUpdate, self).form_valid(form)


class CotizacionDelete(PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Cotizacion
    template_name = 'ventas/cotizacion/cotizacion_delete.html'
    success_url = reverse_lazy('cotizacion:listar_cotizacion')
    success_message = 'Se ha eliminado la cotización con exito'
    permission_required = ('cotizacion.add_cotizacion', 'cotizacion.change_cotizacion')
    # me devuelve al login si es falso y si es true arroja un exceptionError
    raise_exception = False
    # si no tengo los permisos me redirige al login
    login_url = reverse_lazy('user:index')
    redirect_field_name = 'redirect_to'

    def post(self, request, *args, **kwargs):
        caches[settings.CACHE_API_COTIZACIONES].clear()
        return super(CotizacionDelete, self).post(args, kwargs)
