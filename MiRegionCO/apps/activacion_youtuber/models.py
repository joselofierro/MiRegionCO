import uuid

from django.db import models


# Create your models here.
from apps.usuario.models import Usuario


class Youtuber(models.Model):
    codigo = models.CharField(primary_key=True, default=uuid.uuid4, max_length=25)
    nombre = models.CharField(max_length=100, blank=False, null=False)
    foto = models.URLField(blank=False, null=False)

    def __str__(self):
        return self.nombre


class Votaciones(models.Model):
    codigo = models.ForeignKey(Youtuber, blank=False, null=False)
    dispositivo_id = models.TextField(blank=False, null=False, unique=True)
    so = models.CharField(max_length=1, blank=False, null=False)
    fecha = models.DateField(blank=False, null=True, auto_now_add=True)
    hora = models.TimeField(blank=False, null=True, auto_now_add=True)
    usuario = models.OneToOneField(Usuario)
