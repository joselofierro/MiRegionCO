from django.db import models


class Producto(models.Model):
    tiempo = models.IntegerField(blank=False, null=False)
    precio = models.IntegerField(blank=False, null=False)
    medida = models.CharField(max_length=1)

    def __str__(self):
        return '{} {}, ${}'.format(self.tiempo, self.medida, self.precio)
