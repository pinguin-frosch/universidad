// Evaluación 4 parte 2

use('jiffily')

// 1. Generar índice único para una columna dentro del documento (por
// colección)
db.peliculas.createIndex(
    {
        "titulo": 1
    },
    {
        unique: true
    }
)

db.comentarios.createIndex(
    {
        "usuario.nombre": 1
    }
)

db.usuarios.createIndex(
    {
        "nombre": 1
    }
)

// 2. Generar índices compuestos a libre elección (por colección)
db.peliculas.createIndex(
    {
        "titulo": 1,
        "actores.cantidad": 1
    },
    {
        unique: true
    }
)

db.comentarios.createIndex(
    {
        "usuario.nombre": 1,
        "usuario.correo": 1
    }
)

db.usuarios.createIndex(
    {
        "nombre": 1,
        "peliculas_vistas.cantidad": 1
    }
)

// 3. Aplicar instrucciones update (mínimo 5)

// Quitar el actor Robert Duvall de la película El padrino: parte II, además de
// disminuir la cantidad de actores para que coincida con la cantidad real
db.peliculas.updateOne(
    {
        "titulo": "El padrino: parte II"
    },
    {
        $inc: {
            "actores.cantidad": -1
        },
        $pull: {
            "actores.lista": "Robert Duvall"
        }
    }
)

// Añadir el género de ciencia ficción a la película Terminator 2: el juicio
// final
db.peliculas.updateOne(
    {
        "titulo": "Terminator 2: el juicio final"
    },
    {
        $push: {
            "generos": "Ciencia ficción"
        }
    }
)

// Cambiar el primer comentarios de Ned Stark por "Ya no quiero ver más
// películas", aumentar la cantidad de modificaciones y registrar el comentario
// anterior en las modificaciones
let resultado = db.comentarios.findOne(
    {
        "usuario.nombre": "Ned Stark"
    }
)
db.comentarios.updateMany(
    {
        "usuario.nombre": "Ned Stark"
    },
    {
        $push: {
            "modificaciones.comentarios_anteriores": resultado.comentario
        },
        $set: {
            "comentario": "Ya no quiero ver más películas"
        },
        $inc: {
            "modificaciones.veces_modificado": 1
        }
    }
)

// Cambiar el correo de Bran Stark por "bran_stark@gameofthron.es"
db.usuarios.updateOne(
    {
        "nombre": "Bran Stark"
    },
    {
        $set: {
            "correo": "bran_stark@gameofthron.es"
        }
    }
)

// Cambiar la contraseña de Margaery Tyrell por una más corta
db.usuarios.updateOne(
    {
        "nombre": "Margaery Tyrell"
    },
    {
        $set: {
            "contraseña": "$2b$12$AjC.876rd2dgsSIu.5c4qembdVfdDajMIgueMYuO"
        }
    }
)

// 4. Aplicar instrucciones delete (mínimo 5)

// Borrar el usuario Khal Drogo
db.usuarios.deleteOne(
    {
        "nombre": "Khal Drogo"
    }
)

// Si hay comentarios hechos por el usuario también hay que borrarlos
db.comentarios.deleteMany(
    {
        "usuario.nombre": "Khal Drogo"
    }
)

// Borrar la película Interstellar y guardar el resultado para luego borrar los
// comentarios
resultado = db.peliculas.findOne(
    {
        "titulo": "Interstellar"
    }
)
db.peliculas.deleteOne(
    {
        "titulo": "Interstellar"
    }
)

// Borrar los comentarios que hicieran relación a la película Interstellar
db.comentarios.deleteMany(
    {
        "id_pelicula": ObjectId(resultado._id)
    }
)

// Borrar todos los comentarios de la película El caballero oscuro
resultado = db.peliculas.findOne(
    {
        "titulo": "El caballero oscuro"
    }
)
db.comentarios.deleteMany(
    {
        "id_pelicula": resultado._id
    }
)

