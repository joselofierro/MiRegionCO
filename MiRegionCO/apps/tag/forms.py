from django import forms

from apps.tag.models import Tag


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag

        fields = [
            'nombre'
        ]

        labels = {
            'nombre': 'Nombre'
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'})
        }
