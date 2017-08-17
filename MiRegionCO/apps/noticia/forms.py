from django import forms

from apps.noticia.models import Noticia


class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia

        fields = [
            'fecha',
            'hora',
            'titular',
            'lead',
            'texto',
            'video',
            'duracion',
            'categoria',
            'destacada'
        ]

        labels = {
            'fecha': 'Fecha',
            'hora': 'Hora',
            'titular': 'Titular',
            'lead': 'Lead',
            'texto': 'Texto',
            'video': 'Video',
            'duracion': 'Duracion',
            'categoria': 'Categoria',
            'destacada': '¿Es destacada?'

        }

        widgets = {
            'fecha': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/yyyy'}, ),
            'hora': forms.TimeInput(attrs={'class': 'form-control', 'placeholder': '24:00 '}),
            'titular': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe el titular'}),
            'lead': forms.TextInput(attrs={'class': 'form-control'}),
            'texto': forms.Textarea(attrs={'class': 'form-control'}),
            'video': forms.URLInput(attrs={'class': 'form-control'}),
            'duracion': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'destacada': forms.CheckboxInput(attrs={'class': 'form-control'})
        }
