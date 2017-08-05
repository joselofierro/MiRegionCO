from django.conf.urls import url

from apps.estadistica.views import *

urlpatterns = [
    url(r'^estadistica', Estadisticas, name='estadistica')
]
