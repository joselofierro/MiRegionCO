from django.db import models


class Tag(models.Model):
    nombre = models.CharField(max_length=30, blank=False, null=False, unique=True)

    def __str__(self):
        return self.nombre
