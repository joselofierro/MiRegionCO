from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from apps.ventas.subcategoria_producto.views import *

urlpatterns = [
    url(r'^crear_subcategoria', login_required(SubcategoriaCreate.as_view()), name='crear_subcategoria'),
    url(r'^listar_subcategoria', login_required(SubcategoriaList.as_view()), name='listar_subcategoria'),
    url(r'^editar_subcategoria/(?P<pk>\d+)/$', login_required(SubcategoriaUpdate.as_view()),
        name='editar_subcategoria'),
    url(r'^eliminar_subcategoria/(?P<pk>\d+)/$', login_required(SubcategoriaDelete.as_view()),
        name='eliminar_subcategoria'),
]
