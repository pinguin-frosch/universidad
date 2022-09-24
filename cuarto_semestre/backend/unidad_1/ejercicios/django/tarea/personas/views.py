from django.shortcuts import render

def registro(request):
    if request.method == 'POST':
        # Obtener cada elemento de POST
        run = request.POST['run']
        nombre = request.POST['nombre']
        correo = request.POST['correo']
        telefono = request.POST['telefono']
        estado_civil = request.POST['estado_civil']
        genero = request.POST['genero']
        comentario = request.POST['comentario']

        # Crear variable string del registro
        registro = f'{run}|{nombre}|{correo}|{telefono}|{estado_civil}|{genero}|{comentario}\n'

        # Abrir "base de datos" y guardar el registro
        with open('personas.txt', 'a') as archivo:
            archivo.write(registro)

    # Enviar la plantilla para el método GET
    return render(request, 'personas/registro.html')

def lista(request):
    # Leer base de datos y generar estructura
    lista_personas = []

    # Abrir base de datos
    with open('personas.txt', 'r') as archivo:
        # Ciclar por cada línea del archivo
        for linea in archivo.readlines():
            # Crear variable para almacenar persona actual
            persona = []

            # Ciclar por cada elemento de la línea separado por |
            for elemento in linea.rstrip('\n').split('|'):
                # Añadir el elemento a la persona
                persona.append(elemento)

            # Agregar la persona a la lista de personas
            lista_personas.append(persona)


    # Enviar plantilla con los datos
    return render(request, 'personas/lista.html', {
        'lista_personas': lista_personas
    })