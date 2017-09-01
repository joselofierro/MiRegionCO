from django.db import models
# Create your models here.
from apps.noticia.models import Noticia
from apps.sitio.models import Sitio
from apps.usuario.models import Usuario


class VisualizarNoticia(models.Model):
    noticia = models.ForeignKey(Noticia)
    usuario = models.ForeignKey(Usuario, blank=True, null=True)
    fecha = models.DateField(auto_now_add=True, blank=False)
    hora = models.TimeField(auto_now_add=True, blank=False)
    dispositivo = models.IntegerField(blank=False, null=False)


class CompartirNoticia(models.Model):
    noticia = models.ForeignKey(Noticia)
    usuario = models.ForeignKey(Usuario, blank=True, null=True)
    fecha = models.DateField(auto_now_add=True, blank=False)
    hora = models.TimeField(auto_now_add=True, blank=False)
    dispositivo = models.IntegerField(blank=False, null=False)


class GuardarNoticia(models.Model):
    noticia = models.ForeignKey(Noticia)
    usuario = models.ForeignKey(Usuario, blank=True, null=True)
    fecha = models.DateField(auto_now_add=True, blank=False)
    hora = models.TimeField(auto_now_add=True, blank=False)
    dispositivo = models.IntegerField(blank=False, null=False)


class VisitarSitio(models.Model):
    usuario = models.ForeignKey(Usuario, blank=True, null=True)
    sitio = models.ForeignKey(Sitio)
    fecha = models.DateField(auto_now_add=True, blank=False)
    hora = models.TimeField(auto_now_add=True, blank=False)
    dispositivo = models.IntegerField(blank=False, null=False)


class LlamarSitio(models.Model):
    usuario = models.ForeignKey(Usuario, blank=True, null=True)
    sitio = models.ForeignKey(Sitio)
    fecha = models.DateField(auto_now_add=True, blank=False)
    hora = models.TimeField(auto_now_add=True, blank=False)
    dispositivo = models.IntegerField(blank=False, null=False)


class FacebookSitio(models.Model):
    usuario = models.ForeignKey(Usuario, blank=True, null=True)
    sitio = models.ForeignKey(Sitio)
    fecha = models.DateField(auto_now_add=True, blank=False)
    hora = models.TimeField(auto_now_add=True, blank=False)
    dispositivo = models.IntegerField(blank=False, null=False)


class InstagramSitio(models.Model):
    usuario = models.ForeignKey(Usuario, blank=True, null=True)
    sitio = models.ForeignKey(Sitio)
    fecha = models.DateField(auto_now_add=True, blank=False)
    hora = models.TimeField(auto_now_add=True, blank=False)
    dispositivo = models.IntegerField(blank=False, null=False)


class Ingreso(models.Model):
    usuario = models.ForeignKey(Usuario, blank=True, null=True)
    fecha = models.DateField(auto_now_add=True, blank=False)
    hora = models.TimeField(auto_now_add=True, blank=False)
    dispositivo = models.IntegerField(blank=False, null=False)


class IngresoLogin(models.Model):
    usuario = models.ForeignKey(Usuario, blank=True, null=True)
    fecha = models.DateField(auto_now_add=True, blank=False)
    hora = models.TimeField(auto_now_add=True, blank=False)
    dispositivo = models.IntegerField(blank=False, null=False)
