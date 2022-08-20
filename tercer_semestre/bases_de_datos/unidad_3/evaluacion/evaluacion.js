// Caso Practico 1 (Importar registros)
// Crear base de datos "registrosvarios"
use('registrosvarios')

// Crear colección usuarios
db.createCollection('usuarios')

// Importar desde jsonplaceholders la estructura json de users
// El siguiente comando fue ejecutado en la terminal, no en mongosh
// mongoimport --uri="mongodb://localhost/registrosvarios" --collection="usuarios" --drop --jsonArray users.json

// Caso Practico 2 (Eliminar registros)
// Eliminar al usuario cuyo username sea "Antonette"
db.usuarios.deleteOne(
    {
        "username": "Antonette"
    }
)

// Eliminar al usuario cuya ciudad sea "Bartholomebury"
db.usuarios.deleteOne(
    {
        "address.city": "Bartholomebury"
    }
)

// Caso Practico 3 (Actualizar registros)
// Agregar una columna de salary, asignar valor 12500 a todos aquellos usuarios
// cuyo nombre de compañía inicie con la letra R (Sin importar que se escriba
// en mayúscula o minúscula)
db.usuarios.updateMany(
    {},
    {
        $set: {
            "salary": 0
        }
    }
)
db.usuarios.updateMany(
    {
        "company.name": {
            $regex: "^r",
            $options: "i"
        }
    },
    {
        $set: {
            "salary": 12500
        }
    }
)

// Eliminar la columna "catchPhrase" (Se encuentra dentro de company) de todos
// los usuarios cuyo nombre de compañía comience con la letra "c" (Sin importar
// mayúscula o minúscula)
db.usuarios.updateMany(
    {
        "company.catchPhrase": {
            $regex: "^c",
            $options: "i"
        }
    },
    {
        $unset: {
            "company.catchPhrase": ""
        }
    }
)

// A todos los usuarios que trabajan en una compañía que inicie con la letra R
// (Sin importar mayúscula o minúscula) aumentar el sueldo en un 8%
db.usuarios.updateMany(
    {
        "company.name": {
            $regex: "^r",
            $options: "i"
        }
    },
    {
        $mul: {
            "salary": 1.08
        }
    }
)

// Caso Practico 4 (Índices)
// Crear índice único para la columna "username"
db.usuarios.createIndex(
    {
        "username": 1
    },
    {
        unique: true
    }
)

// Crear índices para las columnas "company.name" y "address.street"
db.usuarios.createIndex(
    {
        "company.name": 1,
        "address.street": 1
    }
)

// Añadir un documento y comprobar que no permita ingresar un mismo "username"
// (No es obligatorio ingresar las mismas cantidades de columnas)
db.usuarios.insertOne(
    {
        "username": "Karianne"
    }
)

// Realizar una consulta que muestre todos los nombres de empresas que inicien
// con la letra "c" o "k" y el nombre de la calle contenga la letra "o" en
// cualquier lugar (Debe mostrar estadística de documentos consultados)
db.usuarios.find(
    {
        "company.name": {
            $regex: "^[ck]",
            $options: "i"
        },
        "address.street": {
            $regex: "o"
        }
    }
).explain('executionStats')

