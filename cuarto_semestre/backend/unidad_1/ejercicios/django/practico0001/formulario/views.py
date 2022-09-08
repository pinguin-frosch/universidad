from django.shortcuts import render, redirect
from django.urls import reverse
from django import forms

class Formulario(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100)

def index(request):
    if request.method == 'POST':
        nombre = request.POST["nombre"]
        return redirect('formulario:saludar', nombre)

    return render(request, 'formulario/index.html')

def saludar(request, nombre):
    return render(request, 'formulario/saludar.html', {
        'nombre': nombre
    })