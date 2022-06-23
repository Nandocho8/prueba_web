from django import forms
from .models import Noticias


class FormAgregarNoticia(forms.ModelForm):
    class Meta:
        model = Noticias
        fields = "__all__"
        widgets = {
            'cuerpo': forms.Textarea()
        }
