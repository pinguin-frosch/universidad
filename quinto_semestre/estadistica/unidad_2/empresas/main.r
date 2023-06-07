datos <- read.csv(
    file = "empresas.csv",
    sep = ";",
    dec = ",",
    header = TRUE,
    encoding = "latin1"
)

# Usar unos nombres más cómodos
colnames(datos) <- c("año", "tramo", "region", "empresas", "ventas")

# Convertir los datos apropiadamente
datos$ventas <- as.numeric(gsub("[.*]", "", datos$ventas))
datos$empresas <- as.numeric(gsub("\\.", "", datos$empresas))
datos$region <- factor(datos$region)
datos$tramo <- factor(datos$tramo)

# Realice la tabla de frecuencias bidimensional respecto a la región y el tramo
region_tramo <- table(
    datos$region,
    datos$tramo
)

# Calcule el promedio y la desviación estándar por cada tramo.
tramo_avg_sd <- aggregate(
    datos$ventas,
    by = list(datos$tramo),
    FUN = function(x) {
        c(
            mean = mean(x, na.rm = TRUE),
            std = sd(x, na.rm = TRUE),
            min = min(x, na.rm = TRUE),
            max = max(x, na.rm = TRUE),
            range = max(x, na.rm = TRUE) - min(x, na.rm = TRUE)
        )
    }
)
