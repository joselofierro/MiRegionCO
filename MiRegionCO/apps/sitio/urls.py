from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from apps.sitio.views import *

urlpatterns = [
    url(r'^crear_sitio', login_required(SitioCreate.as_view()), name='crear'),
    url(r'^listar_sitio', login_required(SitioList.as_view()), name='listar'),
    url(r'^editar_sitio/(?P<pk>\d+)/$', login_required(SitioUpdate.as_view()), name='editar'),
    url(r'^eliminar_sitio/(?P<pk>\d+)/$', login_required(SitioDelete.as_view()), name='eliminar'),
    url(r'^delete_imagen', login_required(deleteimagen), name='delete_imagen'),
]