from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import *
from fcm_django.models import FCMDevice

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
        titulo = form.data['titulo']
        mensaje = form.data['mensaje']
        # Obtenemos los usuarios Android
        usuarios_android = FCMDevice.objects.filter(type='android')
        # Enviamos la notificacion
        usuarios_android.send_message(data={'titulo': titulo, 'mensaje': mensaje})

        # Obtenemos los usuarios ios
        usuarios_ios = FCMDevice.objects.filter(type='ios')
        # Enviamos la notificacion
        usuarios_ios.send_message(title=titulo, body=mensaje, sound='default')

        # Obtenemos a cuantos dispositivos ha llegado la notificación
        usuarios_notificados = FCMDevice.objects.filter(active=True).count()

        self.success_message = "La notificación ha llegado a " + str(usuarios_notificados) + " usuario"

        # Eliminamos los usuarios inactivos
        FCMDevice.objects.filter(active=False).delete()

        return super(NotificacionCreate, self).form_valid(form)


class NotificacionList(PermissionRequiredMixin, ListView):
    model = Notificacion
    paginate_by = 10
    template_name = 'notificaciones/notificacion_list.html'
    permission_required = ('notificacion.add_notificacion', 'notificacion.change_notificacion')
    # me devuelve al login si es falso y si es true arroja un exceptionError
    raise_exception = False
    # si no tengo los permisos me redirige al login
    login_url = reverse_lazy('grupo:login')
    redirect_field_name = 'redirect_to'
