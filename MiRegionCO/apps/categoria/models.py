from django.db import models


# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=30, blank=False, null=False)
    color = models.CharField(max_length=10, blank=False, null=False)

    def __str__(self):
        return self.nombre
