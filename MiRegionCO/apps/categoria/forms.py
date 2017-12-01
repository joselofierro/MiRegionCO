from django import forms
from apps.categoria.models import Categoria


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria

        fields = [
            'nombre',
            'color',
            'orden',
            'visibleApp',
            'visibleWeb',
        ]

        labels = {
            'nombre': 'Nombre',
            'visibleApp': 'App',
            'visibleWeb': 'Web',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'orden': forms.NumberInput(attrs={'class': 'form-control'}),
            'visibleApp': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'visibleWeb': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }
