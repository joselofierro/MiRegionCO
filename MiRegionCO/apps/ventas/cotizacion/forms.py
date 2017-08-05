from django import forms

from apps.ventas.cotizacion.models import Cotizacion


class CotizacionForm(forms.ModelForm):
    class Meta:
        model = Cotizacion

        fields = [

            'descripcion',
            'vendedor',
            'cliente',
            'productos'
        ]

        labels = {

            'descripcion': 'Descripcion',
            'vendedor': 'Vendedor',
            'cliente': 'Cliente',
            'productos': 'Productos'

        }

        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'vendedor': forms.TextInput(attrs={'class': 'form-control'}),
            'cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'productos': forms.SelectMultiple(attrs={'class': 'form-control select2_multiple'})
        }
