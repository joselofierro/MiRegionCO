"""MiRegionCO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, \
    password_reset_complete

from MiRegionCO import settings

urlpatterns = [

    url(r'^', include('apps.grupo.urls', namespace='grupo')),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('api.urls', namespace='api')),
    url(r'^categoria/', include('apps.categoria.urls', namespace='categorias')),
    url(r'^categoria_mapa/', include('apps.categoria_mapa.urls', namespace='mapa')),
    url(r'^subcategoria_mapa/', include('apps.subcategoria_mapa.urls', namespace='sub_mapa')),
    url(r'^imagen/', include('apps.imagen.urls', namespace='imagen')),
    url(r'^noticia/', include('apps.noticia.urls', namespace='noticia')),
    url(r'^sitio/', include('apps.sitio.urls', namespace='sitio')),
    url(r'^tag/', include('apps.tag.urls', namespace='tag')),
    url(r'^usuario/', include('apps.usuario.urls', namespace='usuario')),
    url(r'^estadistica/', include('apps.estadistica.urls', namespace='estadistica')),
    url(r'^categoria_producto/', include('apps.ventas.categoria_producto.urls', namespace='categoria_producto')),
    url(r'^cliente/', include('apps.ventas.cliente.urls', namespace='cliente')),
    url(r'^cotizacion/', include('apps.ventas.cotizacion.urls', namespace='cotizacion')),
    url(r'^detalle/', include('apps.ventas.detalle.urls', namespace='detalle')),
    url(r'^producto/', include('apps.ventas.producto.urls', namespace='producto')),
    url(r'^subcategoria_producto/',
        include('apps.ventas.subcategoria_producto.urls', namespace='subcategoria_producto')),
    url(r'^vendedor/', include('apps.ventas.vendedor.urls', namespace='vendedor')),
    url(r'notificacion/', include('apps.notificaciones.urls', namespace='notificacion')),
    url(r'youtuber/', include('apps.activacion_youtuber.urls', namespace='youtuber')),
    url(r'^reset/password_reset', password_reset,
        {'template_name': 'password/password_reset_form.html',
         'email_template_name': 'password/password_reset_email.html'},
        name='password_reset'),
    url(r'^password_reset_done', password_reset_done,
        {'template_name': 'password/password_reset_done.html'},
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', password_reset_confirm,
        {'template_name': 'password/password_reset_confirm.html'},
        name='password_reset_confirm'
        ),
    url(r'^reset/done', password_reset_complete, {'template_name': 'password/password_reset_complete.html'},
        name='password_reset_complete'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
