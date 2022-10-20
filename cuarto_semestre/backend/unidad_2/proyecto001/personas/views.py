from django.shortcuts import render
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

    return render(request, 'personas/registro.html', {
        'formulario': formulario
    })
