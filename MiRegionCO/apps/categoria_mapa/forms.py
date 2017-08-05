from django import forms

from apps.categoria_mapa.models import CategoriaMapa


class MapaForm(forms.ModelForm):
    class Meta:
        model = CategoriaMapa

        fields = [
            'nombre',
            'imagen'
        ]

        labels = {
            'nombre': 'Nombre',
            'imagen': 'Imagen'
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'})
        }
