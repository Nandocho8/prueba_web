from django import forms
from .models import Juegos


class FormAgregarJuegos(forms.ModelForm):
    class Meta:
        model = Juegos
        fields = "__all__"
