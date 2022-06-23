from django.shortcuts import render, redirect
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
    print('getgetgetgetgetgetgetgetgetgetgetgetgetgetgetget\n\n\n\n\n\n\n')

    print('POST POST POST POST POST POST POST \n\n\n\n\n ')
    if request.method == 'POST':
        print('IF POST IF POST IF POST IF POST IF POST IF POST \n\n\n\n\n')

        formulario = FormAgregarNoticia(data=request.POST, files=request.FILES)
        print('data data data data data data data data \n\n\n\n\n')
        print('form instance form instance form instance form instance \n\n\n\n\n')
        if formulario.is_valid():
            print('form valid form valid form valid form valid \n\n\n\n\n')
            formulario.save()
            print('form save form save form save form save form save ')
            data['mensaje'] = 'NOTICIA AGREGADA CON EXITO'
            return redirect('/')
        else:
            print('else if else if else if else if else if \n\n\n\n')
            data['form'] = formulario
            return render(request, '_noticias/agregar_noticias.html', data)

    else:
        print('else else else else else else else \n\n\n\n')
        return render(request, '_noticias/agregar_noticias.html', data)
        # return redirect('juegos/')
