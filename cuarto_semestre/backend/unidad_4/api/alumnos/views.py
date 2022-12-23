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