// Respuesta
// {
//   explainVersion: '1',
//   queryPlanner: {
//     namespace: 'registrosvarios.usuarios',
//     indexFilterSet: false,
//     parsedQuery: {
//       '$and': [
//         { 'address.street': { '$regex': 'o' } },
//         { 'company.name': { '$regex': '^[ck]', '$options': 'i' } }
//       ]
//     },
//     maxIndexedOrSolutionsReached: false,
//     maxIndexedAndSolutionsReached: false,
//     maxScansToExplodeReached: false,
//     winningPlan: {
//       stage: 'FETCH',
//       inputStage: {
//         stage: 'IXSCAN',
//         filter: {
//           '$and': [
//             { 'company.name': { '$regex': '^[ck]', '$options': 'i' } },
//             { 'address.street': { '$regex': 'o' } }
//           ]
//         },
//         keyPattern: { 'company.name': 1, 'address.street': 1 },
//         indexName: 'company.name_1_address.street_1',
//         isMultiKey: false,
//         multiKeyPaths: { 'company.name': [], 'address.street': [] },
//         isUnique: false,
//         isSparse: false,
//         isPartial: false,
//         indexVersion: 2,
//         direction: 'forward',
//         indexBounds: {
//           'company.name': [ '["", {})', '[/^[ck]/i, /^[ck]/i]' ],
//           'address.street': [ '["", {})', '[/o/, /o/]' ]
//         }
//       }
//     },
//     rejectedPlans: []
//   },
//   executionStats: {
//     executionSuccess: true,
//     nReturned: 1,
//     executionTimeMillis: 2,
//     totalKeysExamined: 8,
//     totalDocsExamined: 1,
//     executionStages: {
//       stage: 'FETCH',
//       nReturned: 1,
//       executionTimeMillisEstimate: 0,
//       works: 9,
//       advanced: 1,
//       needTime: 7,
//       needYield: 0,
//       saveState: 0,
//       restoreState: 0,
//       isEOF: 1,
//       docsExamined: 1,
//       alreadyHasObj: 0,
//       inputStage: {
//         stage: 'IXSCAN',
//         filter: {
//           '$and': [
//             { 'company.name': { '$regex': '^[ck]', '$options': 'i' } },
//             { 'address.street': { '$regex': 'o' } }
//           ]
//         },
//         nReturned: 1,
//         executionTimeMillisEstimate: 0,
//         works: 9,
//         advanced: 1,
//         needTime: 7,
//         needYield: 0,
//         saveState: 0,
//         restoreState: 0,
//         isEOF: 1,
//         keyPattern: { 'company.name': 1, 'address.street': 1 },
//         indexName: 'company.name_1_address.street_1',
//         isMultiKey: false,
//         multiKeyPaths: { 'company.name': [], 'address.street': [] },
//         isUnique: false,
//         isSparse: false,
//         isPartial: false,
//         indexVersion: 2,
//         direction: 'forward',
//         indexBounds: {
//           'company.name': [ '["", {})', '[/^[ck]/i, /^[ck]/i]' ],
//           'address.street': [ '["", {})', '[/o/, /o/]' ]
//         },
//         keysExamined: 8,
//         seeks: 1,
//         dupsTested: 0,
//         dupsDropped: 0
//       }
//     }
//   },
//   command: {
//     find: 'usuarios',
//     filter: {
//       'company.name': { '$regex': '^[ck]', '$options': 'i' },
//       'address.street': { '$regex': 'o' }
//     },
//     '$db': 'registrosvarios'
//   },
//   serverInfo: {
//     host: 'archlinux',
//     port: 27017,
//     version: '5.0.9',
//     gitVersion: '6f7dae919422dcd7f4892c10ff20cdc721ad00e6'
//   },
//   serverParameters: {
//     internalQueryFacetBufferSizeBytes: 104857600,
//     internalQueryFacetMaxOutputDocSizeBytes: 104857600,
//     internalLookupStageIntermediateDocumentMaxSizeBytes: 104857600,
//     internalDocumentSourceGroupMaxMemoryBytes: 104857600,
//     internalQueryMaxBlockingSortMemoryUsageBytes: 104857600,
//     internalQueryProhibitBlockingMergeOnMongoS: 0,
//     internalQueryMaxAddToSetBytes: 104857600,
//     internalDocumentSourceSetWindowFieldsMaxMemoryBytes: 104857600
//   },
//   ok: 1
// }


// Caso Practico 5 (Consultas avanzadas collection estaciones (valores se
// obtienen desde API)) (estaciones.json está en plataforma)
use('cne')
db.createCollection('estaciones')
// El siguiente comando fue ejecutado en la terminal y no en mongosh
// mongoimport --uri="mongodb://localhost/cne" --collection="estaciones" --drop --jsonArray estaciones.json

// Se solicita realizar una consulta a libre elección que utilice operadores
// lógicos AND y OR
// Busca todas las estaciones en que (el nombre de comuna es "Iquique" y el
// nombre del distribuidor sea "Shell") o (que el nombre de la comuna sea "Los
// Ángeles y el nombre del distribuidor sea "Copec")
db.estaciones.find(
    {
        $or: [
            {
                $and: [
                    {
                        "nombre_comuna": "Iquique"
                    },
                    {
                        "distribuidor.nombre": "Shell"
                    }
                ]
            },
            {
                $and: [
                    {
                        "nombre_comuna": "Los Ángeles"
                    },
                    {
                        "distribuidor.nombre": "Copec"
                    }
                ]
            }
        ]
    }
)

