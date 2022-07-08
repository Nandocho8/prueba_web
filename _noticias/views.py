from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .models import Noticias
from .forms import FormAgregarNoticia
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404

# Create your views here.


def noticias(request):
    noticias = Noticias.objects.all()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(noticias, 4)
        noticias = paginator.page(page)
    except:
        raise Http404

    data = {'entity': noticias,
            'paginator': paginator,
            }
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


def eliminar_noticias(request, id):
    noticias = get_object_or_404(Noticias, id=id)
    noticias.delete()
    return redirect(to='noticias')


# Create your views here.


def find_page(request):
    print(request.GET)
    queryset = request.GET.get('buscar')
    if queryset:
        noticias = Noticias.objects.filter(
            Q(titulo__icontains=queryset) |
            Q(cuerpo__icontains=queryset)
        ).distinct()
        # juegos = Juegos.objects.filter(
        #     Q(titulo__icontains=queryset)
        # )
        data = {'data': noticias}
    else:
        noticias = Noticias.objects.all()
        data = {'noticias': noticias}

    return render(request, '_base/buscarNoticia.html', data)
