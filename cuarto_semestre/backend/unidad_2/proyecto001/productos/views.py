from django.shortcuts import render, redirect
from django.urls import reverse
from productos.forms import ProductoForm
from productos.models import Producto


def listar(request):
    productos = Producto.objects.all()
    return render(request, 'productos/listar.html', {
        'productos': productos
    })


def crear(request):
    formulario = ProductoForm()

    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(reverse('productos:listar'))

    return render(request, 'productos/crear.html', {
        'formulario': formulario,
        'titulo': 'Crear producto'
    })


def actualizar(request, id):
    producto = Producto.objects.get(id=id)
    formulario = ProductoForm(instance=producto)

    if request.method == 'POST':
        formulario = ProductoForm(request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            return redirect(reverse('productos:listar'))

    return render(request, 'productos/crear.html', {
        'formulario': formulario,
        'titulo': 'Actualizar producto'
    })


def eliminar(_, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect(reverse('productos:listar'))
