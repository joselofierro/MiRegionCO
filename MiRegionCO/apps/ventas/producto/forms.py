from django import forms

from apps.ventas.producto.models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto

        fields = [
            'tiempo',
            'precio',
            'medida'
        ]

        labels = {
            'tiempo': 'Tiempo',
            'precio': 'Precio',
            'medida': 'Medida'
        }

        widgets = {
            'tiempo': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'medida': forms.TextInput(attrs={'class': 'form-control'})
        }
