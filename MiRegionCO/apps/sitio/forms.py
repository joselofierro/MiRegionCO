from django import forms

from apps.sitio.models import Sitio


class SitioForm(forms.ModelForm):
    class Meta:
        model = Sitio

        fields = [
            'nombre',
            'titulo',
            'descripcion',
            'logo',
            'horario',
            'direccion',
            'instagram',
            'facebook',
            'telefono',
            'imagenes',
            'subcategoria',
            'latitud',
            'longitud'
        ]

        labels = {

            'nombre': 'Nombre',
            'titulo': 'Titulo',
            'descripcion': 'Descripcion',
            'logo': 'Logo',
            'horario': 'Horario',
            'direccion': 'Direccion',
            'instagram': 'Instagram',
            'facebook': 'Facebook',
            'telefono': 'Telefono',
            'imagenes': 'Imagenes',
            'subcategoria': 'Subcategoria',
            'latitud': 'Latitud',
            'longitud': 'Longitud'

        }

        widgets = {

            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'horario': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'instagram': forms.TextInput(attrs={'class': 'form-control'}),
            'facebook': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control'}),
            'imagenes': forms.SelectMultiple(attrs={'class': 'form-control select2_multiple'}),
            'subcategoria': forms.SelectMultiple(attrs={'class': 'form-control select2_multiple'}),
            'latitud': forms.NumberInput(attrs={'class': 'form-control'}),
            'longitud': forms.NumberInput(attrs={'class': 'form-control'})
        }
