from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from apps.ventas.cliente.views import *

urlpatterns = [
  url(r'^listar_cliente', login_required(ClienteList.as_view()), name='listar_cliente')
]
