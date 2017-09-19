from django.db import models


def upload_location(instance, filename):
    filebase, extension = filename.split(".")
    return "%s/%s.%s" % ('Imagen', instance.nombre, extension)


class Imagen(models.Model):
    nombre = models.CharField(max_length=150, null=False, blank=True, default='Imagen')
    imagen = models.ImageField(upload_to=upload_location, null=False, blank=False)

    def __str__(self):
        return self.nombre
