from django import forms

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
            'categoria': forms.SelectMultiple(attrs={'class': 'form-control select2_multiple'}),
            'subcategoria': forms.SelectMultiple(attrs={'class': 'form-control select2_multiple'}),
            'producto': forms.SelectMultiple(attrs={'class': 'form-control select2_multiple'}),
        }
