from django.shortcuts import render, redirect
from _noticias.models import Noticias
from _juegos.models import Juegos
from django.db.models import Q

# Create your views here.


def find_page(request):
    print(request.GET)
    queryset = request.GET.get('buscar')
    if queryset:
        noticias = Noticias.objects.filter(
            Q(titulo__icontains=queryset) |
            Q(cuerpo__icontains=queryset)
        ).distinct()
        juegos = Juegos.objects.filter(
            Q(titulo__icontains=queryset)
        )
        data = {'data': [noticias, juegos]}
    else:
        noticias = Noticias.objects.all()
        data = {'noticias': noticias}

    return redirect('_base/buscar.html')
