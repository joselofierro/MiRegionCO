from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from apps.subcategoria_mapa.views import *

urlpatterns = [
    url(r'^crear_subcategoria', login_required(SubcategoriaMapaCreate.as_view()), name='crear_subcategoria_mapa'),
    url(r'^listar_subcategoria', login_required(SubcategoriaMapaList.as_view()), name='listar_subcategoria_mapa'),
    url(r'^actualizar_subcategoria/(?P<pk>\d+)/$', login_required(SubcategoriaMapaUpdate.as_view()),
        name='actualizar_subcategoria_mapa'),
    url(r'^eliminar_subcategoria/(?P<pk>\d+)/$', login_required(SubcategoriaMapaDelete.as_view()),
        name='eliminar_subcategoria_mapa'),
]
