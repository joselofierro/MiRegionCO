
# Create your views here.

from django.views.generic import *
from apps.ventas.cliente.models import Cliente


class ClienteList(ListView):
    model = Cliente
    template_name = 'ventas/cliente/cliente_list.html'
