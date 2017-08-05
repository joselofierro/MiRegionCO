from django.db import models


class Cliente(models.Model):
    nombre_empresa = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    nombre_contacto = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    celular = models.CharField(max_length=20)
    correo = models.EmailField()

    def __str__(self):
        return '{}'.format(self.nombre_empresa)
