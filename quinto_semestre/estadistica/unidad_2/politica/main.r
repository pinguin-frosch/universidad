# Leer la base de datos
datos <- read.csv(
    file = "politica.csv",
    sep = ";",
    header = TRUE,
    col.names = c("partido", "comuna", "rango_edad", "sexo", "categoria"),
    stringsAsFactors = TRUE
)

## Actividad 2
## a) Construya una tabla bidimensional con los sexos y rangos de edad.
sexo_edad <- table(datos$sexo, datos$rango_edad)

## b) De acuerdo con su interpretación, ¿en qué rango de edad se observa más
## inscritos en mujeres y hombres.
## En ambos casos esto ocurre en el rango de edad de 20 a 24 años. Hay 778
## mujeres en ese rango, y 502 hombres.

## Determinar la cantidad de mujeres y hombres en la muestra
hombres <- sum(sexo_edad["Masculino", ])
mujeres <- sum(sexo_edad["Femenino", ])

## Determinar el porcentaje de mujeres en la muestra
total <- mujeres + hombres
p_mujeres <- mujeres / total * 100

## Calcular la frecuencia relativa de afiliados entre 55 y 59
p_afiliados <- sum(sexo_edad[, "55-59"]) / total * 100

## Calcular la frecuencia de mujeres entre 18 a 34 años
m_18_34 <- sum(sexo_edad["Femenino", 1:4])
p_m_18_34 <- m_18_34 / total * 100

## Dado que el afiliado es masculino, determinar la posibilidad o frecuencia de
## que tenga entre 40 y 44 años
p_h_40_44 <- sexo_edad["Masculino", "40-44"] / hombres * 100

## Determinar la frecuencia con la que el afilidado tenga 50-54 años o tenga
## 60-64 años
p_50_54 <- sum(sexo_edad[, c("50-54", "60-64")]) / total * 100

## Determinar la frecuencia de que el afiliado sea mujer y tenga 65-69 años
p_m_65_69 <- sum(sexo_edad["Femenino", "65-69"]) / total * 100

## Actividad 3
## Cree una tabla de frecuencias bidimensional con las comunas y rangos de edad,
## separar entre 18 a 29, 30 a 64 y 65 o más.
comuna_edad <- table(datos$comuna, datos$rango_edad)

## 18-29
rowSums(comuna_edad[, 1:3])
## 30-64
rowSums(comuna_edad[, 4:10])
## 65 o más
rowSums(comuna_edad[, 11:14])

## Actividad 4
## Considerando las variables partido y sexo, construya una tabla de frecuencia
## bidimensional y su respectiva representación gráfica.
table(datos$partido, datos$sexo)

## TODO: Graficar

## ¿Qué partido político observas que tiene mayor diferencia de afiliados por
## sexo?
## El partido progresista es el que tiene la mayor diferencia, hay 612 mujeres
## y solo 142 hombres. Es una diferencia de 470 personas.
