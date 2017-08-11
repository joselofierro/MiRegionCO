from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import *

from apps.notificaciones.forms import NotificacionForm
from apps.notificaciones.models import Notificacion


class NotificacionCreate(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Notificacion
    form_class = NotificacionForm
    template_name = 'notificaciones/notificacion_form.html'
    success_url = reverse_lazy('notificacion:listar_notificacion')
    success_message = 'Se ha creado la notificación con exito'
    permission_required = ('notificacion.add_notificacion', 'notificacion.change_notificacion')
    # me devuelve al login si es falso y si es true arroja un exceptionError
    raise_exception = False
    # si no tengo los permisos me redirige al login
    login_url = reverse_lazy('grupo:login')
    redirect_field_name = 'redirect_to'

    def form_valid(self, form):
        return super(NotificacionCreate, self).form_valid(form)


class NotificacionList(PermissionRequiredMixin, ListView):
    model = Notificacion
    template_name = 'notificaciones/notificacion_list.html'
    permission_required = ('notificacion.add_notificacion', 'notificacion.change_notificacion')
    # me devuelve al login si es falso y si es true arroja un exceptionError
    raise_exception = False
    # si no tengo los permisos me redirige al login
    login_url = reverse_lazy('grupo:login')
    redirect_field_name = 'redirect_to'

