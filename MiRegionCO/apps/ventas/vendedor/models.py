from django.db import models


class Vendedor(models.Model):
    cedula = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField(unique=True)
    telefono = models.BigIntegerField(blank=False, null=False)
    direccion = models.CharField(max_length=30)
    contrasena = models.TextField(blank=False, null=False, default='')

    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellido)
