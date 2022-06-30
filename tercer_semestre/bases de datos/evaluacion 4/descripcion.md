# Evaluacion 4

Tenemos que crear una base de datos que incluya la información de de algún caso
en particular, yo me decidí por la idea de hacer una base de datos para un
servicio de streaming, algo así como netflix. Lo llamaremos <NOMBRE>.
Contaremos con 3 colecciones, comentarios, películas, y usuarios. Pero eso es
solo el comienzo, si al negocio le sigue yendo bien podríamos implementar más
funciones y por lo tanto tener que almacenar más imformación.

## Comentarios
Esta colección tendrá 6 campos, el id, nombre, correo, id de la película, el
texto y la fecha. id será el ObjectId una vez dentro de la base de datos, el
nombre y correos son los datos del usuario que emitió el comentario, id de la
película es para luego poder relacionar el comentario a la película respectiva.
El texto es solo el comentario como tal, no sus metadatos, y finalmente está la
fecha que solo indica cuando se emitió el comentario.

## Película
Aquí estará la información de cada una de las películas disponibles en el
sistema. Para las películas necesitamos algo más de información, pero tampoco
tenemos que irnos al extremo. Incluiremos un id, resumen, géneros, actores,
comentarios, nombre, fecha lanzamiento y directores. Id es lo mismo que con los
comentarios, resumen es eso, un resumen de la película, como una descripción,
géneros será una lista con todos los géneros de la película. Actores también
será una lista que contiene documetos con la información principal de cada
actor. Comentarios es solo la cantidad de comentarios vinculados con esa
película, para no tener que realizar una consulta cada vez para determinar
cuantos comentarios existen. Nombre será el nombre de la película, la fecha
corresponde a cuando se lanzó la película y los directores será una lista de
objetos como con los actores.

## Usuarios
Esta colección se encargará de almacenar la información de los usuarios
registrados en la aplicación, de esta forma también luego se pueden vincular
los comentarios asociados que tengan, no es posible comentar si no se tiene una
cuenta. Cada usuario contará con un id, un nombre, correo y contraseña. El id
no hace falta comentarlo, el nombre y correo son evidentes. Y la contraseña
para los propósitos de simplicidad será almacenada en texto plano, aunque en un
caso real guardaríamos solo el hash para evitar problemas de seguridad producto
de ello.

## Estructura de la base de datos
La estructura final de la base de datos será algo como esto:

Comentarios
{
    "id": ObjectId(""),
    "usuario": {
        "nombre": "",
        "correo": ""
    }
    "id_película": ObjectId(""),
    "texto": "",
    "fecha": new Date(),
    "modificaciones": {
        "veces_modificado": 0,
        "ultimos_comentarios": ["", "", ""]
    }
}

Películas
{
    "_id": ObjectId(""),
    "resumen": "",
    "géneros": [""],
    "actores": {
        "cantidad": 0,
        "lista": [{}]
    }
    "comentarios": 0,
    "nombre": "",
    "fecha lanzamiento": new Date(),
    "directores": {
        "cantidad": 0,
        "lista": [{}]
    }
}

Usuarios
{
    "_id": ObjectId(""),
    "nombre": "",
    "correo": "",
    "contraseña": "",
    "nombres_anteriores": {
        "veces_modificado": 0,
        "nombres": ["", "", ""]
    },
    "peliculas_vistas": {
        "cantidad": 0,
        "peliculas": ["", "", ""]
    }
}
