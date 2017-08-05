from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from apps.ventas.vendedor.views import *

urlpatterns = [
    url(r'^crear_vendedor', login_required(VendedorCreate.as_view()), name='crear_vendedor'),
    url(r'^listar_vendedor', login_required(VendedorList.as_view()), name='listar_vendedor'),
    url(r'^editar_vendedor/(?P<pk>\d+)/$', login_required(VendedorUpdate.as_view()), name='editar_vendedor'),
    url(r'^eliminar_vendedor/(?P<pk>\d+)/$', login_required(VendedorDelete.as_view()), name='eliminar_vendedor'),
]