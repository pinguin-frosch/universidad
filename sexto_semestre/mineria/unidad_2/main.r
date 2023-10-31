# Nota 1: Usar matrices para este ejercicio no fue lo mejor.
# Un dataframa habría sido mucho mejor aquí.

# Definir jugadores y temporadas
jugadores <- c(
  "Esteban Paredes", "Lucas Barrios",
  "Eduardo Vargas", "Alexis Sanchez"
)
temporadas <- c(2019, 2020, 2021, 2022)

# Jugadores y Goles
# |               |2019|2020|2021|2022|
# |Esteban Paredes|15  |12  |14  |20  |
# |Lucas Barrios  |7   |9   |12  |4   |
# |Eduardo Vargas |2   |4   |5   |6   |
# |Alexis Sanchez |12  |22  |31  |15  |

# Guardar los goles de cada jugador
esteban_goles <- c(15, 12, 14, 20)
lucas_goles <- c(7, 9, 12, 4)
eduardo_goles <- c(2, 4, 5, 6)
alexis_goles <- c(12, 22, 31, 15)

# Crear la matriz que representa los goles
goles <- rbind(
  esteban_goles, lucas_goles,
  eduardo_goles, alexis_goles
)
rownames(goles) <- jugadores
colnames(goles) <- temporadas

# Jugadores y Partidos
# |               |2019|2020|2021|2022|
# |Esteban Paredes|20  |22  |23  |20  |
# |Lucas Barrios  |15  |22  |31  |30  |
# |Eduardo Vargas |12  |44  |11  |30  |
# |Alexis Sanchez |33  |12  |30  |19  |

# Guadar los partidos de cada jugador
esteban_partidos <- c(20, 22, 23, 20)
lucas_partidos <- c(15, 22, 31, 30)
eduardo_partidos <- c(12, 44, 11, 30)
alexis_partidos <- c(33, 12, 30, 19)

# Crear la matriz que representa los partidos
partidos <- rbind(
  esteban_partidos, lucas_partidos,
  eduardo_partidos, alexis_partidos
)
rownames(partidos) <- jugadores
colnames(partidos) <- temporadas

# Calcular frecuencia de goles por partido
goles_partido <- round(partidos / goles, 1)
# Nota 2: Está mal la guía, debería ser goles / partidos
# Lo dejaré mal para no interferir con el resto del ejercicio

# Jugadores y Sueldos
# |               |2019    |2020    |2021    |2022    |
# |Esteban Paredes|22500000|24500000|27500000|31500000|
# |Lucas Barrios  |15000000|17000000|19000000|19999999|
# |Eduardo Vargas |12000000|14230000|16930000|21999000|
# |Alexis Sanchez |33000000|34000500|40120000|49233100|

# Guardar los sueldos de cada jugador
esteban_sueldo <- c(22500000, 24500000, 27500000, 31500000)
lucas_sueldo <- c(15000000, 17000000, 19000000, 19999999)
eduardo_sueldo <- c(12000000, 14230000, 16930000, 21999000)
alexis_sueldo <- c(33000000, 34000500, 40120000, 49233100)

# Crear la matriz que representa los sueldos
sueldos <- rbind(
  esteban_sueldo, lucas_sueldo,
  eduardo_sueldo, alexis_sueldo
)
rownames(sueldos) <- jugadores
colnames(sueldos) <- temporadas

# Calcular precio por frecuencia de gol por jugador sin decimales
precio_goles_partido <- round(sueldos / goles_partido, 0)

# Añadir la información principal al gráfico
matplot(
  temporadas,
  t(goles),
  type = "b",
  pch = 15:20,
  xlab = "Temporadas",
  ylab = "Goles",
  xaxt = "n"
)
# Agregar leyenda al gráfico
legend(
  "topleft",
  inset = 0.01,
  legend = jugadores,
  pch = 15:20,
  col = 1:6
)
# Usar las temporadas como los valores del eje x
axis(1, temporadas)
