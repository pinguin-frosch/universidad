from django.shortcuts import render, redirect
from django.urls import reverse
from tipos.forms import TipoFormulario
from tipos.models import Tipo


def listar(request):
    tipos = Tipo.objects.all()

    return render(request, 'tipos/listar.html', {
        'tipos': tipos
    })


def crear(request):
    formulario = TipoFormulario()

    if request.method == 'POST':
        formulario = TipoFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(reverse('tipos:listar'))

    return render(request, 'tipos/crear.html', {
        'formulario': formulario
    })
