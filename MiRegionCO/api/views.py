from threading import Thread
from django.contrib.auth.hashers import check_password
from django.core.mail import send_mail
from django.db.models import Count
from django.db.models.functions import Concat
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from fcm_django.models import FCMDevice
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import *
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from MiRegionCO import settings
from api.serializers import *
from apps.activacion_youtuber.models import Youtuber
from apps.categoria.models import Categoria
from apps.categoria_mapa.models import CategoriaMapa
from apps.noticia.models import Noticia
from apps.sitio.models import Sitio
from apps.usuario.models import Usuario
from apps.ventas.detalle.models import Detalle
from django.db.models import Count, Value

# API CREAR USUARIO POST
from apps.ventas.subcategoria_producto.models import Subcategoria


class CrearUsuarioAPI(CreateAPIView):
    # serializamos el modelo Usuario
    serializer_class = UsuarioCrearSerializer

    def get_queryset(self):
        return Usuario.objects.all()


# vista para listar usuario por id de facebook
class ObtenerUsuarioAPI(APIView):
    def get(self, request, id_facebook):
        try:
            usuario = Usuario.objects.get(idFacebook=id_facebook)
            serializer_usuario = UsuarioSerializer(usuario)
            return Response(serializer_usuario.data, status=status.HTTP_200_OK)
        except Usuario.DoesNotExist:
            return Response({'data': 'Usuario no existe'}, status=status.HTTP_404_NOT_FOUND)


# POST DE NOTICIAS
class NoticiasAPI(CreateAPIView):
    serializer_class = NoticiasSerializerPOST


# APIS DE ESTADISTICA
class ViewsNews(CreateAPIView):
    serializer_class = ViewsNewsSerializer


class SharedNews(CreateAPIView):
    serializer_class = SharedNewsSerializer


class SaveNews(CreateAPIView):
    serializer_class = SaveNewsSerializer


class VisitPlace(CreateAPIView):
    serializer_class = VisitPlaceSerializer


class CallPlace(CreateAPIView):
    serializer_class = CallPlaceSerializer


class Login(CreateAPIView):
    serializer_class = LoginSerializer


class InstagramAPI(CreateAPIView):
    serializer_class = InstagramSerializer


class FacebookAPI(CreateAPIView):
    serializer_class = FacebookSerializer


class LoginUserAPI(CreateAPIView):
    serializer_class = IngresoLoginSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000


@method_decorator(cache_page(None, cache=settings.CACHE_API_NOTICIAS), name='dispatch')
class NewsFeed(ListAPIView):
    serializer_class = NoticiaSerializer

    # pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        print('Aun no se ha cacheado')
        return Noticia.objects.filter(visible=True).order_by('-fecha', '-hora')


@method_decorator(cache_page(None, cache=settings.CACHE_API_NOTICIAS2), name='dispatch')
class NewsFeed2(ListAPIView):
    serializer_class = NoticiaSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        print('Aun no se ha cacheado')
        return Noticia.objects.filter(visible=True).order_by('-fecha', '-hora')


@method_decorator(cache_page(None, cache=settings.CACHE_API_NOTICIAS_DESTACADAS), name='dispatch')
class NoticiasDestacadasAPI(ListAPIView):
    serializer_class = NoticiaSerializer

    def get_queryset(self):
        # devuelva las noticias con destacado =  True
        print('Aun no se ha cacheado')
        return Noticia.objects.filter(destacada=True, visible=True).order_by('fecha', 'hora')


# Mostrar las noticias destacadas por categoria
@method_decorator(cache_page(None, cache=settings.CACHE_API_NOTICIAS_DESTACADAS_CATEGORIA), name='dispatch')
class NoticiasDestacadasCategoriaAPI(ListAPIView):
    serializer_class = NoticiaSerializer

    def get_queryset(self):
        # devuelva las noticias con destacado =  True
        print('Aun no se ha cacheado')
        return Noticia.objects.filter(destacada=True, visible=True, categoria__id=self.kwargs['id_categoria']).order_by(
            'fecha', 'hora')


@method_decorator(cache_page(None, cache=settings.CACHE_API_CATEGORIA_NOTICIAS), name='dispatch')
class CategoriaNoticiasAPI(ListAPIView):
    serializer_class = CategoriaNoticiasSerializer

    def get_queryset(self):
        print('Aun no se ha cacheado')
        return Categoria.objects.filter(visibleApp=True).order_by('orden')


