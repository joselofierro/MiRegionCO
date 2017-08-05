from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from apps.ventas.detalle.views import *

urlpatterns = [
    url(r'^crear_detalle', login_required(DetalleCreate.as_view()), name='crear_detalle'),
    url(r'^listar_detalle', login_required(DetalleList.as_view()), name='listar_detalle'),
    url(r'^editar_detalle/(?P<pk>\d+)/$', login_required(DetalleUpdate.as_view()), name='editar_detalle'),
    url(r'^eliminar_detalle/(?P<pk>\d+)/$', login_required(DetalleDelete.as_view()), name='eliminar_detalle')

]
