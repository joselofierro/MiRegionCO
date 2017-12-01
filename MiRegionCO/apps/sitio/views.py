from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.cache import caches
# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import *

from MiRegionCO import settings
from apps.imagen.forms import ImagenForm
from apps.imagen.models import Imagen
from apps.sitio.forms import SitioForm
from apps.sitio.models import Sitio
from apps.subcategoria_mapa.models import SubcategoriaMapa


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
        form = self.form_class(request.POST, request.FILES)
        form2 = self.second_form_class(request.POST)
        files = request.FILES.getlist('imagen')
        subcategorias = request.POST.getlist('subcategoria')
        list_subcategorias = []
        list_img = []

        if form.is_valid() and form2.is_valid():
            if len(request.FILES) != 0:
                for indx, file in enumerate(files):
                    imagen = Imagen(nombre=form.data['nombre'] + "_" + str(indx), imagen=file)
                    imagen.save()
                    list_img.append(imagen)

                for subcategoria in subcategorias:
                    subcategoria_obj = SubcategoriaMapa.objects.get(id=subcategoria)
                    list_subcategorias.append(subcategoria_obj)

                sitio = form.save(commit=False)
                sitio.save()

                for imagen in list_img:
                    sitio.imagenes.add(imagen)

                for subcatg_id in list_subcategorias:
                    sitio.subcategoria.add(subcatg_id)

                caches[settings.CACHE_API_SITIOS].clear()
                caches[settings.CACHE_API_SITIOSXSUBCATEGORIA].clear()
                return HttpResponseRedirect(self.get_success_url())
            else:
                return render(request, self.template_name,
                              {'form': form, 'form2': form2, 'error': '¡El sitio no tiene imagen!'})
        else:
            return render(request, self.template_name, {'form': form, 'form2': form2})

    # tiempo de vida del cache 15min o infinito
    @method_decorator(cache_page(None))
    def dispatch(self, request, *args, **kwargs):
        return super(SitioCreate, self).dispatch(request, *args, **kwargs)


class SitioList(PermissionRequiredMixin, ListView):
    model = Sitio
    template_name = 'sitio/sitio_list.html'
    paginate_by = 10
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

    def get_context_data(self, **kwargs):
        context = super(SitioUpdate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        pk = kwargs['pk']
        sitio = self.model.objects.get(id=pk)
        form_sitio = self.form_class(request.POST, request.FILES, instance=sitio)
        form_imagen = self.second_form_class(request.POST, request.FILES)
        files = request.FILES.getlist('imagen')

        if form_sitio.is_valid() and form_imagen.is_valid():

            imagen_new = Imagen.objects.last()
            # recorremos las imagenes por indice y archivo que vienen del formulario
            for indx, file in enumerate(files):
                # creamos una instancia del modelo imagen
                imagen = Imagen(nombre=form_sitio.data['nombre'] + "_" + str(imagen_new.id + (indx + 1)), imagen=file)
                # guardamos el objeto
                imagen.save()
                # asignamos esas imagenes al sitio
                sitio.imagenes.add(imagen)

            sitio.save()
            form_sitio.save()

            caches[settings.CACHE_API_SITIOS].clear()
            caches[settings.CACHE_API_SITIOSXSUBCATEGORIA].clear()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return render(request, self.template_name, {'form': form_sitio, 'form2': form_imagen})

    """@method_decorator(cache_page(None))
    def dispatch(self, request, *args, **kwargs):
        return super(SitioUpdate, self).dispatch(request, *args, **kwargs)"""


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
        caches[settings.CACHE_API_SITIOSXSUBCATEGORIA].clear()
        return super(SitioDelete, self).post(args, kwargs)

    @method_decorator(cache_page(None))
    def dispatch(self, request, *args, **kwargs):
        return super(SitioDelete, self).dispatch(request, *args, **kwargs)


def deleteimagen(request):
    if request.method == 'POST':
        try:
            id_imagen = request.POST['imagen_id']
            id_sitio = request.POST['sitio']

            obj_imagen = Imagen.objects.get(id=id_imagen)
            obj_sitio = Sitio.objects.get(id=id_sitio)

            obj_sitio.imagenes.remove(obj_imagen)

            return HttpResponse('Imagen eliminada del sitio exitosamente!')
        except Imagen.DoesNotExist or Sitio.DoesNotExist:
            return HttpResponse('Error! Imagen o Sitio incorrecto')
