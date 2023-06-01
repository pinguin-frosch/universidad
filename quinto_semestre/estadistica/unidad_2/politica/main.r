# Leer la base de datos
datos <- read.csv(file = "politica.csv", sep = ";", header = TRUE)

# Construya una representación gráfica de barras bidimensional para la tabla
# anterior.
tabla <- table(datos$SEXO, datos$RANGO_EDAD)

# Determinar la cantidad de mujeres y hombres en la muestra
hombres <- sum(tabla["Masculino", ])
mujeres <- sum(tabla["Femenino", ])

# Determinar el porcentaje de mujeres en la muestra
total <- mujeres + hombres
porcentaje_mujeres <- mujeres / (total) * 100

# Calcular la frecuencia relativa de afiliados entre 55 y 59
porcentaje_afiliados <- (sum(tabla[, "55-59"]) / total) * 100

# Calcular la frecuencia de mujeres entre 18 a 34 años
m_18_34 <- sum(tabla[c("Femenino"), c("18 a 19", "20-24", "25-29", "30-34")])
porcentaje_m_18_34 <- (m_18_34 / total) * 100

# Dado que el afiliado es masculino, determinar la posibilidad o frecuencia de
# que tenga entre 40 y 44 años
porcentaje_h_40_44 <- (tabla["Masculino", "40-44"] / hombres) * 100

# Determinar la frecuencia con la que el afilidado tenga 50-54 años o tenga
# 60-64 años
porcentaje_50_54 <- sum(tabla[, c("50-54", "60-64")]) / total * 100

# Determinar la frecuencia de que el afiliado sea mujer y tenga 65-69 años
porcentaje_m_65_69 <- sum(tabla["Femenino", "65-69"]) / total * 100

# Datos separados por comuna y rango de edad
comuna_edad <- table(datos$COMUNA, datos$RANGO_EDAD)

# 18-29
rowSums(comuna_edad[, c("18 a 19", "20-24", "25-29")])
# 30-64
rowSums(comuna_edad[, c("30-34", "35-39", "40-44", "45-49", "50-54", "55-59", "60-64")])
# 65 o más
rowSums(comuna_edad[, c("65-69", "70-74", "75-79", "80 o +")])
