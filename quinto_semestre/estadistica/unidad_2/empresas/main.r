# Instalar paquetes
install.packages("dplyr")
library(dplyr)

# Leer los datos
datos <- read.csv(
    file = "empresas.csv",
    sep = ";",
    dec = ",",
    header = TRUE,
    encoding = "latin1",
    col.names = c("año", "tramo", "region", "empresas", "ventas")
)

# Convertir los datos apropiadamente
datos$ventas <- as.numeric(gsub("[.*]", "", datos$ventas))
datos$empresas <- as.numeric(gsub("\\.", "", datos$empresas))
datos$region <- factor(datos$region)
datos$tramo <- factor(datos$tramo)

## Actividad 2
## Realice la tabla de frecuencias bidimensional, considerando las variables
## región, tramo y el número de empresas.
datos %>%
    group_by(region, tramo) %>%
    summarise(empresas = sum(empresas)) %>%
    print(n = 999)

## a) De acuerdo a tu región, ¿cuántas empresas están clasificadas en el tramo
## "Grande"?
## Son 8553 empresas grandes en la región del biobío.

## b) ¿Cuántas empresas están consideradas en la tabla a nivel país?
datos %>% summarise(empresas = sum(empresas))
## Hay 16686158 empresas en total

## Actividad 3
## Calcule la desviación estándar y el promedio por cada tramo
datos %>%
    group_by(tramo) %>%
    summarise(
        promedio = mean(ventas, na.rm = TRUE),
        desviacion = sd(ventas, na.rm = TRUE)
    )

## a) De los tramos obtenidos en la tabla, ¿cuál de ellos supera al promedio
## en general?
## Tengo dos interpretaciones. 1: Si se refiere a las más altas, entonces
## sería "Grande", "Mediana" y "Pequeña". 2: Si se refiere a cuáles superan
## al promedio total, entonces lo debo calcular primero.
datos %>% summarise(promedio = mean(ventas, na.rm = TRUE))
## El promedio general el 233306881, el único tramo que lo supera es "Grande"

## b) ¿Cuál de los tramos según ventas tiene mayor coeficiente de variación?
datos %>%
    group_by(tramo) %>%
    summarise(
        promedio = mean(ventas, na.rm = TRUE),
        desviacion = sd(ventas, na.rm = TRUE),
        coeficiente = desviacion / promedio
    )
## El tramo con mayor coeficiente de variación es "Grande"

## c) Obtenga el rango de las ventas según los tramos
datos %>%
    group_by(tramo) %>%
    summarise(rango = max(ventas, na.rm = TRUE) - min(ventas, na.rm = TRUE))

## d) ¿Qué tramo de empresa tiene mayor y menor rango de ventas anuales?
## Las empresas "Grande" tienen el mayor rango y las "Micro" el menor
