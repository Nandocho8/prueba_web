from django.urls import path
from .views import lista_noticias, detalle_noticias

urlpatterns = [
    path('rest_noticias', lista_noticias, name="rest_noticias"),
    path('detalle_noticias/<id>', detalle_noticias, name='detalle_juego')
]