// Respuesta
// [
//   {
//     _id: ObjectId("62cd86688363fa8782a6d07a"),
//     id: 'sh110103',
//     fecha_hora_actualizacion: '2022-01-27 10:17:56',
//     razon_social: 'Concesiones Benjamín Tomas Barros Donoso E.I.R.L.',
//     direccion_calle: 'Cespedes Gonzalez',
//     direccion_numero: '1685',
//     id_comuna: '01101',
//     nombre_comuna: 'Iquique',
//     id_region: '01',
//     nombre_region: 'Tarapacá',
//     horario_atencion: '24 horas',
//     distribuidor: {
//       nombre: 'Shell',
//       logo: 'http://api.cne.cl/brands/logo4.jpg',
//       logo_svg: 'http://api.cne.cl/brands/shell.svg',
//       logo_horizontal_svg: 'http://api.cne.cl/brands/shell-horizontal.svg'
//     },
//     precios: {
//       'gasolina 93': 1038,
//       'gasolina 97': 1074,
//       'petroleo diesel': 844,
//       'gasolina 95': 1057
//     },
//     metodos_de_pago: {
//       efectivo: true,
//       cheque: true,
//       'tarjetas bancarias': true,
//       'tarjetas grandes tiendas': false
//     },
//     ubicacion: { latitud: -20.2248568511, longitud: -70.140050053596 },
//     servicios: {
//       tienda: false,
//       farmacia: false,
//       mantencion: false,
//       autoservicio: false
//     }
//   },
//   {
//     _id: ObjectId("62cd86688363fa8782a6d07d"),
//     id: 'sh110105',
//     fecha_hora_actualizacion: '2022-01-27 10:00:42',
//     razon_social: 'Sociedad de Inversiones E & E SPA',
//     direccion_calle: 'Manuel Rodrï¿½guezVivar',
//     direccion_numero: '705',
//     id_comuna: '01101',
//     nombre_comuna: 'Iquique',
//     id_region: '01',
//     nombre_region: 'Tarapacá',
//     horario_atencion: '24 horas',
//     distribuidor: {
//       nombre: 'Shell',
//       logo: 'http://api.cne.cl/brands/logo4.jpg',
//       logo_svg: 'http://api.cne.cl/brands/shell.svg',
//       logo_horizontal_svg: 'http://api.cne.cl/brands/shell-horizontal.svg'
//     },
//     precios: {
//       'gasolina 93': 1040,
//       'gasolina 97': 1076,
//       'petroleo diesel': 846,
//       'gasolina 95': 1059
//     },
//     metodos_de_pago: {
//       efectivo: true,
//       cheque: false,
//       'tarjetas bancarias': true,
//       'tarjetas grandes tiendas': false
//     },
//     ubicacion: { latitud: -20.223565710715, longitud: -70.149102509022 },
//     servicios: {
//       tienda: true,
//       farmacia: false,
//       mantencion: false,
//       autoservicio: false
//     }
//   },
//   {
//     _id: ObjectId("62cd86688363fa8782a6d07e"),
//     id: 'sh110104',
//     fecha_hora_actualizacion: '2022-01-27 10:06:33',
//     razon_social: 'Climex chile spa',
//     direccion_calle: 'Genaro Gallo',
//     direccion_numero: '2361',
//     id_comuna: '01101',
//     nombre_comuna: 'Iquique',
//     id_region: '01',
//     nombre_region: 'Tarapacá',
//     horario_atencion: '24 horas',
//     distribuidor: {
//       nombre: 'Shell',
//       logo: 'http://api.cne.cl/brands/logo4.jpg',
//       logo_svg: 'http://api.cne.cl/brands/shell.svg',
//       logo_horizontal_svg: 'http://api.cne.cl/brands/shell-horizontal.svg'
//     },
//     precios: {
//       'gasolina 93': 1033,
//       'gasolina 97': 1071,
//       'petroleo diesel': 840,
//       'gasolina 95': 1053
//     },
//     metodos_de_pago: {
//       efectivo: true,
//       cheque: false,
//       'tarjetas bancarias': true,
//       'tarjetas grandes tiendas': false
//     },
//     ubicacion: { latitud: -20.231584198604, longitud: -70.137767493725 },
//     servicios: {
//       tienda: false,
//       farmacia: false,
//       mantencion: false,
//       autoservicio: true
//     }
//   },
//   {
//     _id: ObjectId("62cd86688363fa8782a6d08f"),
//     id: 'sh110102',
//     fecha_hora_actualizacion: '2022-01-27 10:04:49',
//     razon_social: 'CLIMEX CHILE SPA',
//     direccion_calle: 'Avda. Arturo Prat',
//     direccion_numero: '1850',
//     id_comuna: '01101',
//     nombre_comuna: 'Iquique',
//     id_region: '01',
//     nombre_region: 'Tarapacá',
//     horario_atencion: '24 horas',
//     distribuidor: {
//       nombre: 'Shell',
//       logo: 'http://api.cne.cl/brands/logo4.jpg',
//       logo_svg: 'http://api.cne.cl/brands/shell.svg',
//       logo_horizontal_svg: 'http://api.cne.cl/brands/shell-horizontal.svg'
//     },
//     precios: {
//       'gasolina 93': 1040,
//       'gasolina 97': 1076,
//       'petroleo diesel': 846,
//       'gasolina 95': 1059
//     },
//     metodos_de_pago: {
//       efectivo: true,
//       cheque: false,
//       'tarjetas bancarias': true,
//       'tarjetas grandes tiendas': false
//     },
//     ubicacion: { latitud: -20.242222024877, longitud: -70.142480134964 },
//     servicios: {
//       tienda: true,
//       farmacia: false,
//       mantencion: false,
//       autoservicio: true
//     }
//   },
//   {
//     _id: ObjectId("62cd86688363fa8782a6d09e"),
//     id: 'sh110101',
//     fecha_hora_actualizacion: '2022-01-27 16:46:09',
//     razon_social: 'INVERSIONES ISP SPA.',
//     direccion_calle: 'OHiggins',
//     direccion_numero: '2280',
//     id_comuna: '01101',
//     nombre_comuna: 'Iquique',
//     id_region: '01',
//     nombre_region: 'Tarapacá',
//     horario_atencion: '07.30 HRAS HASTA  23.30 H',
//     distribuidor: {
//       nombre: 'Shell',
//       logo: 'http://api.cne.cl/brands/logo4.jpg',
//       logo_svg: 'http://api.cne.cl/brands/shell.svg',
//       logo_horizontal_svg: 'http://api.cne.cl/brands/shell-horizontal.svg'
//     },
//     precios: {
//       'gasolina 93': 1038,
//       'gasolina 97': 1074,
//       'petroleo diesel': 836,
//       'gasolina 95': 1057
//     },
//     metodos_de_pago: {
//       efectivo: true,
//       cheque: true,
//       'tarjetas bancarias': true,
//       'tarjetas grandes tiendas': false
//     },
//     ubicacion: { latitud: -20.219516041031, longitud: -70.13424038887 },
//     servicios: {
//       tienda: false,
//       farmacia: false,
//       mantencion: true,
//       autoservicio: true
//     }
//   },
//   {
//     _id: ObjectId("62cd86688363fa8782a6d390"),
//     id: 'co830101',
//     fecha_hora_actualizacion: '2022-01-27 08:49:49',
//     razon_social: 'sociedad de inversiones stevens ltda',
//     direccion_calle: 'AV. GABRIELA MISTRAL',
//     direccion_numero: '1625',
//     id_comuna: '08301',
//     nombre_comuna: 'Los Ángeles',
//     id_region: '08',
//     nombre_region: 'Del Biobío',
//     horario_atencion: '24 horas',
//     distribuidor: {
//       nombre: 'Copec',
//       logo: 'http://api.cne.cl/brands/logo5.jpg',
//       logo_svg: 'http://api.cne.cl/brands/copec.svg',
//       logo_horizontal_svg: 'http://api.cne.cl/brands/copec-horizontal.svg'
//     },
//     precios: {
//       'gasolina 93': 1037,
//       'gasolina 97': 1065,
//       'petroleo diesel': 837,
//       'gasolina 95': 1051
//     },
//     metodos_de_pago: {
//       efectivo: true,
//       cheque: false,
//       'tarjetas bancarias': true,
//       'tarjetas grandes tiendas': true
//     },
//     ubicacion: { latitud: -37.47364687002, longitud: -72.329231500626 },
//     servicios: {
//       tienda: false,
//       farmacia: false,
//       mantencion: true,
//       autoservicio: false
//     }
//   },
//   {
//     _id: ObjectId("62cd86688363fa8782a6d391"),
//     id: 'co830102',
//     fecha_hora_actualizacion: '2022-01-27 08:40:39',
//     razon_social: 'VELOSO S.A.',
//     direccion_calle: 'RUTA PANAMERICANA SUR KM. 506',
//     direccion_numero: '0',
//     id_comuna: '08301',
//     nombre_comuna: 'Los Ángeles',
//     id_region: '08',
//     nombre_region: 'Del Biobío',
//     horario_atencion: '24 horas',
//     distribuidor: {
//       nombre: 'Copec',
//       logo: 'http://api.cne.cl/brands/logo5.jpg',
//       logo_svg: 'http://api.cne.cl/brands/copec.svg',
//       logo_horizontal_svg: 'http://api.cne.cl/brands/copec-horizontal.svg'
//     },
//     precios: {
//       'gasolina 93': 1039,
//       'gasolina 97': 1068,
//       'petroleo diesel': 837,
//       'gasolina 95': 1050
//     },
//     metodos_de_pago: {
//       efectivo: true,
//       cheque: true,
//       'tarjetas bancarias': true,
//       'tarjetas grandes tiendas': true
//     },
//     ubicacion: { latitud: -37.441975895501, longitud: -72.327439785004 },
//     servicios: {
//       tienda: false,
//       farmacia: false,
//       mantencion: false,
//       autoservicio: false
//     }
//   },
//   {
//     _id: ObjectId("62cd86688363fa8782a6d392"),
//     id: 'co830103',
//     fecha_hora_actualizacion: '2022-01-27 10:00:10',
//     razon_social: 'Sociedad Comercial ALUN Limitada',
//     direccion_calle: 'KM 18 CAMINO ANTUCO',
//     direccion_numero: '0',
//     id_comuna: '08301',
//     nombre_comuna: 'Los Ángeles',
//     id_region: '08',
//     nombre_region: 'Del Biobío',
//     horario_atencion: '24 horas',
//     distribuidor: {
//       nombre: 'Copec',
//       logo: 'http://api.cne.cl/brands/logo5.jpg',
//       logo_svg: 'http://api.cne.cl/brands/copec.svg',
//       logo_horizontal_svg: 'http://api.cne.cl/brands/copec-horizontal.svg'
//     },
//     precios: {
//       'gasolina 93': 1039,
//       'gasolina 97': 1068,
//       'petroleo diesel': 836,
//       'gasolina 95': 1053
//     },
//     metodos_de_pago: {
//       efectivo: true,
//       cheque: true,
//       'tarjetas bancarias': true,
//       'tarjetas grandes tiendas': true
//     },
//     ubicacion: { latitud: -37.428596602858, longitud: -72.131477594376 },
//     servicios: {
//       tienda: false,
//       farmacia: false,
//       mantencion: false,
//       autoservicio: false
//     }
//   },
//   {
//     _id: ObjectId("62cd86688363fa8782a6d394"),
//     id: 'co830105',
//     fecha_hora_actualizacion: '2022-01-27 09:29:15',
//     razon_social: 'Soc. Comer. Y Distr. De Combustibles Los Angeles Ltda // 76.149.375-2',
//     direccion_calle: 'AV. VICUï¿½A MACKENNA',
//     direccion_numero: '1241',
//     id_comuna: '08301',
//     nombre_comuna: 'Los Ángeles',
//     id_region: '08',
//     nombre_region: 'Del Biobío',
//     horario_atencion: '24 horas',
//     distribuidor: {
//       nombre: 'Copec',
//       logo: 'http://api.cne.cl/brands/logo5.jpg',
//       logo_svg: 'http://api.cne.cl/brands/copec.svg',
//       logo_horizontal_svg: 'http://api.cne.cl/brands/copec-horizontal.svg'
//     },
//     precios: {
//       'gasolina 93': 1037,
//       'gasolina 97': 1065,
//       'petroleo diesel': 837,
//       'gasolina 95': 1051
//     },
//     metodos_de_pago: {
//       efectivo: true,
//       cheque: false,
//       'tarjetas bancarias': true,
//       'tarjetas grandes tiendas': true
//     },
//     ubicacion: { latitud: -37.479832587953, longitud: -72.365352809429 },
//     servicios: {
//       tienda: true,
//       farmacia: false,
//       mantencion: true,
//       autoservicio: false
//     }
//   },
//   {
//     _id: ObjectId("62cd86688363fa8782a6d395"),
//     id: 'co830107',
//     fecha_hora_actualizacion: '2022-01-26 23:43:55',
//     razon_social: 'ADMINISTRADORA DE VENTAS AL DETALLE LTDA.',
//     direccion_calle: 'RUTA 5 SUR KM 518,5',
//     direccion_numero: '0',
//     id_comuna: '08301',
//     nombre_comuna: 'Los Ángeles',
//     id_region: '08',
//     nombre_region: 'Del Biobío',
//     horario_atencion: '24 horas',
//     distribuidor: {
//       nombre: 'Copec',
//       logo: 'http://api.cne.cl/brands/logo5.jpg',
//       logo_svg: 'http://api.cne.cl/brands/copec.svg',
//       logo_horizontal_svg: 'http://api.cne.cl/brands/copec-horizontal.svg'
//     },
//     precios: {
//       'gasolina 93': 1041,
//       'gasolina 97': 1103,
//       'petroleo diesel': 843,
//       'gasolina 95': 1075
//     },
//     metodos_de_pago: {
//       efectivo: true,
//       cheque: true,
//       'tarjetas bancarias': true,
//       'tarjetas grandes tiendas': true
//     },
//     ubicacion: { latitud: -37.546652920382, longitud: -72.309651374817 },
//     servicios: {
//       tienda: false,
//       farmacia: false,
//       mantencion: false,
//       autoservicio: false
//     }
//   },
//   {
//     _id: ObjectId("62cd86688363fa8782a6d396"),
//     id: 'co830108',
//     fecha_hora_actualizacion: '2022-01-27 16:13:38',
//     razon_social: 'ADMINISTRADORA DE VENTAS AL DETALLE  LTDA.',
//     direccion_calle: 'RUTA 5 SUR KM 484, SALIDA NORTE',
//     direccion_numero: '0',
//     id_comuna: '08301',
//     nombre_comuna: 'Los Ángeles',
//     id_region: '08',
//     nombre_region: 'Del Biobío',
//     horario_atencion: '24 horas',
//     distribuidor: {
//       nombre: 'Copec',
//       logo: 'http://api.cne.cl/brands/logo5.jpg',
//       logo_svg: 'http://api.cne.cl/brands/copec.svg',
//       logo_horizontal_svg: 'http://api.cne.cl/brands/copec-horizontal.svg'
//     },
//     precios: {
//       'gasolina 93': 1039,
//       'gasolina 97': 1096,
//       'petroleo diesel': 823,
//       'gasolina 95': 1063
//     },
//     metodos_de_pago: {
//       efectivo: true,
//       cheque: true,
//       'tarjetas bancarias': true,
//       'tarjetas grandes tiendas': true
//     },
//     ubicacion: { latitud: -37.283238543541, longitud: -72.353982925415 },
//     servicios: {
//       tienda: true,
//       farmacia: false,
//       mantencion: false,
//       autoservicio: false
//     }
//   },
//   {
//     _id: ObjectId("62cd86688363fa8782a6d397"),
//     id: 'co830109',
//     fecha_hora_actualizacion: '2022-01-27 12:08:42',
//     razon_social: 'SOC. COMERCIAL MONSERRAT LTDA.',
//     direccion_calle: 'AV. ERCILLA',
//     direccion_numero: '795',
//     id_comuna: '08301',
//     nombre_comuna: 'Los Ángeles',
//     id_region: '08',
//     nombre_region: 'Del Biobío',
//     horario_atencion: '24 horas',
//     distribuidor: {
//       nombre: 'Copec',
//       logo: 'http://api.cne.cl/brands/logo5.jpg',
//       logo_svg: 'http://api.cne.cl/brands/copec.svg',
//       logo_horizontal_svg: 'http://api.cne.cl/brands/copec-horizontal.svg'
//     },
//     precios: {
//       'gasolina 93': 1035,
//       'gasolina 97': 1063,
//       'petroleo diesel': 834,
//       'gasolina 95': 1047
//     },
//     metodos_de_pago: {
//       efectivo: true,
//       cheque: true,
//       'tarjetas bancarias': true,
//       'tarjetas grandes tiendas': true
//     },
//     ubicacion: { latitud: -37.464024570686, longitud: -72.354792952538 },
//     servicios: {
//       tienda: true,
//       farmacia: false,
//       mantencion: false,
//       autoservicio: false
//     }
//   },
//   {
//     _id: ObjectId("62cd86688363fa8782a6d398"),
//     id: 'co830104',
//     fecha_hora_actualizacion: '2022-01-27 07:52:05',
//     razon_social: 'Sociedad Comercial Urquieta Huerta Limitada',
//     direccion_calle: 'VALDIVIA',
//     direccion_numero: '100',
//     id_comuna: '08301',
//     nombre_comuna: 'Los Ángeles',
//     id_region: '08',
//     nombre_region: 'Del Biobío',
//     horario_atencion: '24 horas',
//     distribuidor: {
//       nombre: 'Copec',
//       logo: 'http://api.cne.cl/brands/logo5.jpg',
//       logo_svg: 'http://api.cne.cl/brands/copec.svg',
//       logo_horizontal_svg: 'http://api.cne.cl/brands/copec-horizontal.svg'
//     },
//     precios: {
//       'gasolina 93': 1031,
//       'gasolina 97': 1063,
//       'petroleo diesel': 829,
//       'gasolina 95': 1046
//     },
//     metodos_de_pago: {
//       efectivo: true,
//       cheque: true,
//       'tarjetas bancarias': true,
//       'tarjetas grandes tiendas': true
//     },
//     ubicacion: { latitud: -37.472288753288, longitud: -72.352805435658 },
//     servicios: {
//       tienda: false,
//       farmacia: false,
//       mantencion: true,
//       autoservicio: true
//     }
//   },
//   {
//     _id: ObjectId("62cd86688363fa8782a6d399"),
//     id: 'co830111',
//     fecha_hora_actualizacion: '2022-01-27 08:50:43',
//     razon_social: 'Combustibles Santa Inés de Curiche Limitada',
//     direccion_calle: 'Avda. Alemania',
//     direccion_numero: '1065',
//     id_comuna: '08301',
//     nombre_comuna: 'Los Ángeles',
//     id_region: '08',
//     nombre_region: 'Del Biobío',
//     horario_atencion: '24 horas',
//     distribuidor: {
//       nombre: 'Copec',
//       logo: 'http://api.cne.cl/brands/logo5.jpg',
//       logo_svg: 'http://api.cne.cl/brands/copec.svg',
//       logo_horizontal_svg: 'http://api.cne.cl/brands/copec-horizontal.svg'
//     },
//     precios: {
//       'gasolina 93': 1037,
//       'gasolina 97': 1065,
//       'petroleo diesel': 837,
//       'gasolina 95': 1051
//     },
//     metodos_de_pago: {
//       efectivo: true,
//       cheque: false,
//       'tarjetas bancarias': true,
//       'tarjetas grandes tiendas': true
//     },
//     ubicacion: { latitud: -37.4676933, longitud: -72.3335473 },
//     servicios: {
//       tienda: true,
//       farmacia: false,
//       mantencion: false,
//       autoservicio: false
//     }
//   },
//   {
//     _id: ObjectId("62cd86688363fa8782a6d39a"),
//     id: 'co830110',
//     fecha_hora_actualizacion: '2022-01-27 06:18:51',
//     razon_social: 'CONSTANZA ZIPPEL Y CIA LTDA',
//     direccion_calle: 'ALMAGRO',
//     direccion_numero: '1198',
//     id_comuna: '08301',
//     nombre_comuna: 'Los Ángeles',
//     id_region: '08',
//     nombre_region: 'Del Biobío',
//     horario_atencion: '24 horas',
//     distribuidor: {
//       nombre: 'Copec',
//       logo: 'http://api.cne.cl/brands/logo5.jpg',
//       logo_svg: 'http://api.cne.cl/brands/copec.svg',
//       logo_horizontal_svg: 'http://api.cne.cl/brands/copec-horizontal.svg'
//     },
//     precios: {
//       'gasolina 93': 1023,
//       'gasolina 97': 1057,
//       'petroleo diesel': 823,
//       'gasolina 95': 1030
//     },
//     metodos_de_pago: {
//       efectivo: true,
//       cheque: false,
//       'tarjetas bancarias': true,
//       'tarjetas grandes tiendas': true
//     },
//     ubicacion: { latitud: -37.45887229958, longitud: -72.348108887672 },
//     servicios: {
//       tienda: false,
//       farmacia: false,
//       mantencion: false,
//       autoservicio: false
//     }
//   }
// ]

