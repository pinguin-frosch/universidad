use('equipo');
db.trabajador.insertMany([
  {
    nombre: "Luis",
    cursos: [
      { tema: "PHP", nota: 4 },
      { tema: "C#", nota: 6 },
      { tema: "Cobol", nota: 7 },
      { tema: "PYTHON", nota: 5 }
    ],
    edad: 25,
    ciudad: [
      { nombre: "Concepcion", tiempo: 16 }
    ],
    bono: [200, 500, 400]
  },
  {
    nombre: "Pablo",
    cursos: [
      { tema: "C#", nota: 7 },
      { tema: "PYTHON", nota: 6 },
      { tema: "Cobol", nota: 4 }
    ],
    edad: 27,
    ciudad: [
      { nombre: "Chillán", tiempo: 16 }
    ],
    bono: [100, 500, 200]
  },
  {
    nombre: "Maria",
    cursos: [
      { tema: "PHP", nota: 2 },
      { tema: "JAVA", nota: 4 },
      { tema: "Cobol", nota: 4 }
    ],
    edad: 30,
    ciudad: [
      { nombre: "Concepcion", tiempo: 16 },
      { nombre: "Temuco", tiempo: 10 }
    ],
    bono: [250, 500, 400]
  },
  {
    nombre: "Ana",
    cursos: [
      { tema: "JAVA", nota: 3 },
      { tema: "JS", nota: 5 },
      { tema: "PHP", nota: 4 },
      { tema: "Cobol", nota: 4 }
    ],
    edad: 35,
    Ciudad: "Talcahuano",
    bono: [250, 500, 600]
  },
  {
    nombre: "Matias",
    cursos: [
      { tema: "JS", nota: 4 },
      { tema: "PHP", nota: 6 },
      { tema: "C#", nota: 6 }
    ],
    edad: 26,
    ciudad: "Concepcion",
    bono: [250, 300, 400]
  },
  {
    nombre: "Mariano",
    cursos: [
      { tema: "JAVA", nota: 7 },
      { tema: "PHP", nota: 5 },
      { tema: "Cobol", nota: 4 },
      { tema: "PYTHON", nota: 4 }
    ],
    edad: 28,
    ciudad: "Concepción",
    bono: [250, 500, 400]
  },
  {
    nombre: "Sofia",
    cursos: [
      { tema: "PHP", nota: 7 },
      { tema: "C#", nota: 6 },
      { tema: "Cobol", nota: 4 }
    ],
    edad: 26,
    ciudad: [
      { nombre: "Chillan", tiempo: 12 },
      { nombre: "Temuco", tiempo: 9 }
    ],
    bono: [250, 500, 400]
  },
  {
    nombre: "Marcelo",
    cursos: [
      { tema: "C#", nota: 6 },
      { tema: "JAVA", nota: 5 },
      { tema: "JS", nota: 4 }
    ],
    edad: 23,
    ciudad: "Chillan",
    bono: [250, 500, 400]
  },
  {
    nombre: "Sonia",
    cursos: [
      { tema: "PHP", nota: 4 },
      { tema: "JAVA", nota: 4 },
      { tema: "Cobol", nota: 4 }
    ],
    edad: 27,
    ciudad: [
      { nombre: "Concepcion", tiempo: 6 },
      { nombre: "Temuco", tiempo: 4 }
    ],
    bono: [250, 600, 800]
  },
  {
    nombre: "Sonia",
    cursos: [
      { tema: "JAVA", nota: 7 },
      { tema: "JS", nota: 5 },
      { tema: "PYTHON", nota: 4 },
      { tema: "Cobol", nota: 4 }
    ],
    edad: 23,
    ciudad: "Concepción",
    bono: [250, 500, 400, 800]
  },
  {
    nombre: "Julia",
    cursos: [
      { tema: "PYTHON", nota: 7 },
      { tema: "PYTHON", nota: 7 }
    ],
    edad: 24,
    ciudad: [
      { nombre: "Chillán", tiempo: 16 },
      { nombre: "Temuco", tiempo: 10 }
    ],
    bono: [250, 500, 400]
  }
]);

