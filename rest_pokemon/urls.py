from django.urls import path
from .views import lista_pokemon, detalle_pokemon, apiDex

urlpatterns = [
    path('rest_pokemon', lista_pokemon, name="rest_pokemon"),
    path('detalle_pokemon/<id>', detalle_pokemon, name='detalle_juego'),
    path('dex', apiDex, name='dex')
]
