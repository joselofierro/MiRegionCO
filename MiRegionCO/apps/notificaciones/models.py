from django.db import models


class Notificacion(models.Model):
    fecha = models.TimeField(auto_now_add=True, null=True)
    hora = models.DateField(auto_now_add=True, null=True)
    titulo = models.CharField(max_length=100, null=False, blank=False, default='MiRegión.co')
    mensaje = models.TextField(max_length=140, null=False, blank=False)
