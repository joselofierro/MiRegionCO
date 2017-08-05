from apps.ventas.cliente.models import Cliente
from apps.ventas.detalle.models import Detalle
from django.db import models
from apps.ventas.vendedor.models import Vendedor


class Cotizacion(models.Model):
    fecha = models.DateField(auto_now_add=True)
    hora = models.TimeField(auto_now_add=True)
    descripcion = models.CharField(max_length=200, blank=False, null=False, default='')

    vendedor = models.ForeignKey(Vendedor)
    cliente = models.ForeignKey(Cliente)
    productos = models.ManyToManyField(Detalle)
