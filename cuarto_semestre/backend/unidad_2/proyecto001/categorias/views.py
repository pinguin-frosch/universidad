from django.shortcuts import render, redirect
from django.urls import reverse
from categorias.models import Categoria
from categorias.forms import CategoriaForm


def listar(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias/listar.html', {
        'categorias': categorias
    })


def eliminar(_, id):
    categoria = Categoria.objects.get(id=id)
    categoria.delete()
    return redirect(reverse('categorias:listar'))


def crear(request):
    formulario = CategoriaForm()

    if request.method == 'POST':
        formulario = CategoriaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(reverse('categorias:listar'))

    return render(request, 'categorias/crear.html', {
        'formulario': formulario,
        'titulo': 'Crear categoria'
    })


def actualizar(request, id):
    categoria = Categoria.objects.get(id=id)
    formulario = CategoriaForm(instance=categoria)

    if request.method == 'POST':
        formulario = CategoriaForm(request.POST, instance=categoria)
        if formulario.is_valid():
            formulario.save()
            return redirect(reverse('categorias:listar'))

    return render(request, 'categorias/crear.html', {
        'formulario': formulario,
        'titulo': 'Actualizar categoria'
    })
