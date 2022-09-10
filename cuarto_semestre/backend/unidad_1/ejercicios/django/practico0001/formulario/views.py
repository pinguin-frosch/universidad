from django.shortcuts import render, redirect
from django.urls import reverse
from django import forms

class Formulario(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100)

def index(request):
    if request.method == 'POST':
        nombre = request.POST["nombre"]
        with open('nombres.txt', 'a') as file:
            file.write(f'Hola <b>{nombre}</b>\n')

    return render(request, 'formulario/index.html')

def saludar(request, nombre):
    return render(request, 'formulario/saludar.html', {
        'nombre': nombre
    })

def lista(request):
    with open('nombres.txt', 'r') as file:
        nombres = file.readlines()
    return render(request, 'formulario/lista.html', {
        'lista': nombres
    })