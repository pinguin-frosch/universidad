from django.shortcuts import render, redirect
from django.urls import reverse
from personas.forms import PersonaForm
from personas.models import Persona


def index(request):
    personas = Persona.objects.all()
    return render(request, 'personas/index.html', {
        'personas': personas
    })


def registro(request):
    formulario = PersonaForm()

    if request.method == 'POST':
        formulario = PersonaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(reverse('personas:registro'))

    return render(request, 'personas/registro.html', {
        'formulario': formulario,
        'titulo': 'Registro de persona'
    })


def editar_persona(request, run):
    p = Persona.objects.get(run=run)
    formulario = PersonaForm(instance=p)

    if request.method == 'POST':
        formulario = PersonaForm(request.POST, instance=p)
        if formulario.is_valid():
            formulario.save()
            return redirect(reverse('personas:index'))

    return render(request, 'personas/registro.html', {
        'formulario': formulario,
        'titulo': 'Actualizar persona'
    })

def eliminar_persona(request, run):
    p = Persona.objects.get(run=run)
    p.delete()
    return redirect(reverse('personas:index'))
