from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from apps.imagen.views import *

urlpatterns = [
    url(r'^nueva_imagen', login_required(ImagenCreate.as_view()), name='imagen_crear'),
    url(r'^listar_imagen', login_required(ImagenList.as_view()), name='imagen_listar'),
    url(r'^editar_imagen/(?P<pk>\d+)/$', login_required(ImagenUpdate.as_view()), name='imagen_editar'),
    url(r'^eliminar_imagen/(?P<pk>\d+)/$', login_required(ImagenDelete.as_view()), name='imagen_eliminar'),
]