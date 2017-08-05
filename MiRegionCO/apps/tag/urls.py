from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from apps.tag.views import *

urlpatterns = [
    url(r'^crear_tag', login_required(TagCreate.as_view()), name='crear_tag'),
    url(r'^listar_tag', login_required(TagList.as_view()), name='listar_tag'),
    url(r'^editar_tag/(?P<pk>\d+)/$', login_required(TagUpdate.as_view()), name='editar_tag'),
    url(r'^eliminar_tag/(?P<pk>\d+)/$', login_required(TagDelete.as_view()), name='eliminar_tag'),
]