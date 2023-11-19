# Instalar ggplot2, no es necesario si ya se instaló
install.packages("ggplot2")

# Cargar la librería ggplot2
library(ggplot2)

# Definir empresas y meses de operación
empresas <- c("Aranguiz", "NCN", "Sanhueza", "Valroa")
meses <- c("Enero", "Febrero", "Marzo", "Abril")

# Ingresos de empresas por meses en el recorrido Santa Bárbara -> Los Ángeles
# |        |Enero   |Febrero |Marzo   |Abril   |
# |Aranguiz|5270000 |4938000 |7812300 |7800000 |
# |NCN     |3324750 |3115800 |3038650 |3035000 |
# |Sanhueza|2216500 |2077200 |3173050 |3168750 |
# |Valroa  |10850000|10167250|15380250|15356250|

aranguiz <- c(5270000, 4938000, 7812300, 7800000)
ncn <- c(3324750, 3115800, 3038650, 3035000)
sanhueza <- c(2216500, 2077200, 3173050, 3168750)
valroa <- c(10850000, 10167250, 15380250, 15356250)

ingresos <- rbind(aranguiz, ncn, sanhueza, valroa)
colnames(ingresos) <- meses
rownames(ingresos) <- empresas

graph <- function(data, rows, cols, scale = 1000000, position = "topleft") {
  # Tomar solo un subconjunto de datos de la matriz
  data <- data[rows, cols, drop = FALSE]
  data <- data / scale

  # Información principal del gráfico
  matplot(
    seq_along(colnames(data)),
    t(data),
    type = "b",
    col = c(1, 2, 4, 6),
    pch = 15:20,
    xlab = "Meses",
    ylab = sprintf("Ingresos en montos de $%d", scale),
    xaxt = "n",
    yaxt = "n",
    main = "Ingresos por empresa, primer cuatrimestre 2023."
  )

  # Agregar leyenda al gráfico
  legend(
    position,
    inset = 0.01,
    legend = rownames(data),
    pch = 15:20,
    col = c(1, 2, 4, 6)
  )

  # Agregar los ejes manualmente para usar los nombres correctos
  axis(1, at = seq_along(colnames(data)), labels = colnames(data))
  axis(2, las = 2)
}

# Graficar toda la información de la matriz
graph(ingresos)

# Graficar un subconjunto de la matriz
graph(
  ingresos,
  cols = (meses != "Febrero"),
  rows = (empresas != "Valroa"),
  scale = 1500000
)

# Graficar subconjunto de los buses NCN
graph(
  ingresos,
  rows = (empresas == "NCN"),
  position = "topright"
)

# Cargar archivo csv a un dataframe
df <- read.csv(file = file.choose())

# Calcular ingresos diarios
df$ingresos <- df$estudiantes * 600 + df$adultos * 1850

# Graficar todo el dataframe según distribución de pasajeros e ingresos
qplot(
  x = estudiantes,
  y = adultos,
  data = df,
  color = mes,
  size = ingresos,
  main = "Ingresos por distribución de pasajeros",
  xlab = "Estudiantes",
  ylab = "Adultos"
)

# Graficar un subconjunto, los meses de marzo y abril
qplot(
  x = estudiantes,
  y = adultos,
  data = df[df$mes %in% c("Marzo", "Abril"), ],
  color = mes,
  size = ingresos,
  main = "Ingresos por distribución de pasajeros",
  xlab = "Estudiantes",
  ylab = "Adultos"
)

# Calcular la razón estudiantes/adultos para cada mes
enero <- df[df$mes == "Enero", ]
sum(enero$estudiantes) / (sum(enero$estudiantes) + sum(enero$adultos))
febrero <- df[df$mes == "Febrero", ]
sum(febrero$estudiantes) / (sum(febrero$estudiantes) + sum(febrero$adultos))
marzo <- df[df$mes == "Marzo", ]
sum(marzo$estudiantes) / (sum(marzo$estudiantes) + sum(marzo$adultos))
abril <- df[df$mes == "Abril", ]
sum(abril$estudiantes) / (sum(abril$estudiantes) + sum(abril$adultos))
