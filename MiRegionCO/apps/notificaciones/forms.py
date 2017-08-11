from django import forms

from apps.notificaciones.models import Notificacion


class NotificacionForm(forms.ModelForm):
    class Meta:
        model = Notificacion

        fields = [
            'titulo',
            'mensaje'
        ]

        labels = {
            'titulo': 'Titulo',
            'mensaje': 'Mensaje'
        }

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control'})
        }
