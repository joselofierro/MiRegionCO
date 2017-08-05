from django import forms

from apps.ventas.subcategoria_producto.models import Subcategoria


class SubcategoriaProductoForm(forms.ModelForm):
    class Meta:
        model = Subcategoria

        fields = [
            'nombre'
        ]

        labels = {
            'nombre': 'Nombre'
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'})
        }
