from django import forms

from apps.ventas.vendedor.models import Vendedor


class VendedorForm(forms.ModelForm):
    class Meta:
        model = Vendedor

        fields = [
            'cedula',
            'nombre',
            'apellido',
            'correo',
            'telefono',
            'direccion',
            'contrasena'
        ]

        labels = {
            'cedula': 'Cedula',
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'correo': 'Correo electronico',
            'telefono': 'Telefono',
            'direccion': 'Direccion',
            'contrasena': 'Contraseña'
        }

        widgets = {

            'cedula': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'contrasena': forms.PasswordInput(attrs={'class': 'form-control'})
        }
