from django.conf.urls import url
from apps.notificaciones.views import *

urlpatterns = [
    url(r'^crear_notificacion', NotificacionCreate.as_view(), name='crear_notificacion'),
    url(r'^listar_notificacion', NotificacionList.as_view(), name='listar_notificacion')
]