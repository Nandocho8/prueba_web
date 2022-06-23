from django.shortcuts import render
from .models import Noticias
# Create your views here.


def noticias(request):
    noticias = Noticias.objects.all()
    data = {'news': noticias}
    return render(request, '_noticias/noticias.html', data)
