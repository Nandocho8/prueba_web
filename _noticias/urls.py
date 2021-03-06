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
from django.contrib import admin
from django.urls import path
from . import views
from .views import agregar_noticias, modificar_noticias, eliminar_noticias, find_page

urlpatterns = [
    path('', views.noticias, name='noticias'),
    path('agregar_noticias/', views.agregar_noticias, name='noticias_agrega'),
    path('editar_noticias/<id>/', views.modificar_noticias,
         name='noticias_modifica'),
    path('eliminar_noticias/<id>/', views.eliminar_noticias,
         name='noticias_elimina'),
    path('buscar/', views.find_page, name='buscanot')
]
