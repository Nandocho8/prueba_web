from django.db import models

# Create your models here.
from django.db import models
from django import forms

# Create your models here.


class Pokemon(models.Model):
    numero = models.IntegerField('numero_dex')
    nombre = models.CharField('nombre', max_length=50)
    tipo1 = models.CharField('Tipo Principal', max_length=50)
    tipo2 = models.CharField('Tipo secundario', max_length=50)
    peso = models.FloatField('peso')
    altura = models.FloatField('altura')
