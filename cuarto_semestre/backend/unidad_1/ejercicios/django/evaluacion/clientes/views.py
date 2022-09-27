from django.shortcuts import render

def planes(request):
    if request.method == 'POST':
        rut = request.POST['rut']
        nombre = request.POST['nombre']
        telefono = request.POST['telefono']
        correo = request.POST['correo']
        direccion = request.POST['direccion']
        plan = request.POST['plan']
        comentario = request.POST['comentario']

        registro = f'{rut}|{nombre}|{telefono}|{correo}|{direccion}|{plan}|{comentario}\n'

        with open('infoplanes.txt', 'a') as archivo:
            archivo.write(registro)

    return render(request, 'clientes/planes.html')

def lista(request):
    clientes = []

    with open('infoplanes.txt', 'r') as archivo:
        for linea in archivo.readlines():
            cliente = []

            for elemento in linea.rstrip('\n').split('|'):
                cliente.append(elemento)

            clientes.append(cliente)

    return render(request, 'clientes/lista.html', {
        'clientes': clientes
    })