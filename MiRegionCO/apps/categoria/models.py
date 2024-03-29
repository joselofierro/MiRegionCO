from django.db import models


# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=30, blank=False, null=False)
    color = models.CharField(max_length=10, blank=False, null=False)
    orden = models.IntegerField(blank=False, null=False)
    visibleApp = models.BooleanField(blank=False, default=True)
    visibleWeb = models.BooleanField(blank=False, default=True)

    def __str__(self):
        return self.nombre
