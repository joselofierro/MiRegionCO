from django import forms
from apps.categoria.models import Categoria


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria

        fields = [
            'nombre',
            'color'
        ]

        labels = {
            'nombre': 'Nombre'
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
        }
