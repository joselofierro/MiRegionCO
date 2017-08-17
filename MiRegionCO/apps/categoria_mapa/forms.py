from django import forms

from apps.categoria_mapa.models import CategoriaMapa


class MapaForm(forms.ModelForm):
    class Meta:
        model = CategoriaMapa

        fields = [
            'nombre',
            'imagen',
            'subcategoria_mapa'
        ]

        labels = {
            'nombre': 'Nombre',
            'imagen': 'Imagen',
            'subcategoria_mapa': 'Subcategoria'
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'subcategoria_mapa':forms.SelectMultiple(attrs={'class': 'form-control select2_multiple'})
        }
