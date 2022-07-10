// Crear la base de datos curso
use('curso');

// Ejercicios guía 9

// Ejecute el archivo txt
// Ya está hecho, era insertar los datos

// Insertar cuatro documentos adicionales
db.alumnos.insertMany([
    {
        nombre: 'Gabriel',
        cursos: [
            { tema: 'Python', nota: 7 },
            { tema: 'Go', nota: 7 },
            { tema: 'OwOscript', nota: 7 },
            { tema: 'C++', nota: 7 },
        ],
        edad: 45,
        ciudad: [
            { nombre: 'Santa Barbara', tiempo: 109 }
        ]
    },
    {
        nombre: 'Hanna',
        cursos: [
            { tema: 'Owoscript', nota: 7 },
            { tema: 'Uwuscript', nota: 4 },
            { tema: 'Ewescript', nota: 3 },
            { tema: 'Awascript', nota: 2 },
        ],
        edad: 19,
        ciudad: [
            { nombre: 'Japon', tiempo: 1 }
        ]
    },
    {
        nombre: 'Juan',
        cursos: [
            { tema: 'Python', nota: 6 },
            { tema: 'Go', nota: 7 },
            { tema: 'Owoscript', nota: 4 },
            { tema: 'C++', nota: 3 },
        ],
        edad: 45,
        ciudad: [
            { nombre: 'Angol', tiempo: 6 }
        ]
    },
    {
        nombre: 'Mariajuana',
        cursos: [
            { tema: 'Python', nota: 7 },
            { tema: 'Uwusc', nota: 3 },
            { tema: 'Ewescript', nota: 4 },
            { tema: 'Awascript', nota: 7 },
        ],
        edad: 19,
        ciudad: [
            { nombre: 'Estados Unidos', tiempo: 10 }
        ]
    }
])

// Consultas
// Presentar el nombre del o los alumnos que tengan el ramo de JAVA.
db.alumnos.find(
    {
        "cursos": {
            $elemMatch: {
                "tema": "JAVA"
            }
        }
    },
    {
        "nombre": true,
        "_id": false
    }
)

// Presentar el nombre del o los alumnos que tomen PHP
db.alumnos.find(
    {
        "cursos": {
            $elemMatch: {
                "tema": "PHP"
            }
        }
    },
    {
        "nombre": true,
        "_id": false
    }
)

// Presentar el nombre del o los alumnos que tengan una nota mayor a 4
db.alumnos.find(
    {
        "cursos": {
            $elemMatch: {
                "nota": {
                    $gt: 4
                }
            }
        }
    },
    {
        "nombre": true,
        "_id": false
    }
)

// Presentar el nombre del o los alumnos que cursen JAVA y sean de la ciudad de
// Concepción
db.alumnos.find(
    {
        "cursos": {
            $elemMatch: {
                "tema": "JAVA"
            }
        },
        "ciudad": {
            $elemMatch: {
                "nombre": "Concepcion"
            }
        }
    },
    {
        "nombre": true,
        "_id": false
    }
)

// Presentar el nombre del o los alumnos que cursen PHP y su nota esté entre un
// 2 y un 6
db.alumnos.find(
    {
        "cursos": {
            $elemMatch: {
                "tema": "PHP",
                "nota": {
                    $gte: 2
                },
                "nota": {
                    $lte: 6
                }
            }
        }
    },
    {
        "nombre": true,
        "_id": false
    }
)

// Presentar el nombre del o los alumnos que cursen PHP y que tengan una edad
// mayor a 25 y menor o igual a 30, además que vivan en Concepción
db.alumnos.find(
    {
        "cursos": {
            $elemMatch: {
                "tema": "PHP",
            }
        },
        "edad": {
            $gt: 25,
            $lte: 30,
        },
        "ciudad": {
            $elemMatch: {
                "nombre": "Concepcion",
            }
        }

    },
    {
        "nombre": true,
        "_id": false,
    }
)


// Presentar el nombre del curso que cursan los alumnos que tengan una edad
// mayor o igual a 23 y menor que 30
db.alumnos.find(
    {
        "edad": {
            $gte: 23,
            $lt: 30,
        }
    },
    {
        "cursos.tema": true,
        "_id": false
    }
)

// Presentar el nombre del o los alumnos y el nombre del curso, de aquellos que
// vivan en Chillan
db.alumnos.find(
    {
        "ciudad": {
            $elemMatch: {
                "nombre": "Chillan"
            }
        }

    },
    {
        "nombre": true,
        "_id": false,
        "cursos.tema": true
    }
)

// A Matías se le actualizó su nota de su curso a un 6
db.alumnos.updateMany(
    {
        "nombre": "Matias"
    },
    {
        $set: {
            "cursos.0.nota": 6
        }
    }
)

// Se actualizó el curso que tomo Marcelo, el curso era PHP
db.alumnos.updateMany(
    {
        "nombre": "Marcelo"
    },
    {
        $set: {
            "cursos.2.tema": "go"
        }
    }
)

// Ejercicios guía 10

// Mostrar el nombre del o los alumnos que tienen tres cursos
db.alumnos.find(
    {
        "cursos": {
            $size: 3,
        }
    },
    {
        "nombre": true,
        "_id": false
    }
)

// Actualizar la nota del segundo curso a 5
db.alumnos.updateMany(
    {},
    {
        $set: {
            "cursos.1.nota": 5,
        }
    }
)

// Actualizar la nota del cuarto curso de Ana a 6
db.alumnos.updateOne(
    {
        "nombre": "Ana"
    },
    {
        $set: {
            "cursos.3.nota": 6,
        }
    }
)

// Actualizar la segunda ciudad de Julia a Concepción
db.alumnos.updateOne(
    {
        "nombre": "Julia"
    },
    {
        $set: {
            "ciudad.1.nombre": "Concepcion"
        }
    }
)

// Mostrar el nombre del o los alumnos que su segundo curso es PHP
db.alumnos.find(
    {
        "cursos.1.tema": "PHP"
    },
    {
        "nombre": true,
        "_id": false
    }
)

// Mostrar los cursos de Julia
db.alumnos.find(
    {
        "nombre": "Julia"
    },
    {
        "cursos.tema": true,
        "_id": false
    }
)


// Quitar el curso de Cobol a Ana
db.alumnos.updateOne(
    {
        "nombre": "Ana"
    },
    {
        $pull: {
            "cursos": {
                "tema": "Cobol"
            }
        }
    }
)

// Agregar la ciudad de Santiago y tiempo 24 a Pablo
db.alumnos.updateOne(
    {
        "nombre": "Pablo"
    },
    {
        $push: {
            "ciudad": {
                "nombre": "Santiago",
                "tiempo": 24
            }
        }
    }
)

