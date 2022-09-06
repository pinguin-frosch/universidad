from django.shortcuts import render

def index(request):
    return render(request, 'aplicacion/index.html')

def computacion(request):
    return render(request, 'aplicacion/detalles.html', {
        'titulo': 'Computación',
        'nombre_producto': 'Computador portátil',
        'detalle': 'Notebook HP de gran calidad'
    })

def videojuegos(request):
    return render(request, 'aplicacion/detalles.html', {
        'titulo': 'Videojuegos',
        'nombre_producto': 'The Legend of Zelda: The Breath of the Wild',
        'detalle': 'Excelente juego que no te puedes perder'
    })

def electronica(request):
    return render(request, 'aplicacion/detalles.html', {
        'titulo': 'Electrónica',
        'nombre_producto': 'Raspberry pi',
        'detalle': 'Excelente producto para cualquier tipo de servidor'
    })