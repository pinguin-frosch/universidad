// Todas las estaciones de servicio cuyo distribuidor sea al inicio la letra
// "s" (sin importar mayúscula o minúscula)
db.estaciones.find({ "distribuidor.nombre": { $regex: "^s", $options: "i" } })

// Todas las estaciones de servicio cuyo nombre de ciudad finalice con la letra
// "L" sin importar mayúscula o minúscula
db.estaciones.find({ "distribuidor.nombre": { $regex: "l$", $options: "i" } })

// Todas las estaciones de servicio cuyo distribuidor contenga la letra "o" y
// el inicio del nombre de la comuna sea "P" (sin importar mayúscula o
// minúscula)
db.estaciones.find({
    "distribuidor.nombre": { $regex: "o", $options: "i" },
    "nombre_comuna": { $regex: "^p", $options: "i" }
})

// Todas las estaciones de servicio cuya razón social contenga la letra "i" y
// el inicio del nombre de la comuna sea 'A' (sin importar mayúscula o
// minúscula)
db.estaciones.find({
    "razon_social": { $regex: "i", $options: "i" },
    "nombre_comuna": { $regex: "^a", $options: "i" }
})

// Todas las estaciones de servicio cuyo distribuidor contenga al inicio la
// letra "c" y finalice con la letra "s" (sin importar mayúscula o minúscula),
// y que el nombre de la comuna inicie con la letra "P" (sin importar mayúscula
// o minúscula)
// Opción 1, interpretación literal
db.estaciones.find({
    "distribuidor.nombre": { $regex: "^c.*s$", $options: "i" },
    "nombre_comuna": { $regex: "^p", $options: "i" },
})
// Opción 2, cambiar el y por o en la expresión regular
db.estaciones.find({
    $or: [
        { "distribuidor.nombre": { $regex: "^c", $options: "i" } },
        { "distribuidor.nombre": { $regex: "s$", $options: "i" } }
    ],
    "nombre_comuna": { $regex: "^p", $options: "i" },
})

// Todas la estaciones de servicio cuyo distribuidor contenga al inicio la
// letra "P" y finalice con la letra "c" (sin importar mayúscula y minúscula) y
// que el nombre de la comuna inicie con la letra "P" (sin importar mayúscula o
// minúscula) y que finalice con la letra "a" (sin importar mayúscula o
// minúscula)
// Opción 1, interpretación literal
db.estaciones.find({
    "distribuidor.nombre": { $regex: "^p.*c$", $options: "i" },
    "nombre_comuna": { $regex: "^p.*a$", $options: "i" },
})

// Opción 2, cambiar el y por o en la expresión regular
// FIXME: NO es posible usar $and implícito si hay varios $or en la consulta,
// estamos incluyendo resultados que no queremos, la consulta siguiente lo
// soluciona y se puede ver con la cantidad de resultados, también si alguien
// quiere los puede revisar manualmente.
db.estaciones.find({
    $or: [
        { "distribuidor.nombre": { $regex: "^p", $options: "i" } },
        { "distribuidor.nombre": { $regex: "c$", $options: "i" } }
    ],
    $or: [

        { "nombre_comuna": { $regex: "^p", $options: "i" } },
        { "nombre_comuna": { $regex: "a$", $options: "i" } }
    ]
}).count()

// Versión corregida
db.estaciones.find({
    $and: [
        {
            $or: [
                { "distribuidor.nombre": { $regex: "^p", $options: "i" } },
                { "distribuidor.nombre": { $regex: "c$", $options: "i" } }
            ]
        },
        {
            $or: [
                { "nombre_comuna": { $regex: "^p", $options: "i" } },
                { "nombre_comuna": { $regex: "a$", $options: "i" } }
            ]
        }
    ]
}).count()

// Todas las estaciones de servicio cuyo distribuidor sea "Shell" o "HN" sin
// importar mayúscula o minúscula, que pertenezcan a la comuna de los ángeles y
// el precio de venta sea menor que 1039 y que la razón social inicie con la
// letra "C" o "P" sin importar mayúscula o minúscula
db.estaciones.find({
    $or: [
        { "distribuidor.nombre": { $regex: "shell", $options: "i" } },
        { "distribuidor.nombre": { $regex: "copec", $options: "i" } }
    ],
    "nombre_comuna": { $regex: "los [aá]ngeles", $options: "i" },
    "precios.gasolina 93": { $lt: 1039 },
    "razon_social": { $regex: "^[cp]", $options: "i" }
})

// Todas las estaciones de servicio cuyo distribuidor sea "Shell" o "HN" o
// "Copec" sin importar mayúscula o minúscula, que pertenezcan a una comuna que
// inice con la letra "s" y el precio de venta de la gasolina 93 sea menor que
// 1035 y que la razon social inicie con la letra "I" o "H" o "C" sin importar
// mayúscula o minúscula
db.estaciones.find({
    $or: [
        { "distribuidor.nombre": { $regex: "shell", $options: "i" } },
        { "distribuidor.nombre": { $regex: "copec", $options: "i" } },
        { "distribuidor.nombre": { $regex: "hn", $options: "i" } }
    ],
    "nombre_comuna": { $regex: "^s", $options: "i" },
    "precios.gasolina 93": { $lt: 1300 },
    $or: [
        { "razon_social": { $regex: "^i", $options: "i" } },
        { "razon_social": { $regex: "^h", $options: "i" } },
        { "razon_social": { $regex: "^c", $options: "i" } }
    ]
}).count()

