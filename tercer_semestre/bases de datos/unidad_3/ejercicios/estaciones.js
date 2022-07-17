// Todas las estaciones de servicio que están en Angol
db.estaciones.find({
    "nombre_comuna": "Angol"
})

// Estaciones de servicio que son de la región de la Araucanía
db.estaciones.find(
    {
        "nombre_region": "De la Araucanía"
    },
    {
        "razon_social": 1,
        "direccion_calle": 1,
        "direccion_numero": 1,
        "distribuidor": 1,
        "precios": 1
    }
)

// Estaciones que aceptan cheques
db.estaciones.find(
    {
        "metodos_de_pago.cheque": true
    }
)

// Estaciones de servicio que son de la región de la Araucanía, aceptan medios
// de pago y el nombre del distribuidor es Shell
db.estaciones.find(
    {
        "nombre_region": "De la Araucanía",
        "metodos_de_pago.cheque": true,
        "distribuidor.nombre": "Shell"
    },
    {
        "razon_social": 1,
        "nombre_comuna": 1,
        "nombre_region": 1,
        "distribuidor": 1,
        "precios": 1
    }
)

// Estaciones de servicio que tienen farmacia o son autoservicio
db.estaciones.find(
    {
        $or: [
            { "servicios.farmacia": true },
            { "servicios.autoservicio": true }
        ]
    },
    {
        "razon_social": 1,
        "nombre_comuna": 1,
        "nombre_region": 1,
        "distribuidor": 1,
        "precios": 1
    }
)

// Estaciones de servicio que el nombre del distribuidor es Copec, son de la
// comuna de Providencia y el precio de la gasolina 93 vale menos de 1200
db.estaciones.find(
    {
        "distribuidor.nombre": "Copec",
        "nombre_comuna": "Providencia",
        "precios.gasolina 93": { $lt: 1200 }
    },
    {
        "razon_social": 1,
        "nombre_comuna": 1,
        "nombre_region": 1,
        "distribuidor": 1,
        "precios": 1
    }
)

// Estaciones de servicio que el nombre Copec o es Shell, el precio de diesel
// vale menos de 820 y aceptan cheques
db.estaciones.find(
    {
        $or: [
            { "distribuidor.nombre": "Copec" },
            { "distribuidor.nombre": "Shell" }
        ],
        "precios.petroleo diesel": { $lt: 1000 },
        "metodos_de_pago.cheque": true
    }
).count()

// Charlotte
db.estaciones.find(
    {
        $and: [
            {
                "distribuidor.nombre": "Shell",
                "distribuidor.nombre": "Copec"
            },
            { "metodos_de_pago.cheque": true },
            { "precios.petroleo diesel": { $lt: 1000 } }
        ]
    }
).count()

db.estaciones.find(
    {
        $and: [
            {
                $or: [
                    { "distribuidor.nombre": "Shell" },
                    { "distribuidor.nombre": "Copec" }
                ]
            },
            { "metodos_de_pago.cheque": true },
            { "precios.petroleo diesel": { $lt: 1000 } }
        ]
    }
).count()
