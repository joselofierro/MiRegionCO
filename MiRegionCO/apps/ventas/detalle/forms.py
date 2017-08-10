from django import forms

from apps.ventas.categoria_producto.models import CategoriaProducto
from apps.ventas.detalle.models import Detalle


class DetalleForm(forms.ModelForm):
    class Meta:
        model = Detalle

        fields = [
            'categoria',
            'subcategoria',
            'producto',
        ]

        labels = {
            'categoria': 'Categorias',
            'subcategoria': 'Subcategorias',
            'producto': 'Productos'
        }

        widgets = {
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'subcategoria': forms.Select(attrs={'class': 'form-control '}),
            'producto': forms.Select(attrs={'class': 'form-control'}),
        }