# 2 maneras de obtener parametros de url con clases basadas en vistas
# devolver las noticias asociadas a la categoria x id
@method_decorator(cache_page(None, cache=settings.CACHE_API_NOTICIASXCATEGORIA), name='dispatch')
class NoticiasCategoriaListId(ListAPIView):
    serializer_class = NoticiaSerializer

    def get_queryset(self):
        print('Aun no se ha cacheado')
        return Noticia.objects.filter(categoria__id=self.kwargs['id_categoria'], visible=True).order_by('-fecha',
                                                                                                        '-hora')


@method_decorator(cache_page(None, cache=settings.CACHE_API_NOTICIASXCATEGORIA2), name='dispatch')
class NoticiasCategoriaListId2(ListAPIView):
    serializer_class = NoticiaSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        print('Aun no se ha cacheado')
        return Noticia.objects.filter(categoria__id=self.kwargs['id_categoria'], visible=True).order_by('-fecha',
                                                                                                        '-hora')


@method_decorator(cache_page(None, cache=settings.CACHE_API_SITIOS), name='dispatch')
class SitiosList(ListAPIView):
    serializer_class = SitioSerializer

    def get_queryset(self):
        print('Aun no se ha cacheado')
        return Sitio.objects.all().order_by('nombre')


@method_decorator(cache_page(None, cache=settings.CACHE_API_CATEGORIA_MAPA), name='dispatch')
class MapaListAPI(ListAPIView):
    serializer_class = CategoriaSitioSerializer

    def get_queryset(self):
        print('Aun no se ha cacheado')
        return CategoriaMapa.objects.order_by('nombre')


@cache_page(None, cache=settings.CACHE_API_SITIOSXSUBCATEGORIA)
@api_view(['GET'])
def SitiosXSubcategoria(request, id_subcategoria):
    if request.method == 'GET':
        print("sitios por categoria no cacheados")
        sitios = Sitio.objects.filter(subcategoria=id_subcategoria).values('nombre', 'latitud', 'longitud',
                                                                           'descripcion', 'horario',
                                                                           'telefono', 'direccion').annotate(
            marcador=Concat(Value(settings.MEDIA_URL), 'subcategoria__categoriamapa__icono_marcador'),
            logo_e=Concat(Value(settings.MEDIA_URL), 'logo')).order_by(
            'nombre')
        return Response(sitios, status=status.HTTP_200_OK)


# Se hace el cambio para que solo aparezcan las categorias que tengan subcategorias y sus subcategorias tengan sitios
"""@cache_page(None, cache=settings.CACHE_API_CATEGORIA_MAPA)
@api_view(['GET'])
def MapaListAPI(request):
    if request.method == "GET":
        print("Mapa_Categoria no cacheado")
        list_dict_categorias = []
        # Consultamos las categorias
        categorias = CategoriaMapa.objects.all().order_by('nombre')

        # Recorremos las categorias para consultar las subcategorias
        for categoria in categorias:
            dict_categoria = OrderedDict()
            dict_categoria['id'] = categoria.id
            dict_categoria['nombre'] = categoria.nombre
            dict_categoria['imagen'] = categoria.imagen.url
            dict_categoria['icono_marcador'] = categoria.icono_marcador.url
            dict_categoria['icono'] = categoria.icono.url

            list_dict_subcategoria = []
            for subcategoria in categoria.subcategoria_mapa.all():
                dict_subcategoria = OrderedDict()
                dict_subcategoria['nombre'] = subcategoria.nombre

                list_dict_sitios = []
                # Consultamos los sitios que tiene esta subcategoria
                sitios = Sitio.objects.filter(subcategoria=subcategoria.id).order_by('nombre')
                if sitios:
                    for sitio in sitios:
                        dict_sitio = OrderedDict()
                        dict_sitio['id'] = sitio.id
                        dict_sitio['nombre'] = sitio.nombre
                        dict_sitio['titulo'] = sitio.titulo
                        dict_sitio['descripcion'] = sitio.descripcion
                        dict_sitio['logo'] = sitio.logo.url
                        dict_sitio['horario'] = sitio.horario
                        dict_sitio['direccion'] = sitio.direccion
                        dict_sitio['instagram'] = sitio.instagram
                        dict_sitio['facebook'] = sitio.facebook
                        list_dict_imagenes = []
                        for imagen in sitio.imagenes.all():
                            dict_imagen = OrderedDict()
                            dict_imagen['imagen'] = imagen.imagen.url
                            list_dict_imagenes.append(dict_imagen)

                        dict_sitio['imagenes'] = list_dict_imagenes
                        dict_sitio['telefono'] = sitio.telefono
                        dict_sitio['latitud'] = sitio.latitud
                        dict_sitio['longitud'] = sitio.longitud

                        # Agregamos el sitio al listato de dict
                        list_dict_sitios.append(dict_sitio)

                    dict_subcategoria['sitio'] = list_dict_sitios

                    # Agregamos la subcategoria al listado de dict de subcategorias
                    list_dict_subcategoria.append(dict_subcategoria)

            # Agregamos el listado de subcategorias a la categoria
            dict_categoria['subcategoria_mapa'] = list_dict_subcategoria

            # Si hay subcategorias agregamos la categoria al list
            if list_dict_subcategoria:
                list_dict_categorias.append(dict_categoria)

        return Response(list_dict_categorias, status=status.HTTP_200_OK)

    else:
        return Response({'data': 'error'}, status=status.HTTP_400_BAD_REQUEST)"""


