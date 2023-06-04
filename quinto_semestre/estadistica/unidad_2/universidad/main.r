# Leer base de datos en codificación latin1.
# Los nombres de las columnas no pueden contener caráteres de más de un byte,
# latin1 usa solo un byte para cada carácter. Pero lo correcto sería usar
# nombres de columnas sin carácteres especiales y leer en codificación UTF-8.
datos <- read.csv(
    file = "universidad.csv",
    header = TRUE,
    sep = ";",
    encoding = "latin1"
)

# Cambiar los nombres para mejor experiencia
colnames(datos) <- c(
    "institucion",
    "tipo_institucion",
    "sede",
    "comuna",
    "region",
    "numero_region",
    "carrera",
    "programa",
    "area",
    "vacantes"
)

# Realice la tabla bidimensional entre regiones y tipo de institución
region_tipo <- table(datos$region, datos$tipo_institucion)

# ¿Cuántas carreras hay en cft, ip y universidades?
cft <- sum(region_tipo[, "C.F.T."])
ip <- sum(region_tipo[, "I.P."])
universidad <- sum(region_tipo[, "Univ."])

# ¿Cuántas carreras ofrece inacap en total?
total <- cft + ip + universidad

# Realizar la tabla bidimensional entre área y vacantes
table(datos$area)

### Esto no es para nada bueno, tuve que calcular manualmenete los valores e
### incluso así no se ve bien el gráfico. Creo que para esto es mejor trabajar
### con ggplot2.
datos$tipo_institucion <- factor(datos$tipo_institucion)
datos$region <- factor(datos$region)
regiones <- unique(datos$region)
tipos <- unique(datos$tipo_institucion)
barras_por_region <- length(tipos)
barras_totales <- barras_por_region * length(regiones)

barplot(
    matrix(
        datos$vacantes,
        nrow = barras_por_region,
        ncol = length(regiones),
        byrow = TRUE
    ),
    beside = TRUE,
    col = c("red", "blue", "green"),
    xlab = "Región",
    ylab = "Total de vacantes",
    legend.text = levels(datos$tipo_institucion),
)

posiciones <- seq(2.5, barras_totales * 1.35, by = barras_por_region + 1)

axis(1, at = posiciones, labels = regiones, las = 2)
