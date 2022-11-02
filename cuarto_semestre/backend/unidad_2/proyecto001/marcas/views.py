from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Marca
from marcas.forms import MarcaForm

def listar(request):
    marcas = Marca.objects.all()
    return render(request, 'marcas/listar.html', {
        'marcas': marcas
    })

def crear(request):
    formulario = MarcaForm()

    if request.method == 'POST':
        formulario = MarcaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(reverse('marcas:listar'))

    return render(request, 'marcas/crear.html', {
        'formulario': formulario,
        'titulo': 'Crear marca'
    })

def eliminar(_, id):
    marca = Marca.objects.get(id=id)
    marca.delete()
    return redirect(reverse('marcas:listar'))

def actualizar(request, id):
    marca = Marca.objects.get(id=id)
    formulario = MarcaForm(instance=marca)

    if request.method == 'POST':
        formulario = MarcaForm(request.POST, instance=marca)
        if formulario.is_valid():
            formulario.save()
            return redirect(reverse('marcas:listar'))

    return render(request, 'marcas/crear.html', {
        'formulario': formulario,
        'titulo': 'Actualizar marca'
    })