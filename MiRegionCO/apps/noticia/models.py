from django.contrib.auth.models import User
from django.db import models

from apps.categoria.models import Categoria
from apps.imagen.models import Imagen
from apps.tag.models import Tag


class Noticia(models.Model):
    fecha = models.DateField(blank=False)
    hora = models.TimeField(blank=False)
    titular = models.CharField(max_length=150)
    lead = models.CharField(max_length=220)
    texto = models.TextField(blank=False, null=False)
    imagen_video = models.ImageField(blank=True, null=False)
    url = models.URLField(blank=False, null=False)
    video = models.TextField(blank=True, null=False)
    duracion = models.CharField(max_length=150, blank=True)
    imagenes = models.ManyToManyField(Imagen)
    # en caso de necesitar mas campos del User creamos el modelo auto herendado de User
    autor = models.ForeignKey(User)
    tag = models.ManyToManyField(Tag)
    categoria = models.ManyToManyField(Categoria, related_name='categoria')
    destacada = models.BooleanField(default=False, blank=False, null=False)
    visible = models.BooleanField(default=True)
    mobile = models.BooleanField(default=True)
    web = models.BooleanField(default=True)

    def __str__(self):
        return self.titular
