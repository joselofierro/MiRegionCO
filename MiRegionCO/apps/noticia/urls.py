from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from apps.noticia.views import *

urlpatterns = [
    url(r'^nueva_noticia', login_required(NoticiaCreate.as_view()), name='crear'),
    url(r'^listar_noticia', login_required(NoticiaList.as_view()), name='listar'),
    url(r'^editar_noticia/(?P<pk>\d+)/$', login_required(NoticiaUpdate.as_view()), name='actualizar'),
    url(r'^eliminar_noticia/(?P<pk>\d+)/$', login_required(eliminarnoticia), name='eliminar'),
    url(r'^delete_imagen', login_required(deleteimage), name='delete_imagen')
]