@method_decorator(cache_page(None, cache=settings.CACHE_API_USUARIOS), name='dispatch')
class UsuariosAPI(ListAPIView):
    serializer_class = UsuarioSerializer

    def get_queryset(self):
        print('Aun no se ha cacheado')
        return Usuario.objects.all()


# agregar la noticia al usuario
@api_view(['post'])
def noticiausuario(request):
    try:
        # id del usuario y noticia
        usuario = request.data['usuario']
        noticia = request.data['noticia']

        # obtener objeto usuario y noticia por idfacebook y id
        obj_usuario = Usuario.objects.get(id=usuario)
        obj_noticia = Noticia.objects.get(id=noticia)

        obj_usuario.noticias.add(obj_noticia)

        return Response({'data': True}, status=status.HTTP_200_OK)
    except Exception as ex:

        return Response({'data': ex}, status=status.HTTP_400_BAD_REQUEST)


# eliminar la noticia del usuario
@api_view(['delete'])
def eliminarnoticia(request, id_facebook, id_noticia):
    try:

        obj_usuario = Usuario.objects.get(idFacebook=id_facebook)
        obj_noticia = Noticia.objects.get(id=id_noticia)

        obj_usuario.noticias.remove(obj_noticia)

        return Response({'data': True}, status=status.HTTP_200_OK)
    except Exception as ex:

        return Response({'data': ex}, status=status.HTTP_400_BAD_REQUEST)


