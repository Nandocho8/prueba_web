from django.db import models
from django import forms

# Create your models here.


class Noticias(models.Model):
    nombre = models.CharField('nombre', max_length=30)
    titulo = models.CharField('titulo', max_length=100)
    cuerpo = models.CharField(max_length=800)
    imagen = models.ImageField(upload_to='noticias', blank=True, null=True)
    link = models.CharField('link', max_length=300, default='www.google.com')

    def __str__(self):
        return self.nombre
