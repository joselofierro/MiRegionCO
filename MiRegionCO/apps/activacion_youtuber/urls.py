from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import *

urlpatterns = [
    url(r'^crear', login_required(YoutuberCreate.as_view()), name='crear'),
    url(r'^listar', login_required(YoutuberList.as_view()), name='listar'),
    url(r'^editar/(?P<pk>.*)/$', login_required(YoutuberUpdate.as_view()), name='editar'),
    url(r'^eliminar/(?P<pk>.*)/$', login_required(YoutuberDelete.as_view()), name='eliminar'),
]