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
