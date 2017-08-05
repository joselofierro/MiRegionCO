from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from apps.noticia.views import *

urlpatterns = [
    url(r'^nueva_noticia', login_required(NoticiaCreate.as_view()), name='crear_noticia'),
    url(r'^listar_noticia', login_required(NoticiaList.as_view()), name='listar_noticia'),
    url(r'^editar_noticia/(?P<pk>\d+)/$', login_required(NoticiaUpdate.as_view()), name='actualizar_noticia'),
    url(r'^eliminar_noticia/(?P<pk>\d+)/$', login_required(NoticiaDelete.as_view()), name='eliminar_noticia')
]
