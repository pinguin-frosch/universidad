from django.shortcuts import render
from personas.forms import PersonaForm

def index(request):
    return render(request, 'personas/index.html')

def registro(request):
    if request.method == 'POST':
        formulario = PersonaForm(request.POST)
        if formulario.is_valid():
            formulario.save()

    formulario = PersonaForm()

    return render(request, 'personas/registro.html', {
        'formulario': formulario
    })