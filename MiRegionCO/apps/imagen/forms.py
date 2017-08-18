
from django import forms

from apps.imagen.models import Imagen


class ImagenForm(forms.ModelForm):
    class Meta:
        model = Imagen

        fields = [
            'nombre',
            'imagen'
        ]

        labels = {
            'nombre': 'Nombre',
            'imagen': 'Imagen'
        }

        widgets = {
            'imagen': forms.FileInput(attrs={'class': 'form-control', 'multiple': True})
        }


