from django.shortcuts import render, redirect, get_object_or_404
from .forms import FormAgregarJuegos
from .models import Juegos
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
# Create your views here.


def juegos(request):
    juegos = Juegos.objects.all()
    page = request.GET.get('page', 1)

    try:
        # ? ACA ESTA LA INSTANCIA
        paginator = Paginator(juegos, 8)
        juegos = paginator.page(page)
    except:
        raise Http404

    data = {'entity': juegos,
            'paginator': paginator
            }
    return render(request, '_juegos/juego.html', data)


def agregar_juegos(request):
    data = {
        'form': FormAgregarJuegos()
    }

    if request.method == 'POST':

        formulario = FormAgregarJuegos(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Agregado con exito")
            # todo cambiar
            return redirect(to='/juegos')
        else:
            data['form'] = formulario
            return render(request, '_juegos/agregar_juegos.html', data)

    else:
        return render(request, '_juegos/agregar_juegos.html', data)
        # return redirect('juegos/')


def modificar_juegos(request, id):
    juegos = get_object_or_404(Juegos, id=id)
    data = {
        'form': FormAgregarJuegos(instance=juegos)
    }
    if request.method == 'POST':

        formulario = FormAgregarJuegos(
            data=request.POST, files=request.FILES, instance=juegos)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Juego modificado")
            return redirect(to='juegos', )
        else:
            data['form'] = formulario
            return render(request, '_juegos/editar_juegos.html', data)

    else:
        return render(request, '_juegos/editar_juegos.html', data)


def eliminar_juegos(request, id):
    juegos = get_object_or_404(Juegos, id=id)
    juegos.delete()
    messages.success(request, "Juego Eliminado")
    return redirect(to='juegos')
