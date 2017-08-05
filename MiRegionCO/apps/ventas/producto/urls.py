from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from apps.ventas.producto.views import *

urlpatterns = [
    url(r'^crear_producto', login_required(ProductoCreate.as_view()), name='crear_producto'),
    url(r'^listar_producto', login_required(ProductoList.as_view()), name='listar_producto'),
    url(r'^editar_producto/(?P<pk>\d+)', login_required(ProductoUpdate.as_view()), name='editar_producto'),
    url(r'^eliminar_producto/(?P<pk>\d+)', login_required(ProductoDelete.as_view()), name='eliminar_producto')
]
