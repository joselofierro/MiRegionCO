from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from apps.usuario.models import Usuario


class UsuarioList(ListView):
    model = Usuario
    template_name = 'usuario/usuario_list.html'
