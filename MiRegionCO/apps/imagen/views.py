from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import *

from apps.imagen.forms import ImagenForm
from apps.imagen.models import Imagen


class ImagenCreate(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Imagen
    form_class = ImagenForm
    template_name = 'imagen/imagen_form.html'
    success_url = reverse_lazy('imagen:imagen_listar')
    success_message = 'Se ha creado la imagen satisfactoriamente.'
    permission_required = ('imagen.add_imagen', 'imagen.change_imagen')
    raise_exception = False
    login_url = reverse_lazy('grupo:login')
    redirect_field_name = 'redirect_to'


class ImagenList(PermissionRequiredMixin, ListView):
    model = Imagen
    template_name = 'imagen/imagen_list.html'
    permission_required = ('imagen.add_imagen', 'imagen.change_imagen')
    raise_exception = False
    login_url = reverse_lazy('grupo:login')
    redirect_field_name = 'redirect_to'


class ImagenUpdate(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Imagen
    form_class = ImagenForm
    template_name = 'imagen/imagen_form.html'
    success_url = reverse_lazy('imagen:imagen_listar')
    success_message = 'Se ha creado la imagen satisfactoriamente.'
    permission_required = ('imagen.add_imagen', 'imagen.change_imagen')
    raise_exception = False
    login_url = reverse_lazy('grupo:login')
    redirect_field_name = 'redirect_to'


class ImagenDelete(PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Imagen
    template_name = 'imagen/imagen_delete.html'
    success_url = reverse_lazy('imagen:imagen_listar')
    success_message = 'Se ha creado la imagen satisfactoriamente.'
    permission_required = ('imagen.add_imagen', 'imagen.change_imagen')
    raise_exception = False
    login_url = reverse_lazy('grupo:login')
    redirect_field_name = 'redirect_to'
