from apps.activacion_youtuber.models import Votaciones
from apps.subcategoria_mapa.models import SubcategoriaMapa
from apps.ventas.cliente.models import Cliente
from apps.ventas.cotizacion.models import Cotizacion
from apps.ventas.producto.models import Producto
from django.contrib.auth.models import User
from rest_framework.serializers import *

from apps.categoria.models import Categoria
from apps.categoria_mapa.models import CategoriaMapa
from apps.estadistica.models import *
from apps.imagen.models import Imagen
from apps.noticia.models import Noticia
from apps.sitio.models import Sitio
from apps.tag.models import Tag
from apps.usuario.models import Usuario
from apps.ventas.vendedor.models import Vendedor


class AutorSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class ImagenSerializer(ModelSerializer):
    class Meta:
        model = Imagen
        fields = ('imagen',)


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ('nombre',)


class NoticiaSerializer(ModelSerializer):
    # consultas
    autor = AutorSerializer(many=False)
    imagenes = ImagenSerializer(many=True)
    tag = TagSerializer(many=True)

    class Meta:
        model = Noticia
        fields = (
            'id', 'fecha', 'hora', 'titular', 'lead', 'texto', 'imagen_video', 'url', 'video', 'duracion', 'imagenes',
            'autor', 'tag')


class NoticiasSerializerPOST(ModelSerializer):
    class Meta:
        model = Noticia
        fields = ('id', 'fecha', 'hora', 'titular', 'lead', 'texto', 'video', 'imagenes', 'tag')


class CategoriaNoticiasSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'nombre', 'color')


class SitioSerializer(ModelSerializer):
    imagenes = ImagenSerializer(many=True)

    class Meta:
        model = Sitio
        fields = (
            'id', 'nombre', 'titulo', 'descripcion', 'logo', 'horario', 'direccion', 'instagram', 'facebook',
            'imagenes', 'telefono', 'latitud', 'longitud')


class CrearSitioSerializer(ModelSerializer):
    class Meta:
        model = Sitio
        fields = '__all__'


class SubcategoriaSitioSerializer(ModelSerializer):
    sitio = SitioSerializer(many=True)

    class Meta:
        model = SubcategoriaMapa
        fields = ('nombre', 'sitio')


class CategoriaSitioSerializer(ModelSerializer):
    subcategoria_mapa = SubcategoriaSitioSerializer(many=True)

    class Meta:
        model = CategoriaMapa
        fields = ('id', 'nombre', 'imagen', 'subcategoria_mapa', 'icono_marcador', 'icono')


class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'


class UsuarioCrearSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = (
            'id',
            'idFacebook',
            'primerNombre',
            'segundoNombre',
            'nombreCompleto',
            'correo',
            'foto',)


class ViewsNewsSerializer(ModelSerializer):
    class Meta:
        model = VisualizarNoticia
        fields = ('noticia', 'usuario', 'dispositivo')


class SharedNewsSerializer(ModelSerializer):
    class Meta:
        model = CompartirNoticia
        fields = ('noticia', 'usuario', 'dispositivo')


class SaveNewsSerializer(ModelSerializer):
    class Meta:
        model = GuardarNoticia
        fields = ('noticia', 'usuario', 'dispositivo')


class VisitPlaceSerializer(ModelSerializer):
    class Meta:
        model = VisitarSitio
        fields = ('usuario', 'sitio', 'dispositivo')


class CallPlaceSerializer(ModelSerializer):
    class Meta:
        model = LlamarSitio
        fields = ('usuario', 'sitio', 'dispositivo')


class LoginSerializer(ModelSerializer):
    class Meta:
        model = Ingreso
        fields = ('usuario', 'dispositivo')


class VisitIndexSerializer(ModelSerializer):
    class Meta:
        model = VisitIndex
        fields = ('isdesktop',)


class VisitNewsSerializer(ModelSerializer):
    class Meta:
        model = VisitNews
        fields = ('isdesktop', 'noticia')


class ShareFacebookSerializer(ModelSerializer):
    class Meta:
        model = ShareFacebook
        fields = ('isdesktop', 'noticia')


class ShareTwitterSerializer(ModelSerializer):
    class Meta:
        model = ShareTwitter
        fields = ('isdesktop', 'noticia')


class ShareGoogleSerializer(ModelSerializer):
    class Meta:
        model = ShareGoogle
        fields = ('isdesktop', 'noticia')


class VisitMapaSerializer(ModelSerializer):
    class Meta:
        model = VisitMap
        fields = ('isdesktop',)


class MapVisitPlaceSerializer(ModelSerializer):
    class Meta:
        model = VisitPlace
        fields = ('isdesktop', 'sitio')


class SaveNewsSerializer(ModelSerializer):
    class Meta:
        model = SaveNewsSerializer
        fields = ('isdesktop',)


# Serializers de MiregionVentas
class VendedorSerializer(ModelSerializer):
    class Meta:
        model = Vendedor
        fields = '__all__'


class ProductoSerializer(ModelSerializer):
    class Meta:
        model = Producto
        fields = ('tiempo', 'precio', 'medida',)


class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('nombre', 'medida',)


class ClienteSerializer(ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


class CotizacionSerializer(ModelSerializer):
    class Meta:
        model = Cotizacion
        fields = '__all__'


class InstagramSerializer(ModelSerializer):
    class Meta:
        model = InstagramSitio
        fields = ('usuario', 'sitio', 'dispositivo')


class FacebookSerializer(ModelSerializer):
    class Meta:
        model = FacebookSitio
        fields = ('usuario', 'sitio', 'dispositivo')


class IngresoLoginSerializer(ModelSerializer):
    class Meta:
        model = IngresoLogin
        fields = ('dispositivo',)


class VotacionSerializer(ModelSerializer):
    class Meta:
        model = Votaciones
        fields = ('codigo', 'dispositivo_id', 'so', 'usuario')
