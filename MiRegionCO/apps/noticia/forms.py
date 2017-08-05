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
            'imagenes',
            'video',
            'autor',
            'tag',
            'categoria',
            'destacada'
        ]

        labels = {
            'fecha': 'Fecha',
            'hora': 'Hora',
            'titular': 'Titular',
            'lead': 'Lead',
            'texto': 'Texto',
            'imagenes': 'Imagenes',
            'video': 'Video',
            'autor': 'Autor',
            'tag': 'Tag',
            'categoria': 'Categoria',
            'destacada': '¿Es destacada?'

        }

        widgets = {
            'fecha': forms.DateInput(attrs={'class': 'form-control'}),
            'hora': forms.TimeInput(attrs={'class': 'form-control'}),
            'titular': forms.TextInput(attrs={'class': 'form-control'}),
            'lead': forms.TextInput(attrs={'class': 'form-control'}),
            'texto': forms.Textarea(attrs={'class': 'form-control'}),
            'imagenes': forms.SelectMultiple(attrs={'class': 'form-control select2_multiple'}),
            'video': forms.URLInput(attrs={'class': 'form-control'}),
            'autor': forms.Select(attrs={'class': 'form-control'}),
            'tag': forms.SelectMultiple(attrs={'class': 'form-control select2_multiple'}),
            'categoria': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'destacada': forms.CheckboxInput(attrs={'class': 'form-control'})
        }
