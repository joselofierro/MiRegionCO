from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import *

from apps.tag.forms import TagForm
from apps.tag.models import Tag


class TagCreate(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Tag
    form_class = TagForm
    template_name = 'tag/tag_form.html'
    success_url = reverse_lazy('tag:listar_tag')
    success_message = 'Se ha creado el tag correctamente'
    permission_required = ('tag.add_tag', 'tag.change_tag')
    raise_exception = False
    login_url = reverse_lazy('user:index')
    redirect_field_name = 'redirect_to'


class TagList(PermissionRequiredMixin, ListView):
    model = Tag
    template_name = 'tag/tag_list.html'
    paginate_by = 10
    permission_required = ('tag.add_tag', 'tag.change_tag')
    raise_exception = False
    login_url = reverse_lazy('user:index')
    redirect_field_name = 'redirect_to'


class TagUpdate(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Tag
    form_class = TagForm
    template_name = 'tag/tag_form.html'
    success_url = reverse_lazy('tag:listar_tag')
    success_message = 'Se ha actualizado el tag correctamente'
    permission_required = ('tag.add_tag', 'tag.change_tag')
    raise_exception = False
    login_url = reverse_lazy('user:index')
    redirect_field_name = 'redirect_to'


class TagDelete(PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Tag
    template_name = 'tag/tag_delete.html'
    success_url = reverse_lazy('tag:listar_tag')
    success_message = 'Se ha eliminado el tag correctamente'
    permission_required = ('tag.add_tag', 'tag.change_tag')
    raise_exception = False
    login_url = reverse_lazy('user:index')
    redirect_field_name = 'redirect_to'
