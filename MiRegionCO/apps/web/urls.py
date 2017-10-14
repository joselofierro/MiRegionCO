from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^categoria/(?P<p_categoria_id>.+)/$', noticias_categoria, name='noticia_categoria'),
    url(r'^noticia/(?P<p_id>.+)/$', noticia_id, name='noticia_id'),
    url(r'^mapa$', mapa, name='mapa'),
]