// Interesante: la opción anterior no funciona, al parecer el $and implícito no
// funciona si hay más de un $or dentro de la expresión. Con la expresión
// anterior hay 6 resultado que no deberían estar ahí, como petrobras entre
// otros. Si hay más de un $or debemos usar un $and explícito.
db.estaciones.find({
    $and: [
        {
            $or: [
                { "distribuidor.nombre": { $regex: "shell", $options: "i" } },
                { "distribuidor.nombre": { $regex: "copec", $options: "i" } },
                { "distribuidor.nombre": { $regex: "hn", $options: "i" } }
            ]
        },
        { "nombre_comuna": { $regex: "^s", $options: "i" } },
        { "precios.gasolina 93": { $lt: 1300 } },
        {
            $or: [
                { "razon_social": { $regex: "^i", $options: "i" } },
                { "razon_social": { $regex: "^h", $options: "i" } },
                { "razon_social": { $regex: "^c", $options: "i" } }
            ]
        }
    ]
}).count()

// Se solicita aumentar en un 5% el precio de venta de todas las estaciones de
// servicio cuyo distribuidor inicie con la letra "S" sin importar mayúscula o
// minúscula, que esté en las regiones que contenga la letra "b"
// HINT: No se me ocurre como hacer esto, porque necesito los nombres de los
// combustibles y podrían ser varios, creo que lo mejor es usar $aggregate para
// saber los nombres de los combustibles y luego modificar cada uno
db.estaciones.aggregate([
    {
        $project: {
            "data": {
                $objectToArray: "$precios"
            }
        }
    },
    {
        $project: {
            "data": "$data.k"
        }
    },
    {
        $unwind: "$data"
    },
    {
        $group: {
            "_id": null,
            keys: {
                $addToSet: "$data"
            }
        }
    }
])

// gnc
db.estaciones.updateMany(
    {
        "distribuidor.nombre": { $regex: "^s", $options: "i" },
        "nombre_region": { $regex: "b", $options: "i" },
        "precios.gnc": { $exists: true }
    },
    {
        $mul: {
            "precios.gnc": 1.05
        }
    }
)
// Se actualizaron 0 documentos

// gasolina 93
db.estaciones.updateMany(
    {
        "distribuidor.nombre": { $regex: "^s", $options: "i" },
        "nombre_region": { $regex: "b", $options: "i" },
        "precios.gasolina 93": { $exists: true }
    },
    {
        $mul: {
            "precios.gasolina 93": 1.05
        }
    }
)
// Se actualizaron 147 documentos

// gasolina 95
db.estaciones.updateMany(
    {
        "distribuidor.nombre": { $regex: "^s", $options: "i" },
        "nombre_region": { $regex: "b", $options: "i" },
        "precios.gasolina 95": { $exists: true }
    },
    {
        $mul: {
            "precios.gasolina 95": 1.05
        }
    }
)
// Se actualizaron 148 documentos

// gasolina 97
db.estaciones.updateMany(
    {
        "distribuidor.nombre": { $regex: "^s", $options: "i" },
        "nombre_region": { $regex: "b", $options: "i" },
        "precios.gasolina 97": { $exists: true }
    },
    {
        $mul: {
            "precios.gasolina 97": 1.05
        }
    }
)
// Se actualizaron 114 documentos

// glp vehicular
db.estaciones.updateMany(
    {
        "distribuidor.nombre": { $regex: "^s", $options: "i" },
        "nombre_region": { $regex: "b", $options: "i" },
        "precios.glp vehicular": { $exists: true }
    },
    {
        $mul: {
            "precios.glp vehicular": 1.05
        }
    }
)
// Se actualizaron 3 documentos

// Creamos un índice compuesto para razon_social, nombre_comuna,
// distribuidor.nombre y precios.gasolina 93
db.estaciones.createIndex({
    "distribuidor.nombre": 1,
    "nombre_comuna": 1,
    "razon_social": 1,
    "precios.gasolina 93": 1
})

// Podemos verificar que se creó con db.coleccion.getIndices()
db.estaciones.getIndices()

// Crear un índice para id, con la restricción de ser único
db.estaciones.createIndex({ "id": 1 }, { "unique": true })

// Insertar un documento con id repetido para que el índice lo impida
db.estaciones.insertOne({
    "id": "co110101"
})

// Crear un índice compuesto a libre elección de al menos dos propiedades. Los
// índices deberían ser usados para las columnas que sean más accedidas, ya aue
// agregarlos a todas partes tendrá impacto en el rendimiento y no será muy
// útil. En base a los ejemplos se usa mucho distribuidor.nombre junto a
// nombre_comuna, así que haré un índice con esa combinación y luego realizar
// una comparación.
db.estaciones.createIndex({
    "distribuidor.nombre": 1,
    "nombre_comuna": 1
})

// Ejercicio con el cual comparar
db.estaciones.find({
    $and: [
        {
            $or: [
                { "distribuidor.nombre": { $regex: "^p", $options: "i" } },
                { "distribuidor.nombre": { $regex: "c$", $options: "i" } }
            ]
        },
        {
            $or: [
                { "nombre_comuna": { $regex: "^p", $options: "i" } },
                { "nombre_comuna": { $regex: "a$", $options: "i" } }
            ]
        }
    ]
}).explain('executionStats')

// Sin índice
// totalKeysExamined: 0,
// totalDocsExamined: 1812,

// Con índice
// totalKeysExamined: 1812,
// totalDocsExamined: 418,
