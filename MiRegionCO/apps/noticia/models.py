from django.contrib.auth.models import User
from django.core import urlresolvers
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify

from apps.categoria.models import Categoria
from apps.imagen.models import Imagen
from apps.tag.models import Tag


class Noticia(models.Model):
    fecha = models.DateField(blank=False)
    hora = models.TimeField(blank=False)
    titular = models.CharField(max_length=150)
    slug = models.SlugField(max_length=200, default='')
    lead = models.CharField(max_length=220)
    texto = models.TextField(blank=False, null=False)
    imagen_video = models.ImageField(blank=True, null=False)
    url = models.URLField(blank=True, null=False)
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
    web = models.BooleanField(default=False)

    def __str__(self):
        return self.titular

    # metodo para crear objeto de noticia
    """def save(self, *args, **kwargs):
        print('save() es llamada')
        return super(Noticia, self).save(*args, **kwargs)
        la señal ocurre cuando se llama al metodo save y si dentro de la señal volvemos a usar save entonces entrar en un loop infinito"""


# señal(post_save) que envia despues de haber creado la instancia de la noticia
@receiver(post_save, sender=Noticia)
def save_news(sender, instance, **kwargs):
    # variable con el slug armado
    slug = slugify(instance.titular + " " + str(instance.id))
    # filtramos la noticia recien creada y actualizamos el slug
    Noticia.objects.filter(id=instance.id).update(slug=slug)
    print('signal dispatched - Señal enviada')
