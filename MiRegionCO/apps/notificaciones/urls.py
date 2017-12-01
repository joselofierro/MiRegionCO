from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from apps.notificaciones.views import *

urlpatterns = [
    url(r'^crear_notificacion/$', login_required(NotificacionCreate.as_view()), name='crear_notificacion'),
    url(r'^listar_notificacion/$', login_required(NotificacionList.as_view()), name='listar_notificacion')
]
