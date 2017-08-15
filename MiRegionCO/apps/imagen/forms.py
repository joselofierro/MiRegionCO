
from django import forms

from apps.imagen.models import Imagen


class ImagenForm(forms.ModelForm):
    class Meta:
        model = Imagen

        fields = [
            'imagen'
        ]

        labels = {
            'imagen': 'Imagen'
        }

        widgets = {
            'imagen': forms.FileInput(attrs={'class': 'form-control', 'multiple': True})
        }