// 5. Aplicar consultas simples (mínimo 3)
// Mostrar el nombre y contraseña del usuario Davos Seaworth
db.usuarios.findOne(
    {
        "nombre": "Davos Seaworth"
    },
    {
        "nombre": 1,
        "contraseña": 1,
        "_id": 0
    }
)

// Buscar las 5 películas con más actores registrados
db.peliculas.find(
    {},
    {
        "titulo": 1,
        "actores.cantidad": 1,
        "_id": 0
    }
).sort(
    {
        "actores.cantidad": -1
    }
).limit(5)

// Mostrar los comentarios que hayan sido modificados al menos una vez, mostrar
// solo el comentario y el nombre del usuario que lo realizó
db.comentarios.find(
    {
        "modificaciones.veces_modificado": {
            $gte: 1
        }
    },
    {
        "comentario": 1,
        "usuario.nombre": 1,
        "_id": 0
    }
)

// 6. Aplicar consultas con operadores lógicos (mínimo 3)
// Mostrar las películas que hayan sido dirigidas por James Cameron o George
// Lucas. Mostrando el titulo y fecha de lanzamiento
db.peliculas.find(
    {
        $or: [
            {
                "directores.lista": "James Cameron"
            },
            {
                "directores.lista": "George Lucas"
            }
        ]
    },
    {
        "titulo": 1,
        "fecha_de_lanzamiento": 1,
        "_id": 0
    }
)

// Buscar la película en la que participe Mark Hamill y Harrison Ford como
// actores y el director sea George Lucas
db.peliculas.find(
    {
        $and: [
            {
                "actores.lista": {
                    $all: [
                        "Mark Hamill",
                        "Harrison Ford"
                    ]
                }
            },
            {
                "directores.lista": "George Lucas"
            }
        ]
    }
)

// Buscar las películas de los directores Sergio Leone y Frank Darabont.
// Mostrar el título y resumen
db.peliculas.find(
    {
        $or: [
            {
                "directores.lista": "Sergio Leone"
            },
            {
                "directores.lista": "Frank Darabont"
            }
        ]
    },
    {
        "titulo": 1,
        "resumen": 1,
        "_id": 0
    }
)

// 7. Aplicar consultas con expresiones regulares (mínimo 5)
// Buscar las películas que empiezen con la letra c, sin importar mayúscula o
// minúscula
db.peliculas.find(
    {
        "titulo": /^c/i
    }
)

// Buscar los comentarios que incluyan la palabra enfermaron
db.comentarios.find(
    {
        "comentario": /enfermaron/
    }
)

// Mostrar los usuarios que tengan el apellido Stark
db.usuarios.find(
    {
        "nombre": /^[\w\d]* stark/i
    }
)

// Mostrar las películas que incluyan a actores que se llamen Robert
db.peliculas.find(
    {
        "actores.lista": /^robert/i
    }
)

// Mostrar los comentarios que tengan al menos 400 carácteres
db.comentarios.find(
    {
        "comentario": /^[\s\S]{400,}/
    }
)

// 8. Generar consultas que contengan:
// a. Operadores lógicos
// Buscar la película Interstellar y Ciudad de Dios, mostrar el título y
// géneros de las películas
db.peliculas.find(
    {
        $or: [
            {
                "titulo": "Interstellar"
            },
            {
                "titulo": "Ciudad de dios"
            }
        ]
    },
    {
        "titulo": 1,
        "generos": 1,
        "_id": 0
    }
)

// b. Expresiones regulares
// Mostrar los usuarios en que su correo termine en .es
db.usuarios.find(
    {
        "correo": /\.es$/
    },
    {
        "nombre": 1,
        "correo": 1,
        "contraseña": 1,
        "_id": 0
    }
)

// 9. Generar una estadística de consultas donde exista índices compuestos
db.comentarios
    .find()
    .sort({
        "usuario.nombre": 1,
        "usuario.correo": 1
    })
    .explain('executionStats')

