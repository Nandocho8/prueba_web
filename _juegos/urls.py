"""foro_gamer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from .views import agregar_juegos, modificar_juegos, eliminar_juegos
from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers


urlpatterns = [
    path('', views.juegos, name='juegos'),
    path('agregar_juegos/', views.agregar_juegos, name='juegos_agrega'),
    path('editar_juegos/<id>/', views.modificar_juegos,
         name='juegos_modifica'),
    path('eliminar_juegos/<id>/', views.eliminar_juegos,
         name='juegos_elimina'),

]