# Crear Sitios
@api_view(['POST'])
def CrearSitio(request):
    if request.method == 'POST':
        serializer = CrearSitioSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': 'OK'}, status=status.HTTP_200_OK)
        else:
            return Response({'data': 'False', 'Errores': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


# agregar el sitio al usuario
@api_view(['post'])
def sitiousuario(request):
    try:
        usuario = request.data['usuario']
        sitio = request.data['sitio']

        obj_usuario = Usuario.objects.get(id=usuario)
        obj_sitio = Sitio.objects.get(id=sitio)

        obj_usuario.sitios.add(obj_sitio)

        return Response({'data': True}, status=status.HTTP_200_OK)
    except Exception as ex:
        return Response({'data': ex}, status=status.HTTP_400_BAD_REQUEST)


# eliminar el sitio del usuario
@api_view(['delete'])
def eliminarsitio(request, id_facebook, id_sitio):
    try:

        obj_usuario = Usuario.objects.get(idFacebook=id_facebook)

        obj_sitio = Sitio.objects.get(id=id_sitio)

        obj_usuario.sitios.remove(obj_sitio)

        return Response({'data': True}, status=status.HTTP_200_OK)

    except Exception as ex:
        return Response({'data': ex}, status=status.HTTP_400_BAD_REQUEST)


# actualizar telefono del usuario
@api_view(['put'])
def actualizartelefono(request):
    try:

        # obtenemos el id de usuario y telefono
        usuario = request.data['usuario']
        telefono = request.data['telefono']

        obj_usuario = Usuario.objects.get(id=usuario)

        obj_usuario.telefono = telefono

        obj_usuario.save()

        return Response({'data': True}, status=status.HTTP_200_OK)

    except Exception as ex:
        return Response({'data': ex}, status=status.HTTP_400_BAD_REQUEST)


# APIS DE MIREGION VENTAS
@api_view(['GET'])
def login(request, p_correo, p_pass):
    if request.method == 'GET':
        try:
            vendedor = Vendedor.objects.get(correo=p_correo)
            if check_password(p_pass, vendedor.contrasena):
                return Response({'data': True, 'user_id': vendedor.id}, status=status.HTTP_200_OK)
            else:
                return Response({'data': False}, status=status.HTTP_200_OK)

        except Vendedor.DoesNotExist:
            return Response({'data': False}, status=status.HTTP_200_OK)


# crear json del portafolio
@method_decorator(cache_page(None, cache=settings.CACHE_API_PORTAFOLIO), name='dispatch')
class PortafolioAPI(APIView):
    def get(self, request, format=None):

        categorias = Categoria.objects.all().order_by('id')
        lista_categoria = []

        # recorremos las categorias
        for categoria in categorias:
            json_categoria = OrderedDict()
            json_categoria['id'] = categoria.id
            json_categoria['nombre'] = categoria.nombre
            json_categoria['medida'] = categoria.medida

            # obtenemos las subcategorias
            subcategorias = Subcategoria.objects.all().order_by('nombre')
            listado_subcategoria = []

            # recorremos la subcategoria para encontrar productos relacionados a la categoria y subcategoria
            for subcategoria in subcategorias:
                json_subcategoria = OrderedDict()
                json_subcategoria['id'] = subcategoria.id
                json_subcategoria['nombre'] = subcategoria.nombre

                productos_asociados = Detalle.objects.filter(categoria=categoria, subcategoria=subcategoria).order_by(
                    'producto__tiempo')

                # si hay productos asociados los buscamos
                if productos_asociados:
                    listado_productos = []

                    # recorremos los productos asociados consultando los productos
                    for producto in productos_asociados:
                        json_producto = OrderedDict()
                        json_producto['id'] = producto.producto.id
                        json_producto['tiempo'] = producto.producto.tiempo
                        json_producto['medida'] = producto.producto.medida
                        json_producto['precio'] = producto.producto.precio

                        listado_productos.append(json_producto)

                    # agregamos el listado de productos al json de subcategoria
                    json_subcategoria['productos'] = listado_productos
                    # agregamos el json de subcategorias a la lista de subcategorias
                    listado_subcategoria.append(json_subcategoria)
            # agregamos el listado de subcategoria al json de categoria
            json_categoria['subcategorias'] = listado_subcategoria
            # agregamos el json de categoria a la lista de categoria
            lista_categoria.append(json_categoria)

        if lista_categoria:
            return Response(lista_categoria, status=status.HTTP_201_CREATED)
        else:
            return Response({'data': 'No hay datos'}, status=status.HTTP_400_BAD_REQUEST)


# POST DE COTIZACION  y almacenar la cotizacion
class CrearCotizacionAPI(CreateAPIView):
    serializer_class = CotizacionSerializer

    def post(self, request, *args, **kwargs):
        # obtenemos el cliente serializado
        serializer_cliente = ClienteSerializer(data=request.data['cliente'])
        if serializer_cliente.is_valid():
            try:
                # obtenemos el nombre de la empresa y verificamos si ya existe
                cliente = Cliente.objects.get(nombre_empresa=request.data['cliente']['nombre_empresa'])
                if CrearCotizacion(cliente.id, request):
                    return Response({'data': True}, status=status.HTTP_201_CREATED)
                else:
                    return Response({'data': False}, status=status.HTTP_400_BAD_REQUEST)
            # si el cliente no existe creelo
            except Cliente.DoesNotExist:
                serializer_cliente.save()
                # ¿porque ultimo cliente? pq es el cliente reciente en ser creado
                ultimo_cliente = Cliente.objects.last()
                if CrearCotizacion(ultimo_cliente.id, request):
                    return Response({'data': True}, status=status.HTTP_201_CREATED)
                else:
                    return Response({'data': False}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer_cliente.errors, status=status.HTTP_400_BAD_REQUEST)


def CrearCotizacion(id_cliente, request):
    request.data['cotizacion']['cliente'] = id_cliente
    serializer_cotizacion = CotizacionSerializer(data=request.data['cotizacion'])

    lista_productos = []
    for detalle in request.data['cotizacion']['productos']:
        detalle_producto = Detalle.objects.get(producto_id=detalle['producto'],
                                               categoria_id=detalle['categoria'],
                                               subcategoria_id=detalle['subcategoria'])
        lista_productos.append(detalle_producto.id)

    if lista_productos:
        request.data['cotizacion']['productos'] = lista_productos
        serializer_cotizacion = CotizacionSerializer(data=request.data['cotizacion'])

    if serializer_cotizacion.is_valid():
        serializer_cotizacion.save()
        EnviarEmail(request)
        return True
    else:
        print(serializer_cotizacion.errors)
        return False


# JSON DE COTIZACIONES
@cache_page(None, cache=settings.CACHE_API_COTIZACIONES)
@api_view(['GET'])
def ListCotizaciones(request, id_vendedor):
    if request.method == 'GET':
        cotizaciones = Cotizacion.objects.filter(vendedor_id=id_vendedor)
        clientes = []

        for cotizacion in cotizaciones:
            clientes.append(cotizacion.cliente)

        lista_cliente = []
        for cliente in clientes:
            json_cliente = OrderedDict()
            json_cliente['nombre_empresa'] = cliente.nombre_empresa
            json_cliente['direccion'] = cliente.direccion
            json_cliente['nombre_contacto'] = cliente.nombre_contacto
            json_cliente['telefono'] = cliente.telefono
            json_cliente['celular'] = cliente.celular
            json_cliente['correo'] = cliente.correo

            cotizaciones_cliente = Cotizacion.objects.filter(cliente=cliente)
            # cotizacion relacionada al cliente (recorremos la cotizacion para ver si hay cotizacion relacionada al
            # cliente)
            if cotizaciones_cliente:
                lista_cotizaciones = []
                for cotizacion in cotizaciones_cliente:
                    json_cotizacion = OrderedDict()
                    json_cotizacion['fecha'] = cotizacion.fecha
                    json_cotizacion['hora'] = cotizacion.hora
                    json_cotizacion['descripcion'] = cotizacion.descripcion

                    cotizacion_producto = cotizacion.productos.all()
                    listado_productos = []

                    for productoDetalle in cotizacion_producto:
                        json_producto = OrderedDict()
                        json_producto['tiempo'] = productoDetalle.producto.tiempo
                        json_producto['precio'] = productoDetalle.producto.precio
                        json_producto['medida'] = productoDetalle.producto.medida
                        json_producto['categoria'] = productoDetalle.categoria.nombre
                        json_producto['subcategoria'] = productoDetalle.subcategoria.nombre

                        listado_productos.append(json_producto)

                    json_cotizacion['producto_detalle'] = listado_productos
                    lista_cotizaciones.append(json_cotizacion)

                json_cliente['cotizaciones'] = lista_cotizaciones

            lista_cliente.append(json_cliente)

        if lista_cliente:
            return Response(lista_cliente, status=status.HTTP_200_OK)
        else:
            return Response({'data': False}, status.HTTP_400_BAD_REQUEST)


# Decorador
def postpone(function):
    def decorator(*args, **kwargs):
        t = Thread(target=function, args=args, kwargs=kwargs)
        t.daemon = True
        t.start()

    return decorator


# Saco del JSON LOS DATOS A ENVIAR
@postpone
def EnviarEmail(request):
    try:
        list_detalle = []

        for producto_detalle in request.data['cotizacion']['productos']:
            detalle = Detalle.objects.get(id=producto_detalle)

            detalle.producto.precio = '{0:,}'.format(detalle.producto.precio)
            list_detalle.append(detalle)

        cotizacion_obj = Cotizacion.objects.last()

        msg = render_to_string('ventas/cotizacion/cotizacion_email.html', {'cliente': request.data['cliente'],
                                                                           'cotizacion_detalle': list_detalle,
                                                                           'cotizacion': cotizacion_obj,
                                                                           })
        para = str(request.data['cliente']['correo'])
        send_mail(
            'Cotización Mi Region.co',
            'mensaje',
            'jfierro985@gmail.com',
            [para],
            html_message=msg
        )
    except Exception as ex:
        print(ex)


@api_view(['POST'])
def FCM_CREATE(request):
    # si el usuario es nulo
    if request.data['user'] is None:
        # creamos la instancia del fcm
        fcm_device_new = FCMDevice(user=None, registration_id=request.data['registration_id'],
                                   type=request.data['type'])
        # guardamos la instancia
        fcm_device_new.save()
        return Response(data={'data:' 'FCM CREADO🙏'}, status=status.HTTP_200_OK)

    else:
        # si el usuario existe
        if Usuario.objects.filter(id=request.data['user']).exists():
            # obtenemos el usuario que viene del json
            fcm_user = Usuario.objects.get(id=request.data['user'])
            # si existe fcm_device con ese user y ese type
            if FCMDevice.objects.filter(user=fcm_user, type=request.data['type']).exists():
                # obtenemos el fcm_device
                fcm_obj = FCMDevice.objects.get(user=fcm_user, type=request.data['type'])
                # si el token es igual
                if fcm_obj.registration_id == request.data['registration_id']:
                    fcm_obj.active = True
                    fcm_obj.save()
                    return Response({'data': 'ya existe este token'}, status=status.HTTP_200_OK)
                else:
                    # actualizamos el token
                    fcm_obj.registration_id = request.data['registration_id']
                    fcm_obj.active = True
                    fcm_obj.save()
                    return Response({'data': 'Token actualizado'}, status=status.HTTP_200_OK)
            else:
                fcm_device_new = FCMDevice(user=fcm_user, registration_id=request.data['registration_id'],
                                           type=request.data['type'])
                fcm_device_new.save()
                return Response(data={'data': 'FCM CREADO 👏'})
        # si el usuario no existe
        else:
            fcm_device_new = FCMDevice(user=None, registration_id=request.data['registration_id'],
                                       type=request.data['type'])
            fcm_device_new.save()
            return Response(data={'data:' 'FCM CREADO👍'}, status=status.HTTP_200_OK)


@api_view(['GET'])
def ListadoConcursantes(request):
    if request.method == 'GET':
        concursantes = Youtuber.objects.filter(visible=True).values('codigo', 'foto', 'nombre').annotate(
            votos=Count('votaciones__codigo')).order_by('-votos', 'nombre')

        return Response(concursantes, status=status.HTTP_200_OK)


class VotarYoutuber(CreateAPIView):
    serializer_class = VotacionSerializer

    def post(self, request, *args, **kwargs):
        votar = False
        if 'accessToken' in request.data:
            if votar:
                if request.data['accessToken'] == 'ba517f21210bdf8e9e594f0f28257b020d9c0923' or request.data[
                    'accessToken'] == 'dbc6821f13c30a91738f280456f32513310c8aa4':
                    request.data.pop('accessToken')
                    obj_votacion = VotacionSerializer(data=request.data)
                    if obj_votacion.is_valid():
                        obj_votacion.save()
                        return Response({'data': True}, status=status.HTTP_201_CREATED)
                    else:
                        # Validamos si el usuario existe
                        if Usuario.objects.filter(id=request.data['usuario']).exists():
                            # Validamos si existe el codigo
                            if Youtuber.objects.filter(codigo=request.data['codigo']).exists():
                                # Validamos si usuario ya votó
                                if Votaciones.objects.filter(usuario__id=request.data['usuario']).exists():
                                    votacion = Votaciones.objects.filter(usuario__id=request.data['usuario'])
                                    return Response(
                                        {'data': 'Este usuario ya votó por ' + votacion.first().codigo.nombre},
                                        status=status.HTTP_400_BAD_REQUEST)

                                # Validamos si el dispositivo ya votó
                                if Votaciones.objects.filter(dispositivo_id=request.data['dispositivo_id']).exists():
                                    votacion = Votaciones.objects.filter(dispositivo_id=request.data['dispositivo_id'])
                                    return Response(
                                        {'data': 'Este dispositivo ya votó ' + votacion.first().codigo.nombre},
                                        status=status.HTTP_400_BAD_REQUEST)
                            else:
                                return Response({'data': 'No existe participante con el código ingresado'},
                                                status=status.HTTP_400_BAD_REQUEST)
                        else:
                            return Response({'data': 'El usuario que intenta votar no existe'},
                                            status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({'Error': 'No estas autorizado para hacer este POST 😜'},
                                    status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'data': 'Las votaciones han sido cerradas 🙂'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'Error': 'No estas autorizado para hacer este POST 😜'},
                            status=status.HTTP_400_BAD_REQUEST)


class noticiaByText(ListAPIView):
    serializer_class = NoticiaSerializer

    def get_queryset(self):
        return Noticia.objects.filter(titular__icontains=self.kwargs['p_texto']).order_by('-fecha', '-hora')
