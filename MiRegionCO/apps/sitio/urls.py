from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from apps.sitio.views import *

urlpatterns = [
    url(r'^crear_sitio', login_required(SitioCreate.as_view()), name='crear_sitio'),
    url(r'^listar_sitio', login_required(SitioList.as_view()), name='listar_sitio'),
    url(r'^editar_sitio/(?P<pk>\d+)/$', login_required(SitioUpdate.as_view()), name='editar_sitio'),
    url(r'^eliminar_sitio/(?P<pk>\d+)/$', login_required(SitioDelete.as_view()), name='eliminar_sitio'),
]