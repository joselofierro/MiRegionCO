from django import forms

from apps.ventas.cliente.models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente

        fields = [
            'nombre_empresa',
            'direccion',
            'nombre_contacto',
            'telefono',
            'celular',
            'correo'
        ]

        labels = {
            'nombre_empresa': 'Nombre de empresa',
            'direccion': 'Direccion',
            'nombre_contacto': 'Nombre de contacto',
            'telefono': 'Telefono',
            'celular': 'Celular',
            'correo': 'Correo'
        }

        widgets = {
            'nombre_empresa': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_contacto': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'celular': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'})
        }
