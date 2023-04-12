datos <- read.csv(file = "datos.csv")

# Crear un histograma para la variable volumen
png("volumen.png", width = 800, height = 600)
hist(
    datos$volumen,
    ylab = "Número de árboles",
    xlab = "Volumen",
    main = "Histograma de frecuencias absolutas",
)
dev.off()

# Generar el diagrama circular de las variedades
variedades <- data.frame(table(datos$variedad))
variedades$porcentaje <- round(variedades$Freq / sum(variedades$Freq) * 100, 2)
png("circular.png", width = 800, height = 600)
pie(
    table(datos$variedad),
    labels = paste(variedades$Var1, "(", variedades$porcentaje, "%)", sep = "")
)
dev.off()

# Generar el polígono de frecuencias
png("poligono.png", width = 800, height = 600)
hist <- hist(
    datos$altura,
    ylab = "Número de árboles",
    xlab = "Altura (m)",
    main = "Polígono de frecuencias absolutas",
    col = "transparent",
    border = "transparent",
)
x <- c(min(hist$breaks), hist$mids, max(hist$breaks))
y <- c(0, hist$counts, 0)
lines(x, y, type = "l")
dev.off()
