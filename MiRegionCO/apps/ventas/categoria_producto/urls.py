from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from apps.ventas.categoria_producto.views import *

urlpatterns = [
    url(r'^nueva_categoria_producto', login_required(CategoriaProductoCreate.as_view()),
        name='nueva_categoria_producto'),
    url(r'^listar_categoria_producto', login_required(CategoriaProductoList.as_view()),
        name='listar_categoria_producto'),
    url(r'^editar_categoria_producto/(?P<pk>\d+)/$', login_required(CategoriaProductoUpdate.as_view()),
        name='editar_categoria_producto'),
    url(r'^eliminar_categoria_producto/(?P<pk>\d+)/$', login_required(CategoriaProductoDelete.as_view()),
        name='eliminar_categoria_producto'),
]
