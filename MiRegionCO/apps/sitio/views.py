from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.cache import caches

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import *

from MiRegionCO import settings
from apps.imagen.forms import ImagenForm
from apps.imagen.models import Imagen
from apps.sitio.forms import SitioForm
from apps.sitio.models import Sitio


class SitioCreate(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Sitio
    form_class = SitioForm
    second_form_class = ImagenForm
    template_name = 'sitio/sitio_form.html'
    success_url = reverse_lazy('sitio:listar')
    success_message = 'Se ha creado el sitio correctamente.'
    permission_required = ('sitio.add_sitio', 'sitio.change_sitio')
    raise_exception = False
    login_url = reverse_lazy('grupo:login')
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super(SitioCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.form_class(request.POST)
        files = request.FILES.getlist('imagen')

        if form.is_valid() and form2.is_valid():
            if len(request.FILES) != 0:
                list_img = []
                for indx, file in enumerate(files):
                    imagen = Imagen(nombre=form.data['nombre'] + "_" + str(indx), imagen=file)
                    list_img.append(imagen)

                noticia = form.save(commit=False)
                user = request.user
                noticia.autor = user
                noticia.save()

                for imagen in list_img:
                    noticia.imagenes.add(imagen)

                caches[settings.CACHE_API_SITIOS].clear()
                return HttpResponseRedirect(self.get_success_url())
            else:
                return render(request, self.template_name,
                              {'form': form, 'form2': form2, 'error': '¡La noticia no tiene imagen!'})
        else:
            return render(request, self.template_name, {'form': form, 'form2': form2})


class SitioList(PermissionRequiredMixin, ListView):
    model = Sitio
    template_name = 'sitio/sitio_list.html'
    permission_required = ('sitio.add_sitio', 'sitio.change_sitio')
    raise_exception = False
    login_url = reverse_lazy('grupo:login')
    redirect_field_name = 'redirect_to'

    def get_queryset(self):
        return Sitio.objects.order_by('nombre')


class SitioUpdate(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Sitio
    second_model = Imagen
    form_class = SitioForm
    second_form_class = ImagenForm
    template_name = 'sitio/sitio_form.html'
    success_url = reverse_lazy('sitio:listar')
    success_message = 'Se ha actualizado el sitio correctamente.'
    permission_required = ('sitio.add_sitio', 'sitio.change_sitio')
    raise_exception = False
    login_url = reverse_lazy('grupo:login')
    redirect_field_name = 'redirect_to'

    """def form_valid(self, form):
        caches[settings.CACHE_API_SITIOS].clear()
        return super(SitioUpdate, self).form_valid(form)"""

    def get_context_data(self, **kwargs):
        context = super(SitioUpdate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        pk = self.kwargs['pk']
        sitio = self.model.objects.get(id=pk)
        form_sitio = self.form_class(request.POST, instance=sitio)
        form_imagen = self.second_form_class(request.POST)

        if form_sitio.is_valid() and form_imagen.is_valid():
            form_sitio.save()
            form_imagen.save()

            caches[settings.CACHE_API_SITIOS].clear()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return render(request, self.template_name, {'form': form_sitio, 'form2': form_imagen})


class SitioDelete(PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Sitio
    template_name = 'sitio/sitio_delete.html'
    success_url = reverse_lazy('sitio:listar')
    success_message = 'Se ha eliminado el sitio correctamente.'
    permission_required = ('sitio.add_sitio', 'sitio.change_sitio')
    raise_exception = False
    login_url = reverse_lazy('grupo:login')
    redirect_field_name = 'redirect_to'

    def post(self, request, *args, **kwargs):
        caches[settings.CACHE_API_SITIOS].clear()
        return super(SitioDelete, self).post(args, kwargs)
