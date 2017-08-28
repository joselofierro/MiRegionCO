from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.cache import caches


# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import *

from MiRegionCO import settings
from apps.sitio.forms import SitioForm
from apps.sitio.models import Sitio


class SitioCreate(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Sitio
    form_class = SitioForm
    template_name = 'sitio/sitio_form.html'
    success_url = reverse_lazy('sitio:listar')
    success_message = 'Se ha creado el sitio correctamente.'
    permission_required = ('sitio.add_sitio', 'sitio.change_sitio')
    raise_exception = False
    login_url = reverse_lazy('grupo:login')
    redirect_field_name = 'redirect_to'

    def form_valid(self, form):
        caches[settings.CACHE_API_SITIOS].clear()
        return super(SitioCreate, self).form_valid(form)


class SitioList(PermissionRequiredMixin, ListView):
    model = Sitio
    template_name = 'sitio/sitio_list.html'
    permission_required = ('sitio.add_sitio', 'sitio.change_sitio')
    raise_exception = False
    login_url = reverse_lazy('grupo:login')
    redirect_field_name = 'redirect_to'

    def get_queryset(self):
        return Sitio.objects.order_by('nombre')


class SitioUpdate(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Sitio
    form_class = SitioForm
    template_name = 'sitio/sitio_form.html'
    success_url = reverse_lazy('sitio:listar')
    success_message = 'Se ha actualizado el sitio correctamente.'
    permission_required = ('sitio.add_sitio', 'sitio.change_sitio')
    raise_exception = False
    login_url = reverse_lazy('grupo:login')
    redirect_field_name = 'redirect_to'

    def form_valid(self, form):
        caches[settings.CACHE_API_SITIOS].clear()
        return super(SitioUpdate, self).form_valid(form)


class SitioDelete(PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Sitio
    template_name = 'sitio/sitio_delete.html'
    success_url = reverse_lazy('sitio:listar')
    success_message = 'Se ha eliminado el sitio correctamente.'
    permission_required = ('sitio.add_sitio', 'sitio.change_sitio')
    raise_exception = False
    login_url = reverse_lazy('grupo:login')
    redirect_field_name = 'redirect_to'

    def post(self, request, *args, **kwargs):
        caches[settings.CACHE_API_SITIOS].clear()
        return super(SitioDelete, self).post(args, kwargs)
