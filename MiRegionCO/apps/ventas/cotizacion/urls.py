from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from apps.ventas.cotizacion.views import *

urlpatterns = [
    url(r'^crear_cotizacion', login_required(CotizacionCreate.as_view()), name='crear_cotizacion'),
    url(r'^listar_cotizacion', login_required(CotizacionList.as_view()), name='listar_cotizacion'),
    url(r'^editar_cotizacion/(?P<pk>\d+)/$', login_required(CotizacionUpdate.as_view()), name='editar_cotizacion'),
    url(r'^eliminar_cotizacion/(?P<pk>\d+)/$', login_required(CotizacionDelete.as_view()), name='eliminar_cotizacion'),
]