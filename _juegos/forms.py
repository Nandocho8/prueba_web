from django import forms
from .models import Juegos


class FormAgregarNoticia(forms.ModelForm):
    class Meta:
        model = Juegos
        fields = "__all__"
