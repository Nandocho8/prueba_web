from django.db import models
from django import forms

# Create your models here.


class Juegos(models.Model):
    FISICO = 'F'
    DIGITAL = 'D'
    TIPO_VENTA = [
        (FISICO, 'Disponible en fisico'),
        (DIGITAL, 'Disponible en Digital')
    ]
    nombre = models.CharField('nombre', max_length=30)
    titulo = models.CharField('titulo', max_length=100)
    tipo = models.CharField('disponibilidad', max_length=1, choices=TIPO_VENTA)
    imagen = models.ImageField(upload_to='noticias', blank=True, null=True)
    link = models.CharField('link', max_length=300, default='hola')

    def __str__(self):
        return self.nombre
