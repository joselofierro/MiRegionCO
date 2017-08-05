from apps.ventas.categoria_producto.models import CategoriaProducto
from apps.ventas.subcategoria_producto.models import Subcategoria
from django.db import models

from apps.ventas.producto.models import Producto


class Detalle(models.Model):
    categoria = models.ForeignKey(CategoriaProducto)
    subcategoria = models.ForeignKey(Subcategoria)
    producto = models.ForeignKey(Producto)

    def __str__(self):
        return '{}, {}, {}'.format(self.categoria.nombre, self.subcategoria.nombre,
                                   '{}{}, {}'.format(self.producto.tiempo, self.producto.medida, self.producto.precio))
