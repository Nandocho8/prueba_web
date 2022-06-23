from django.shortcuts import render

# Create your views here.


def juegos(request):
    juegos = Juegos.objects.all()
    data = {'news': juegos}
    return render(request, '_juegos/juegos.html', data)


def agregar_juegos(request):
    data = {
        'form': FormAgregarJuegos()
    }

    if request.method == 'POST':

        formulario = FormAgregarJuegos(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'JUEGO AGREGADO CON EXITO'
            return redirect('/')
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
            data['mensaje'] = 'jUEGO MODIFICADO CON EXITO'
            return redirect(to='juegos')
        else:
            data['form'] = formulario
            return render(request, '_juegos/editar_juegos.html', data)

    else:
        return render(request, '_juegos/editar_juegos.html', data)


def eliminar_juegos(request, id):
    juegos = get_object_or_404(Juegos, id=id)
    juegos.delete()
    return redirect(to='juegos')
