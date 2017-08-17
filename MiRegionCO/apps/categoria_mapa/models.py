from django.db import models

from apps.subcategoria_mapa.models import SubcategoriaMapa


def upload_location(instance, filename):
    filebase, extension = filename.split(".")
    return "%s/%s.%s" % ('ImagenCategoria_mapa', instance.nombre, extension)


class CategoriaMapa(models.Model):
    nombre = models.CharField(max_length=30, blank=False, null=False)
    imagen = models.ImageField(blank=False, null=False, upload_to=upload_location)
    subcategoria_mapa = models.ManyToManyField(SubcategoriaMapa)

    def __str__(self):
        return self.nombre
