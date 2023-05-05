# Leer la base de datos
datos <- read.csv(file = "datos.csv", header = TRUE, sep = ",")

## 1. Crear la variable sueldo per-cápita en R usando la estructura adecuada.
datos$sueldo_per_capita <- round(datos$remuneracion / datos$integrantes)


## 2. Crear la variable decil al que pertenece, considerando la información de
## la tabla deciles.

# Inicialmente todos estarán en el decil 10
datos$decil <- 10

# Valores máximos para cada decil
rangos <- c(
    48750, 74969, 100709, 125558, 154166,
    193104, 250663, 352743, 611728
)

# Actualizar cada registro con el decil correcto
for (i in seq_along(datos$sueldo_per_capita)) {
    for (j in seq_along(rangos)) {
        if (datos$sueldo_per_capita[i] <= rangos[j]) {
            datos$decil[i] <- j
            break
        }
    }
}


## 3. Realice un gráfico de barras de la distribución de estudiantes por decil
## al que pertenece.
barplot(table(datos$decil), main = "Cantidad de familias en cada decil")


## 4. Crear la variable gratuidad con respuesta "Si" o "No" según corresponda.
datos$gratuidad <- "No"
datos$gratuidad[datos$decil <= 6] <- "Si"


## 5. Construya un gráfico circular con el porcentaje de estudiantes con y sin
## gratuidad.
pie(
    table(datos$gratuidad),
    labels = c("Sin gratuidad", "Con gratuidad"),
    main = "Gráfico del nivel de gratuidad"
)
