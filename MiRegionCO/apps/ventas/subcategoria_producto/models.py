from django.db import models


class Subcategoria(models.Model):
    nombre = models.TextField(max_length=30, blank=False, null=False)

    def __str__(self):
        return self.nombre
