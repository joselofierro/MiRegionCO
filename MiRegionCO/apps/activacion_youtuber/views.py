from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import *

from apps.activacion_youtuber.forms import YoutuberForm
from apps.activacion_youtuber.models import Youtuber


class YoutuberCreate(PermissionRequiredMixin, SuccessMessageMixin,CreateView):
    model = Youtuber
    form_class = YoutuberForm
    template_name = 'youtuber/youtuber_form.html'
    success_url = reverse_lazy('youtuber:listar')
    success_message = 'Se ha creado el youtuber correctamente'
    permission_required = ('activacion_youtuber.add_youtuber', 'activacion_youtuber.change_youtuber')
    raise_exception = False
    login_url = reverse_lazy('grupo:login')
    redirect_field_name = 'redirect_to'


class YoutuberList(PermissionRequiredMixin,ListView):
    model = Youtuber
    template_name = 'youtuber/youtuber_list.html'
    permission_required = ('activacion_youtuber.add_youtuber', 'activacion_youtuber.change_youtuber')
    raise_exception = False
    login_url = reverse_lazy('grupo:login')
    redirect_field_name = 'redirect_to'


class YoutuberUpdate(PermissionRequiredMixin, SuccessMessageMixin,UpdateView):
    model = Youtuber
    form_class = YoutuberForm
    template_name = 'youtuber/youtuber_form.html'
    success_url = reverse_lazy('youtuber:listar')
    success_message = 'Se ha actualizado el youtuber correctamente'
    permission_required = ('activacion_youtuber.add_youtuber', 'activacion_youtuber.change_youtuber')
    raise_exception = False
    login_url = reverse_lazy('grupo:login')
    redirect_field_name = 'redirect_to'


class YoutuberDelete(PermissionRequiredMixin, SuccessMessageMixin,DeleteView):
    model = Youtuber
    template_name = 'youtuber/youtuber_delete.html'
    success_url = reverse_lazy('youtuber:listar')
    success_message = 'Se ha eliminado el youtuber correctamente'
    permission_required = ('activacion_youtuber.add_youtuber', 'activacion_youtuber.change_youtuber', 'activacion_youtuber.delete_youtuber')
    raise_exception = False
    login_url = reverse_lazy('grupo:login')
    redirect_field_name = 'redirect_to'

