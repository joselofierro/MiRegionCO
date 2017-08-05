from threading import Thread

from django.contrib.auth.hashers import check_password
from django.core.mail import send_mail
from django.template.loader import render_to_string
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import *
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import *
from apps.categoria.models import Categoria
from apps.categoria_mapa.models import CategoriaMapa
from apps.noticia.models import Noticia
from apps.sitio.models import Sitio
from apps.usuario.models import Usuario
from apps.ventas.detalle.models import Detalle


# API CREAR USUARIO POST
class CrearUsuarioAPI(CreateAPIView):
    # serializamos el modelo Usuario
    serializer_class = UsuarioCrearSerializer

    def get_queryset(self):
        return Usuario.objects.all()


# vista para obtener usuario por id de facebook
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


class NewsFeed(ListAPIView):
    serializer_class = NoticiaSerializer

    def get_queryset(self):
        return Noticia.objects.all().order_by('fecha', 'hora')


class NoticiasDestacadasAPI(ListAPIView):
    serializer_class = NoticiaSerializer

    def get_queryset(self):
        # devuelva las noticias con destacado =  True
        return Noticia.objects.filter(destacada=True).order_by('fecha', 'hora')


class CategoriaNoticiasAPI(ListAPIView):
    serializer_class = CategoriaNoticiasSerializer

    def get_queryset(self):
        return Categoria.objects.all()


# 2 maneras de obtener parametros de url con clases basadas en vistas
# devolver las noticias asociadas a la categoria x id
class NoticiasCategoriaListId(ListAPIView):
    serializer_class = NoticiaSerializer

    def get_queryset(self):
        return Noticia.objects.filter(categoria__id=self.kwargs['id_categoria']).order_by('fecha', 'hora')


class SitiosList(ListAPIView):
    serializer_class = SitioSerializer

    def get_queryset(self):
        return Sitio.objects.all().order_by('nombre')


class MapaCategoriaList(ListAPIView):
    serializer_class = SitioSerializer

    def get_queryset(self):
        return Sitio.objects.filter(categoria__id=self.kwargs['id_categoria'])


class CategoriaMapaAPI(ListAPIView):
    serializer_class = CategoriaMapaSerializer

    def get_queryset(self):
        return CategoriaMapa.objects.all()


class UsuariosAPI(ListAPIView):
    serializer_class = UsuarioSerializer

    def get_queryset(self):
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
            if check_password(p_pass, vendedor.contraseña):
                return Response({'data': True, 'user_id': vendedor.id}, status=status.HTTP_200_OK)
            else:
                return Response({'data': False}, status=status.HTTP_200_OK)

        except Vendedor.DoesNotExist:
            return Response({'data': False}, status=status.HTTP_200_OK)


# podemos hacer de dos formas la creacion de la peticion de la clase del api ()
# crear json del portafolio
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


# recibir POST DE COTIZACION  y almacenar la cotizacion
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