// Se solicita realizar una consulta a libre elección que utilice $regex Busca
// todas las estaciones en que el nombre de la comuna empiece con "santa" y
// termine con una "a", sin importar mayúscula o minúscula. Solo muestra la
// columna de nombre comuna.
db.estaciones.find(
    {
        "nombre_comuna": {
            $regex: "^santa.*a$",
            $options: "i"
        }
    },
    {
        "nombre_comuna": 1
    }
)

// Se solicita realizar una consulta a libre elección que utilice $regex y
// operadores lógicos AND y OR
// Busca todas las estaciones en que (el nombre de la región contenga 3 letras
// "a" o el nombre de la comuna sean al menos 3 palabras, sin importar
// mayúscula o minúscula en ambos casos) y (la estación tenga petroleo a la
// venta y no venda gasolina 93). Finalmente solo muestra las columnas del
// nombre de la región, los precios y el nombre de la comuna. Finalmente los
// resultados se ordenan ascendentemente con el nombre de la región y luego el
// nombre de la comuna.
db.estaciones.find(
    {
        $and: [
            {
                $or: [
                    {
                        "nombre_region": {
                            $regex: "a.*a.*a",
                            $options: "i"
                        }
                    },
                    {
                        "nombre_comuna": {
                            $regex: " .* ",
                            $options: "i"
                        }
                    }
                ]
            },
            {
                "precios.petroleo diesel": {
                    $exists: true
                },
                "precios.gasolina 93": {
                    $exists: false
                }
            }
        ]
    },
    {
        "nombre_region": 1,
        "nombre_comuna": 1,
        "precios": 1
    }
).sort(
    {
        "nombre_region": 1,
        "nombre_comuna": 1
    }
)

