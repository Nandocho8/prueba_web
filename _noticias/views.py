from django.shortcuts import render, redirect, get_object_or_404
from .models import Noticias
from .forms import FormAgregarNoticia

# Create your views here.


def noticias(request):
    noticias = Noticias.objects.all()
    data = {'news': noticias}
    return render(request, '_noticias/noticias.html', data)


def agregar_noticias(request):
    data = {
        'form': FormAgregarNoticia()
    }

    if request.method == 'POST':

        formulario = FormAgregarNoticia(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'NOTICIA AGREGADA CON EXITO'
            return redirect('/')
        else:
            data['form'] = formulario
            return render(request, '_noticias/agregar_noticias.html', data)

    else:
        return render(request, '_noticias/agregar_noticias.html', data)
        # return redirect('juegos/')


def modificar_noticias(request, id):
    noticias = get_object_or_404(Noticias, id=id)
    data = {
        'form': FormAgregarNoticia(instance=noticias)
    }
    if request.method == 'POST':

        formulario = FormAgregarNoticia(
            data=request.POST, files=request.FILES, instance=noticias)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'NOTICIA MODIFICADA CON EXITO'
            return redirect(to='noticias')
        else:
            data['form'] = formulario
            return render(request, '_noticias/editar_noticias.html', data)

    else:
        return render(request, '_noticias/editar_noticias.html', data)
