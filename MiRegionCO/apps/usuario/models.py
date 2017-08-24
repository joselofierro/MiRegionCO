
from django.db import models


# Create your models here.
from apps.noticia.models import Noticia
from apps.sitio.models import Sitio


class Usuario(models.Model):
    idFacebook = models.CharField(blank=False, null=False, unique=True, max_length=150)
    primerNombre = models.CharField(max_length=30, blank=False, null=False)
    segundoNombre = models.CharField(max_length=30, blank=False, null=False)
    nombreCompleto = models.CharField(max_length=50, blank=False, null=False)
    telefono = models.BigIntegerField(blank=True, null=False, default=0)
    correo = models.EmailField(unique=True, blank=False, null=False)
    foto = models.TextField(blank=False, null=False)
    noticias = models.ManyToManyField(Noticia, blank=True )
    sitios = models.ManyToManyField(Sitio, blank=True)

    def __str__(self):
        return self.nombreCompleto


