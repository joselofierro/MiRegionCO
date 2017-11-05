from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^categorias/(?P<p_categoria_id>.+)/$', noticias_categoria, name='noticia_categoria'),
    url(r'^noticias/(?P<p_id>.+)/$', noticia_id, name='noticia_id'),
    url(r'^mapa$', mapa, name='mapa'),
]
