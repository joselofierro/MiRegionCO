from django import forms

from apps.ventas.categoria_producto.models import CategoriaProducto


class CategoriaProductoForm(forms.ModelForm):
    class Meta:
        model = CategoriaProducto

        fields = [
            'nombre',
            'medida'
        ]

        labels = {
            'nombre': 'Nombre',
            'medida': 'Medida'
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'medida': forms.TextInput(attrs={'class': 'form-control'})
        }
