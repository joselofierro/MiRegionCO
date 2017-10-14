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
    fecha = models.DateField(auto_now_add=True, blank=False)
    hora = models.TimeField(auto_now_add=True, blank=False)
    dispositivo = models.IntegerField(blank=False, null=False)


# MODELOS DE ESTADISTICA PARA LA WEB #

class VisitIndex(models.Model):
    fecha = models.DateField(auto_now_add=True, blank=False)
    hora = models.TimeField(auto_now_add=True, blank=False)
    usuario = models.ForeignKey(Usuario, blank=True, null=True)
    isdesktop = models.BooleanField(default=True)


class VisitNews(models.Model):
    fecha = models.DateField(auto_now_add=True, blank=False)
    hora = models.TimeField(auto_now_add=True, blank=False)
    usuario = models.ForeignKey(Usuario, blank=True, null=True)
    isdesktop = models.BooleanField(default=True)


class ShareFacebook(models.Model):
    fecha = models.DateField(auto_now_add=True, blank=False)
    hora = models.TimeField(auto_now_add=True, blank=False)
    usuario = models.ForeignKey(Usuario, blank=True, null=True)
    isdesktop = models.BooleanField(default=True)


class ShareTwitter(models.Model):
    fecha = models.DateField(auto_now_add=True, blank=False)
    hora = models.TimeField(auto_now_add=True, blank=False)
    usuario = models.ForeignKey(Usuario, blank=True, null=True)
    isdesktop = models.BooleanField(default=True)


class ShareGoogle(models.Model):
    fecha = models.DateField(auto_now_add=True, blank=False)
    hora = models.TimeField(auto_now_add=True, blank=False)
    usuario = models.ForeignKey(Usuario, blank=True, null=True)
    isdesktop = models.BooleanField(default=True)


class VisitMap(models.Model):
    fecha = models.DateField(auto_now_add=True, blank=False)
    hora = models.TimeField(auto_now_add=True, blank=False)
    usuario = models.ForeignKey(Usuario, blank=True, null=True)
    isdesktop = models.BooleanField(default=True)


class VisitPlace(models.Model):
    fecha = models.DateField(auto_now_add=True, blank=False)
    hora = models.TimeField(auto_now_add=True, blank=False)
    usuario = models.ForeignKey(Usuario, blank=True, null=True)
    isdesktop = models.BooleanField(default=True)


class SaveNews(models.Model):
    fecha = models.DateField(auto_now_add=True, blank=False)
    hora = models.TimeField(auto_now_add=True, blank=False)
    usuario = models.ForeignKey(Usuario, blank=True, null=True)
    isdesktop = models.BooleanField(default=True, null=False)

# END MODELOS ESTADISTICAS PARA LA WEB #
