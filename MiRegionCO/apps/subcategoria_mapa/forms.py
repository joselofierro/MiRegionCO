from django import forms

from apps.subcategoria_mapa.models import SubcategoriaMapa


class SubcategoriaMapaForm(forms.ModelForm):
    class Meta:
        model = SubcategoriaMapa

        fields = [
            'nombre'
        ]

        labels = {
            'nombre': 'Nombre'
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'})
        }
