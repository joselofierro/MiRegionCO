from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from apps.categoria_mapa.views import *

urlpatterns = [
    url(r'^nueva_categoria', login_required(CategoriaMapaCreate.as_view()), name='categoria_crear'),
    url(r'^listar_categoria', login_required(CategoriaMapaList.as_view()), name='categoria_listar'),
    url(r'^editar_categoria/(?P<pk>\d+)/$', login_required(CategoriaMapaUpdate.as_view()), name='categoria_editar'),
    url(r'^eliminar_categoria/(?P<pk>\d+)/$', login_required(CategoriaMapaDelete.as_view()), name='categoria_eliminar'),
]