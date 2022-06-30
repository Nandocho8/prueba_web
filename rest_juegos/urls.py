from django.urls import path
from .views import lista_juegos, detalle_juegos

urlpatterns = [
    path('rest_juegos', lista_juegos, name="rest_juegos"),
    path('detalle_juegos/<id>', detalle_juegos, name='detalle_juego')
]
