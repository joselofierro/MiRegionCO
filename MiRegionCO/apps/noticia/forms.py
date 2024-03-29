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
            'url',
            'video',
            'duracion',
            'categoria',
            'destacada',
            'web',
            'mobile'
        ]

        labels = {
            'fecha': 'Fecha',
            'hora': 'Hora',
            'titular': 'Titular',
            'lead': 'Lead',
            'texto': 'Texto',
            'url': 'URL',
            'video': 'Video',
            'duracion': 'Duracion',
            'categoria': 'Categoria',
            'destacada': '¿Es destacada?',
            'web': '¿Visible en página?',
            'mobile': '¿Visible en App?'
        }

        widgets = {
            'fecha': forms.DateInput(
                attrs={'class': 'form-control', 'placeholder': 'dd/mm/yyyy', 'id': 'datetimepicker1'}),
            'hora': forms.TimeInput(attrs={'class': 'form-control', 'placeholder': '24:00 '}),
            'titular': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe el titular'}),
            'lead': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe el lead'}),
            'texto': forms.Textarea(attrs={'class': 'form-control'}),
            'url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Solo esriba aquí si es un evento o una oferta... 🙏🏻'}),
            'video': forms.URLInput(attrs={'class': 'form-control'}),
            'duracion': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'destacada': forms.CheckboxInput(attrs={'class': 'form-control chkbox'}),
            'web': forms.CheckboxInput(attrs={'class': 'form-control chkbox'}),
            'mobile': forms.CheckboxInput(attrs={'class': 'form-control chkbox'}),
        }
