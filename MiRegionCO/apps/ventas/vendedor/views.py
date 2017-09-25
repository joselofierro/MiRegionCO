from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect, request
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import *

from apps.ventas.vendedor.forms import VendedorForm
from apps.ventas.vendedor.models import Vendedor


class VendedorCreate(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Vendedor
    form_class = VendedorForm
    template_name = 'ventas/vendedor/vendedor_form.html'
    success_url = reverse_lazy('vendedor:listar_vendedor')
    success_message = 'Se ha creado con exito el vendedor'
    permission_required = ('vendedor.add_vendedor', 'vendedor.change_vendedor')
    # me devuelve al login si es falso y si es true arroja un exceptionError
    raise_exception = False
    # si no tengo los permisos me redirige al login
    login_url = reverse_lazy('grupo:login')
    redirect_field_name = 'redirect_to'

    def form_valid(self, form):
        contra = form.data['contrasena']
        contra_cifrada = make_password(contra, salt=None, hasher='sha1')
        if check_password(contra, contra_cifrada):
            return HttpResponseRedirect(self.get_success_url())
        else:
            return render(request, self.template_name, {'form': form})


class VendedorList(PermissionRequiredMixin, ListView):
    model = Vendedor
    template_name = 'ventas/vendedor/vendedor_list.html'
    permission_required = ('vendedor.add_vendedor', 'vendedor.change_vendedor')
    # me devuelve al login si es falso y si es true arroja un exceptionError
    raise_exception = False
    # si no tengo los permisos me redirige al login
    login_url = reverse_lazy('grupo:login')
    redirect_field_name = 'redirect_to'


class VendedorUpdate(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Vendedor
    form_class = VendedorForm
    template_name = 'ventas/vendedor/vendedor_form.html'
    success_url = reverse_lazy('vendedor:listar_vendedor')
    success_message = 'Se ha actualizado con exito el vendedor'
    permission_required = ('vendedor.add_vendedor', 'vendedor.change_vendedor')
    # me devuelve al login si es falso y si es true arroja un exceptionError
    raise_exception = False
    # si no tengo los permisos me redirige al login
    login_url = reverse_lazy('grupo:login')
    redirect_field_name = 'redirect_to'


class VendedorDelete(PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Vendedor
    template_name = 'ventas/vendedor/vendedor_form.html'
    success_url = reverse_lazy('vendedor:listar_vendedor')
    success_message = 'Se ha eliminado con exito el vendedor'
    permission_required = ('vendedor.add_vendedor', 'vendedor.change_vendedor')
    # me devuelve al login si es falso y si es true arroja un exceptionError
    raise_exception = False
    # si no tengo los permisos me redirige al login
    login_url = reverse_lazy('grupo:login')
    redirect_field_name = 'redirect_to'
