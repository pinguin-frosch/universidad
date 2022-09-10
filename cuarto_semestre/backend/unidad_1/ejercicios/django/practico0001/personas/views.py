from django.shortcuts import render

def registrar(request):
    if request.method == 'POST':
        # Obtener las variables desde POST
        nombre = request.POST['nombre'].strip()
        apellido = request.POST['apellido'].strip()
        email = request.POST['email']
        fecha_nacimiento = request.POST['fecha_nacimiento']

        # Dar vuelta el año y el día en la fecha
        partes_fecha = fecha_nacimiento.split('-')
        partes_fecha[0], partes_fecha[2] = partes_fecha[2], partes_fecha[0]
        fecha_nacimiento = '/'.join(partes_fecha)

        # Generar el formato de guardado con los datos
        registro = f'{nombre}|{apellido}|{fecha_nacimiento}|{email}\n'

        # Guardar el usuario registrado en la "base de datos"
        with open('personas.txt', 'a') as archivo:
            archivo.write(registro)

    return render(request, 'personas/registro.html')

def formato_web(personas):
    # Lista global de datos
    lista = []

    for persona in personas:
        # Lista para cada una de las personas
        lista_persona = []

        for elemento in persona.split('|'):
            lista_persona.append(elemento.strip('\n'))

        # Añadir los datos a la lista global
        lista.append(lista_persona)

    return lista

def listar(request):
    with open('personas.txt', 'r') as archivo:
        personas = formato_web(archivo.readlines())

    return render(request, 'personas/lista.html', {
        'personas': personas
    })