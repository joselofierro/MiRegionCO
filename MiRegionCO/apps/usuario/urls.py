from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from apps.usuario.views import UsuarioList

urlpatterns = [
    url(r'^listar_usuario', login_required(UsuarioList.as_view()), name='listar_usuario')
]
