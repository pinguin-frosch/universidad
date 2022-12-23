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
