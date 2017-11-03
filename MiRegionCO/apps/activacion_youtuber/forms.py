from django import forms

from apps.activacion_youtuber.models import Youtuber


class YoutuberForm(forms.ModelForm):
    class Meta:
        model = Youtuber

        fields = [
            'codigo',
            'nombre',
            'foto',
            'visible'
        ]

        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'foto': forms.URLInput(attrs={'class': 'form-control'}),
            'visible': forms.CheckboxInput(attrs={'class': 'form-control'})
        }
