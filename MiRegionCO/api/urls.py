from django.conf.urls import url
from api.views import *
from fcm_django.api.rest_framework import *

urlpatterns = [

    url(r'^crear_usuario', CrearUsuarioAPI.as_view(), name='usuario_api'),
    #  listado de usuario por id fb
    url(r'^usuario/(?P<id_facebook>.+)$', ObtenerUsuarioAPI.as_view(), name='obtener_usuario_api'),
    # listado de usuarios con noticias y sitios
    url(r'^usuarios', UsuariosAPI.as_view(), name='usuario_api'),
    # listado de todas las noticias
    url(r'^news_feed', NewsFeed.as_view(), name='news_feed_api'),
    url(r'^pagination_news_feed', NewsFeed2.as_view(), name='news_feed2_api'),
    url(r'^pagination_news_web', NewsFeedWeb.as_view(), name='web_news_feed2_api'),
    # listado de noticias por id de la categoria
    url(r'^noticias/(?P<id_categoria>.+)$', NoticiasCategoriaListId.as_view(), name='noticias_api'),
    url(r'^pagination_noticias/(?P<id_categoria>.+)$', NoticiasCategoriaListId2.as_view(), name='noticias2_api'),
    # listado de todos los sitios
    url(r'^sitios', SitiosList.as_view(), name='list_sitio_api'),
    # listado de sitios por el id de la subcategoria del mapa
    url(r'^subcategoria_sitios/(?P<id_subcategoria>.+)$', SitiosXSubcategoria, name='sitios_by_subcategoria'),
    # noticias destacadas
    url(r'^noticias_destacadas', NoticiasDestacadasAPI.as_view(), name='noticias_destacadas_api'),
    # noticias destacadas por el id de la categoria
    url(r'^destacados_categoria/(?P<id_categoria>.+)/$', NoticiasDestacadasCategoriaAPI.as_view(),
        name='noticias_destacadas_categoria_api'),
    # listado de categoria de noticias
    url(r'^categoria', CategoriaNoticiasAPI.as_view(), name='noticias_destacadas_api'),
    # categoria, subcategoria y sitios del mapa
    url(r'^mapa_categoria', MapaListAPI.as_view(), name='categorias_mapa_api'),
    # crear noticias
    url(r'^crear_noticia', NoticiasAPI.as_view(), name='noticia_api'),
    # guardar noticia al usuario
    url(r'^guardar_noticia', noticiausuario, name='guardar_noticia_usuario'),
    url(r'^eliminar_noticia/(?P<id_facebook>.+)/(?P<id_noticia>.+)$', eliminarnoticia, name='eliminar_noticia_usuario'),
    url(r'^crear_sitio/$', CrearSitio, name='crear_sitio'),
    url(r'^guardar_sitio', sitiousuario, name='guardar_noticia_usuario'),
    url(r'^eliminar_sitio/(?P<id_facebook>.+)/(?P<id_sitio>.+)$', eliminarsitio, name='eliminar_noticia_usuario'),
    # actualizar numero del usuario
    url(r'^actualizar_telefono', actualizartelefono, name='actualizar_telefono_sitio'),
    # estadistica (visualizar noticia)
    url(r'^visualizacion_noticia', ViewsNews.as_view(), name='visualizar_noticia_api'),
    url(r'^comparte_noticia', SharedNews.as_view(), name='comparte_noticia_api'),
    url(r'^guarda_noticia', SaveNews.as_view(), name='guardar_noticia_api'),
    url(r'^visita_sitio', VisitPlace.as_view(), name='visitar_sitio_api'),
    url(r'^llamada_sitio', CallPlace.as_view(), name='llamar_sitio_api'),
    url(r'^ingreso', Login.as_view(), name='ingreso_api'),
    url(r'^facebook_sitio', FacebookAPI.as_view(), name='ingreso_api'),
    url(r'^instagram_sitio', InstagramAPI.as_view(), name='ingreso_api'),
    url(r'^usuario_vista_login/$', LoginUserAPI.as_view(), name='usuario_vista_login'),
    # ESTADISTICAS PAGINA WEB
    url(r'^visita_index_web/$', VisitIndexAPI.as_view(), name='visita_index_web'),
    url(r'^visita_noticia_web/$', VisitNewsAPI.as_view(), name='visita_noticia_web'),
    url(r'^comparte_facebook_web/$', ShareFacebookAPI.as_view(), name='comparte_facebook_web'),
    url(r'^comparte_twitter_web/$', ShareTwitterAPI.as_view(), name='comparte_twitter_web'),
    url(r'^comparte_google_web/$', ShareGoogleAPI.as_view(), name='comparte_google_web'),
    url(r'^visita_mapa_web/$', VisitMapAPI.as_view(), name='visita_mapa_web'),
    url(r'^web_visita_sitio/$', VisitPlaceAPI.as_view(), name='visita_sitio_web'),
    # Buscar noticias por texto (Buscador pagina web)
    url(r'^noticias_text/(?P<p_texto>.*)$', NoticiaByText.as_view(), name='search_noticia_text'),

    # urls de Apis mi region_ventas
    url(r'^login/(?P<p_correo>.+)/(?P<p_pass>.+)$', login, name='login_vendedor'),
    # listado de portafolio de ventas
    url(r'^portafolio', PortafolioAPI.as_view(), name='api_portafolio'),
    # crear cotizacion
    url(r'^cotizacion', CrearCotizacionAPI.as_view(), name='api_cotizacion'),
    # listado de cotizaciones por id del vendedor
    url(r'^listado_vendedor/(?P<id_vendedor>.+)$', ListCotizaciones, name='cotizaciones_vendedor'),
    # creacion de notificaciones
    url(r'^fcm_create/$', FCM_CREATE, name='fcm_create'),
    url(r'^fcm_list/$', FCMDeviceViewSet.as_view({'get': 'list'}), name='fcm_list'),
    # Votaciones Youtuber
    url(r'^votar_youtuber/$', VotarYoutuber.as_view(), name='votar_youtuber'),
    url(r'^listado_concursantes/$', ListadoConcursantes, name='listado_concursantes'),

]