// 1.Mostrar el nombre del o los alumnos que tienen el curso de PYTHON.
db.trabajador.find(
  {
    "cursos": {
      $elemMatch: {
        "tema": "PYTHON"
      }
    }
  },
  {
    "nombre": 1,
    "_id": 0
  }
)

// 2.Actualizar la nota del curso C# a 7.
db.trabajador.updateMany(
  {
    "cursos": {
      $elemMatch: {
        "tema": "C#"
      }
    }
  },
  {
    $set: {
      "cursos.$.nota": 7
    }
  }
)

// 3.Agregar el curso de PB a todos los alumnos y su nota por ahora es 1.
db.trabajador.updateMany(
  {},
  {
    $push: {
      "cursos": {
        "tema": "PB",
        "nota": 1
      }
    }
  }
)

// 4.Actualizar la nota de Matias y Sofia a un 5, en el curso de PB
db.trabajador.updateMany(
  {
    $or: [
      { "nombre": "Matias" },
      { "nombre": "Sofia" }
    ],
    "cursos": {
      $elemMatch: {
        "tema": "PB"
      }
    }
  },
  {
    $set: {
      "cursos.$.nota": 5
    }
  }
)

// 5.Mostrar el nombre del o los alumnos que tiene un bono de 250.
db.trabajador.find(
  {
    "bono": {
      $all: [
        250
      ]
    }
  },
  {
    "nombre": 1,
    "_id": 0
  }
)

// 6.Mostrar el nombre del o los alumnos que cursaron el curso de JAVA y Cobol,
// además pueden vivir en la ciudad de Concepción o Temuco.
db.trabajador.find(
  {
    $and: [
      {
        "cursos": {
          $elemMatch: {
            "tema": "JAVA"
          }
        }
      },
      {
        "cursos": {
          $elemMatch: {
            "tema": "Cobol"
          }
        }
      }
    ],
    $or: [
      {
        "ciudad": {
          $elemMatch: {
            "nombre": "Concepcion"
          }
        }
      },
      {
        "ciudad": {
          $elemMatch: {
            "nombre": "Temuco"
          }
        }
      }
    ]
  }
)

// 7.Borrar el alumno Luis.
db.trabajador.deleteOne(
  {
    "nombre": "Luis"
  }
)

// 8.Mostrar el nombre del o los alumnos que poseen cuatro bonos
db.trabajador.find(
  {
    "bono": {
      $size: 4
    }
  },
  {
    "nombre": true,
    "_id": false
  }
)

// 9.Mostrar el nombre del o los alumnos que sean de la ciudad de Concepción o
// Chillán y además tengan una edad mayor a 27 y menor a 35, incluidas ambas
db.trabajador.find(
  {
    $or: [
      {
        "ciudad": {
          $elemMatch: {
            "nombre": "Concepcion"
          }
        }
      },
      {
        "ciudad": {
          $elemMatch: {
            "nombre": "Chillán"
          }
        }
      }
    ],
    edad: {
      $gte: 27,
      $lte: 35
    }
  },
  {
    "nombre": true,
    "_id": false
  }
)

// 10.Mostrar el nombre del o los alumnos que cursaron el curso de JAVA o JS,
// ordenado de manera descendente.
db.trabajador.find(
  {
    $or: [
      {
        "cursos": {
          $elemMatch: {
            "tema": "JS"
          }
        }
      },
      {
        "cursos": {
          $elemMatch: {
            "tema": "JAVA"
          }
        }
      }
    ]
  }
).sort({"nombre":1})

// 11.Generar un ejemplo con la instrucción unset.
// Borrar la nota de PB para todos los usuarios
db.trabajador.updateMany(
  {
    "cursos": {
      $elemMatch: {
        "tema": "PB"
      }
    }
  },
  {
    $unset: {
      "cursos.$.nota": ""
    }
  }
)

// Espero te sirvan uwu
