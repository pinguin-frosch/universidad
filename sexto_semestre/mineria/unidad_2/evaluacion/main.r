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
    ylab = sprintf("Ingresos en montos de %d$", scale),
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

graph(
  ingresos,
  cols = (meses != "Febrero"),
  rows = (empresas != "Valroa"),
  scale = 25000
)
