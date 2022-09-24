from django.shortcuts import render

def registro(request):
    if request.method == 'POST':
        run = request.POST['run']
        nombre = request.POST['nombre']
        email = request.POST['email']
        telefono = request.POST['telefono']
        estado_civil = request.POST['estado_civil']
        genero = request.POST['genero']
        comentario = request.POST['comentario']

        registro = f'{run}|{nombre}|{email}|{telefono}|{estado_civil}|{genero}|{comentario}\n'

        with open('personas.txt', 'a') as archivo:
            archivo.write(registro)

    return render(request, 'personas/registro.html')

def lista(request):
    lista_personas = []

    with open('personas.txt', 'r') as archivo:
        for persona in archivo.readlines():
            nueva_persona = []

            for elemento in persona.split('|'):
                nueva_persona.append(elemento.rstrip('\n'))

            lista_personas.append(nueva_persona)

    print(lista_personas)

    return render(request, 'personas/lista.html', {
        'lista_personas': lista_personas
    })