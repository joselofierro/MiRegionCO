from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count, Value
from django.db.models.functions import Concat
from django.shortcuts import render

from MiRegionCO import settings
from apps.categoria_mapa.models import CategoriaMapa
from apps.estadistica.models import VisitarSitio
from apps.noticia.models import *
# Create your views here.
from apps.sitio.models import Sitio


def index(request):
    if request.method == 'GET':
        # Consultar las noticias destacadas
        noticias_destacadas = Noticia.objects.filter(visible=True, destacada=True).order_by('-fecha', '-hora')

        # Consultar todas las noticias en order cronológico descendente
        noticias_list = Noticia.objects.filter(visible=True).order_by('-fecha', '-hora')

        paginator = Paginator(noticias_list, 10)  # Mostramos paginas de 10 imagenes
        page = request.GET.get('page')

        try:
            # Si hay noticias
            noticias = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            noticias = paginator.page(1)
        except EmptyPage:
            # Si la pagina esta fuera del rango, entrega la ultima pagina
            noticias = paginator.page(paginator.num_pages)

        return render(request, 'pagina_web/home/index.html',
                      {'noticias_destacadas': noticias_destacadas, 'noticias': noticias})


def noticias_categoria(request, p_categoria_id):
    if request.method == 'GET':
        try:
            # Obtengo la categoria
            categoria = Categoria.objects.get(id=p_categoria_id)

            # Consultar las noticias destacadas por categoria
            noticias_destacadas = Noticia.objects.filter(visible=True, destacada=True,
                                                         categoria=p_categoria_id).order_by('-fecha', '-hora')

            # Consultar todas las noticias en order cronológico descendente
            noticias_list = Noticia.objects.filter(visible=True, categoria=p_categoria_id).order_by('-fecha', '-hora')

            paginator = Paginator(noticias_list, 10)  # Mostramos paginas de 10 imagenes
            page = request.GET.get('page')

            try:
                # Si hay noticias
                noticias = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                noticias = paginator.page(1)
            except EmptyPage:
                # Si la pagina esta fuera del rango, entrega la ultima pagina
                noticias = paginator.page(paginator.num_pages)

            return render(request, 'pagina_web/home/index_categoria.html',
                          {'noticias_destacadas': noticias_destacadas, 'noticias': noticias, 'categoria': categoria})
        except Categoria.DoesNotExist:
            return render(request, 'pagina_web/404.html', {})


def noticia_id(request, p_id):
    if request.method == 'GET':
        # Consultamos la noticia por id
        try:
            # Cargar las categorias existentes
            categorias = Categoria.objects.all()

            # Consultar las noticias destacadas
            noticias_destacadas = Noticia.objects.filter(visible=True, destacada=True).order_by('-fecha', '-hora')

            noticia = Noticia.objects.get(id=p_id)

            # Creamos las metas
            dict_meta = '<meta property="og:title" content="' + noticia.titular + '">' + \
                        '<meta property="og:url" content="' + request.build_absolute_uri() + '">' + \
                        '<meta property="og:description" content="' + noticia.lead + '">' + \
                        '<meta property="og:image" content="' + noticia.imagenes.first().imagen.url + '">' + \
                        '<meta property="og:image:type" content="image/jpeg">'

            list_tags = ""

            for tag in noticia.tag.all():
                list_tags += tag.nombre + ","

            list_tags = list_tags[:-1]

            print(list_tags)

            return render(request, 'pagina_web/noticia/noticia_id.html',
                          {'noticia': noticia, 'categorias': categorias, 'noticias_destacadas': noticias_destacadas,
                           'meta': dict_meta, 'full_url': request.build_absolute_uri(), 'tags': list_tags})

        except Noticia.DoesNotExist:
            return render(request, 'pagina_web/404.html', {})


def mapa(request):
    if request.method == 'GET':
        # Cargar las categorias existentes
        categorias = Categoria.objects.all()

        # Obtener todos los sitios
        sitios = Sitio.objects.all().values('nombre', 'latitud', 'longitud', 'descripcion', 'horario',
                                            'telefono', 'direccion').annotate(
            marcador=Concat(Value(settings.MEDIA_URL), 'subcategoria__categoriamapa__icono_marcador'),
            logo_e=Concat(Value(settings.MEDIA_URL), 'logo')).order_by(
            'nombre')

        sitios_visitados = VisitarSitio.objects.all().values('sitio__id', 'sitio__nombre').annotate(
            sitio_count=Count('sitio'), sitio__logo=Concat(Value(settings.MEDIA_URL), 'sitio__logo')).order_by(
            '-sitio_count')[:10]

        categorias_Mapa = CategoriaMapa.objects.all().order_by('nombre')

        return render(request, 'pagina_web/mapa/mapa.html',
                      {'categorias': categorias, 'sitios': sitios, 'sitios_recomendados': sitios_visitados,
                       'categorias_mapa': categorias_Mapa},
                      content_type='text/html')
