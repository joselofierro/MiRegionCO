from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^categorias/(?P<categoria_nombre>.+)/$', noticias_categoria, name='noticia_categoria'),
    # expresion regular alfanumerica
    url(r'^noticias/(?P<slug>[-\w]+)/$', noticia_id, name='noticia_id'),
    url(r'^mapa$', mapa, name='mapa'),
]
