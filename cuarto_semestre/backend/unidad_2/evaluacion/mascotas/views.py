from django.shortcuts import render, redirect
from django.urls import reverse
from mascotas.forms import MascotaFormulario
from mascotas.models import Mascota


def listar(request):
    mascotas = Mascota.objects.all()

    return render(request, 'mascotas/listar.html', {
        'mascotas': mascotas
    })


def crear(request):
    formulario = MascotaFormulario()

    if request.method == 'POST':
        formulario = MascotaFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(reverse('mascotas:listar'))

    return render(request, 'mascotas/crear.html', {
        'formulario': formulario
    })


def actualizar(request, id):
    mascota = Mascota.objects.get(id=id)
    formulario = MascotaFormulario(instance=mascota)

    if request.method == 'POST':
        formulario = MascotaFormulario(request.POST, instance=mascota)
        if formulario.is_valid():
            formulario.save()
            return redirect(reverse('mascotas:listar'))

    return render(request, 'mascotas/crear.html', {
        'formulario': formulario
    })


def eliminar(_, id):
    mascota = Mascota.objects.get(id=id)
    mascota.delete()
    return redirect(reverse('mascotas:listar'))
