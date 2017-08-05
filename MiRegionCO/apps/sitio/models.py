from django.db import models
from apps.categoria_mapa.models import CategoriaMapa
from apps.imagen.models import Imagen


class Sitio(models.Model):
    nombre = models.CharField(max_length=30, blank=False, null=False)
    titulo = models.CharField(max_length=150, blank=False, null=False)
    descripcion = models.TextField(max_length=100, blank=False, null=False)
    logo = models.ImageField(blank=False, null=False)
    horario = models.CharField(max_length=30, blank=False, null=False)
    direccion = models.CharField(max_length=50, blank=False, null=False)
    instagram = models.CharField(blank=True, null=False, max_length=200)
    facebook = models.CharField(blank=True, null=False, max_length=200)
    telefono = models.CharField(max_length=30, blank=False, null=False)
    imagenes = models.ManyToManyField(Imagen)
    categoria = models.ManyToManyField(CategoriaMapa, related_name='categoria_sitio')
    latitud = models.FloatField(max_length=30, blank=False, null=False)
    longitud = models.FloatField(max_length=30, blank=False, null=False)

    def __str__(self):
        return self.nombre
