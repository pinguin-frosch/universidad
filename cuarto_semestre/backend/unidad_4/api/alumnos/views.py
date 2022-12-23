from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from alumnos.models import Alumno
from alumnos.serializers import AlumnoSerializer


@api_view(['GET', 'POST'])
def lista_alumnos(request):
    if request.method == 'GET':
        alumnos = Alumno.objects.all()
        serializer = AlumnoSerializer(alumnos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AlumnoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def detalle_alumno(request, id):
    try:
        alumno = Alumno.objects.get(id=id)
    except Alumno.DoesNotExist:
        data = {f'No existe el alumno con id {id}'}
        return Response(data, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AlumnoSerializer(alumno)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AlumnoSerializer(alumno, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        alumno.delete()
        data = {f'El alumno con id {id} ha sido eliminado'}
        return Response(data, status=status.HTTP_204_NO_CONTENT)
