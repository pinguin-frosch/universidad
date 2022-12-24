# API
Este es un proyecto simple para usar una api rest con django. La documentación
solo está pensada como una guía para tener mejor entendimiento de qué hace cada
cosa en el proyecto y poder repetirlo luego.

# Configuración inicial
Luego de haber creado el proyecto, primero que nada vamos a crear una
aplicación llamada alumnos, ya que eso será lo que vamos a manejar con esta
api.

```bash
python manage.py startapp alumnos
```

Después vamos a agregar la aplicación en settings.py.

```python
INSTALLED_APPS = [
    # ...
    "alumnos"
]
```

Ahora en mysql creamos una base de datos y un usuario que tenga acceso a esa
base de datos, para poder usarla en el proyecto. Desde mysql podemos hacer
esto:

```mysql
create database api;
create user 'api'@'localhost' identified by 'api';
grant all on api.* to 'api'@'localhost';
flush privileges;
```

Después probaremos a acceder a la base de datos desde la terminal con:
```bash
mysql -u api -p api
```

Si todo funciona bien haremos los cambios en `settings.py` para que se vea así:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "api",
        "PASSWORD": "api",
        "USER": "api"
    }
}
```

Finalmente vamos a aplicar las migraciones:

```bash
python manage.py migrate
```

# Modelos y serializadores
Dentro de alumnos, vamos a crear un modelo de base de datos que lo represente,
vamos a usar esta estrucutra:

```python
class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    matricula = models.PositiveIntegerField()
    correo = models.EmailField()

    def __str__(self):
        return f'{self.nombre} {self.matricula}'
```

Luego solo vamos a crear las migraciones y luego aplicarlas:

```bash
python manage.py makemigrations
python manage.py migrate
```

Vamos a instalar `djangorestframework` y lo añadiremos en las aplicaciones
instaladas en `settings.py`. 

```bash
pip install djangorestframework
```

```python
INSTALLED_APPS = [
    # ...
    "rest_framework"
]
```

Con esto podemos agregar un serializador para nuestro modelo de `Alumno`. Lo
haremos en un archivo nuevo llamado `serializers.py` en la aplicación de
alumnos.

```python
from rest_framework import serializers
from alumnos.models import Alumno


class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = '__all__'
```

# Vistas
Una vez que hayamos llegado hasta aquí podemos proceder a crear las vistas,
tendremos dos. Una principal que permitirá ver todos los alumnos y a su vez
crearlos. Por otra parte habrá otra vista que permita ver la información para
cada alumno en específico, así como actulizarlo o eliminarlo.

## Lista de usuarios
Primero haremos la vista de lista para los alumnos, lo haremos en `views.py` de
la aplicación. De esta forma:

```python
from rest_framework.decorators import api_view
from rest_framework.response import Response
from alumnos.models import Alumno
from alumnos.serializers import AlumnoSerializer


@api_view(['GET'])
def lista_alumnos(request):
    if request.method == 'GET':
        alumnos = Alumno.objects.all()
        serializer = AlumnoSerializer(alumnos, many=True)
        return Response(serializer.data)
```

Luego en `urls.py` de la aplicación vamos a añadir una ruta para acceder a la
vista que creamos:

```python
from django.urls import path
from alumnos import views

urlpatterns = [
    path('', views.lista_alumnos, name='alumnos')
]
```

Finalmente en `urls.py` del proyecto lo modificaremos para que se vea así:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/alumnos/', include('alumnos.urls'))
]
```

Usando un programa para probar apis, o el mismo navegador, podemos entrar a esa
ruta y deberíamos ver una lista vacía, ya que aún no hemos añadido a ningún
usuario.

Agregaremos una nueva vista. Esta nos permitirá añadir un alumno a nuestra base
de datos mediante la misma ruta, pero usando el método POST.

En `views.py` tenemos que agregar el siguiente import: `from rest_framework
import status`. Y cambiamos la función así:

```python
@api_view(['GET', 'POST'])
def lista_alumnos(request):
    if request.method == 'GET':
        # ...

    elif request.method == 'POST':
        serializer = AlumnoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

Ahora deberíamos poder agregar alumnos enviando una petición POST con la
información que necesitamos. Ejemplo:

```json
{
    "nombre": "Gabriel Barrientos",
    "correo": "gabri12.rubik@gmail.com",
    "matricula": 14
}
```

## Información de usuario
Lo siguiente es crear una nueva ruta que permita ver la información de solo un
usuario, al mismo tiempo que permita actualizarlo y eliminarlo.

En `views.py` agregaremos una nueva vista, de momento solo haremos la lectura:

```python
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
```

En `urls.py` cambiaremos `urlpatterns` de la siguiente forma:

```python
urlpatterns = [
    path('', views.lista_alumnos, name='alumnos'),
    path('<int:id>', views.detalle_alumno, name='detalle_alumno'),
]
```

El resto de los métodos harán los siguiente:

```python
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
```

Con eso ya se podría actualizar, eliminar y ver la información de un usuario,
usando los métodos HTTP respectivos.

# Configuración CORS
Ahora que ya contamos con todos los métodos de la api para manipular los
usuarios, haremos una página simple en html que se encargue de consumir la
información por medio de la api. Por razones de estilo además agregaremos
bootstrap al proyecto para que se vea algo mejor.

Antes que nada, por temas de políticas CORS tendremos que modificar algunas
cosas en django, de lo contrario no podremos usar nuestra api directamente
desde el navegador con fetch.

Usando pip vamos a instalar django-cors-headers:

```bash
pip install django-cors-headers
```

Luego en `settings.py` tenemos que agregar estas configuraciones o modificarlas
para que se vean así:

```python
ALLOWED_HOSTS = ['*']
CORS_ORIGIN_ALLOW_ALL = True

INSTALLED_APPS = [
    # ...
    'corsheaders'
]

MIDDLEWARE = [
    # ...
    'corsheaders.middleware.CorsMiddleware'
]
```
