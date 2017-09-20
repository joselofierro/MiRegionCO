from django import forms

from apps.imagen.models import Imagen
from apps.sitio.models import Sitio
from apps.subcategoria_mapa.models import SubcategoriaMapa


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
            # 'imagenes',
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
            # 'imagenes': 'Imagenes',
            'subcategoria': 'Subcategoria',
            'latitud': 'Latitud',
            'longitud': 'Longitud'

        }

        widgets = {

            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'cols': 6}),
            'horario': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'instagram': forms.TextInput(attrs={'class': 'form-control'}),
            'facebook': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control'}),
            # 'imagenes': forms.SelectMultiple(attrs={'class': 'form-control select2_multiple'}),
            'subcategoria': forms.SelectMultiple(attrs={'class': 'form-control select2_multiple'}),
            'latitud': forms.NumberInput(attrs={'class': 'form-control'}),
            'longitud': forms.NumberInput(attrs={'class': 'form-control'})
        }

    # sobreescribimos el metodo
    def __init__(self, *args, **kwargs):
        super(SitioForm, self).__init__(*args, **kwargs)
        self.fields['imagenes'].queryset = Imagen.objects.order_by('nombre')
        self.fields['subcategoria'].queryset = SubcategoriaMapa.objects.order_by('nombre')