// Respuesta
// [
//   {
//     _id: ObjectId("62cd86688363fa8782a6d730"),
//     nombre_comuna: 'Arica',
//     nombre_region: 'Arica y Parinacota',
//     precios: { 'petroleo diesel': 794 }
//   },
//   {
//     _id: ObjectId("62cd86688363fa8782a6d735"),
//     nombre_comuna: 'Arica',
//     nombre_region: 'Arica y Parinacota',
//     precios: { 'petroleo diesel': 790 }
//   },
//   {
//     _id: ObjectId("62cd86688363fa8782a6d736"),
//     nombre_comuna: 'Arica',
//     nombre_region: 'Arica y Parinacota',
//     precios: { 'petroleo diesel': 845 }
//   },
//   {
//     _id: ObjectId("62cd86688363fa8782a6d737"),
//     nombre_comuna: 'Arica',
//     nombre_region: 'Arica y Parinacota',
//     precios: { 'petroleo diesel': 792 }
//   },
//   {
//     _id: ObjectId("62cd86688363fa8782a6d742"),
//     nombre_comuna: 'Arica',
//     nombre_region: 'Arica y Parinacota',
//     precios: { 'petroleo diesel': 845 }
//   },
//   {
//     _id: ObjectId("62cd86688363fa8782a6d743"),
//     nombre_comuna: 'Arica',
//     nombre_region: 'Arica y Parinacota',
//     precios: { 'petroleo diesel': 815, 'gasolina 95': 1042 }
//   },
//   {
//     _id: ObjectId("62cd86688363fa8782a6d4c2"),
//     nombre_comuna: 'Cisnes',
//     nombre_region: 'Aysén del Gral. Carlos Ibáñez del Campo',
//     precios: { 'petroleo diesel': 945 }
//   },
//   {
//     _id: ObjectId("62cd86688363fa8782a6d4b4"),
//     nombre_comuna: 'Coihaique',
//     nombre_region: 'Aysén del Gral. Carlos Ibáñez del Campo',
//     precios: { 'petroleo diesel': 957, 'gasolina 95': 1139 }
//   },
//   {
//     _id: ObjectId("62cd86688363fa8782a6d4c6"),
//     nombre_comuna: 'O’Higgins',
//     nombre_region: 'Aysén del Gral. Carlos Ibáñez del Campo',
//     precios: { 'petroleo diesel': 1023, 'gasolina 95': 1201 }
//   },
//   {
//     _id: ObjectId("62cd86688363fa8782a6d224"),
//     nombre_comuna: 'Machalí',
//     nombre_region: 'Del Libertador Gral. Bernardo O’Higgins',
//     precios: { 'petroleo diesel': 851, 'gasolina 95': 1067 }
//   },
//   {
//     _id: ObjectId("62cd86688363fa8782a6d24d"),
//     nombre_comuna: 'Marchihue',
//     nombre_region: 'Del Libertador Gral. Bernardo O’Higgins',
//     precios: { 'petroleo diesel': 822, 'gasolina 95': 1043 }
//   },
//   {
//     _id: ObjectId("62cd86688363fa8782a6d233"),
//     nombre_comuna: 'Pichidegua',
//     nombre_region: 'Del Libertador Gral. Bernardo O’Higgins',
//     precios: { 'petroleo diesel': 830, 'gasolina 95': 1067 }
//   },
//   {
//     _id: ObjectId("62cd86688363fa8782a6d68b"),
//     nombre_comuna: 'Lampa',
//     nombre_region: 'Metropolitana de Santiago',
//     precios: { 'petroleo diesel': 826, 'gasolina 95': 1066 }
//   },
//   {
//     _id: ObjectId("62cd86688363fa8782a6d5d8"),
//     nombre_comuna: 'Peñalolén',
//     nombre_region: 'Metropolitana de Santiago',
//     precios: { 'petroleo diesel': 838 }
//   },
//   {
//     _id: ObjectId("62cd86688363fa8782a6d603"),
//     nombre_comuna: 'Pudahuel',
//     nombre_region: 'Metropolitana de Santiago',
//     precios: { 'petroleo diesel': 816 }
//   },
//   {
//     _id: ObjectId("62cd86688363fa8782a6d60a"),
//     nombre_comuna: 'Quilicura',
//     nombre_region: 'Metropolitana de Santiago',
//     precios: { 'petroleo diesel': 803 }
//   },
//   {
//     _id: ObjectId("62cd86688363fa8782a6d084"),
//     nombre_comuna: 'Alto Hospicio',
//     nombre_region: 'Tarapacá',
//     precios: { 'petroleo diesel': 826 }
//   },
//   {
//     _id: ObjectId("62cd86688363fa8782a6d086"),
//     nombre_comuna: 'Alto Hospicio',
//     nombre_region: 'Tarapacá',
//     precios: { 'petroleo diesel': 833 }
//   },
//   {
//     _id: ObjectId("62cd86688363fa8782a6d078"),
//     nombre_comuna: 'Iquique',
//     nombre_region: 'Tarapacá',
//     precios: { 'petroleo diesel': 846 }
//   },
//   {
//     _id: ObjectId("62cd86688363fa8782a6d18c"),
//     nombre_comuna: 'Los Andes',
//     nombre_region: 'Valparaíso',
//     precios: { 'petroleo diesel': 819 }
//   }
// ]
// Type "it" for more
