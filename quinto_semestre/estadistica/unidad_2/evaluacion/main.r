## Integrantes
## Constanza Baeza
## Gabriel Barrientos
## Cristian Espinoza

## Cargar la librería dplyr
library(dplyr)

## Leer los datos
datos <- read.csv(
    file = "datos.csv",
    header = TRUE,
    sep = ",",
    col.names = c(
        "id",
        "genero",
        "rango_edad",
        "fuerza_trabajo",
        "estado_laboral",
        "ingreso"
    )
)

## Problema 1
## a) Complete la tabla de bidimensional entre género y rango de edad.
table(datos$genero, datos$rango_edad)

## Problema 2
## a) Realice una tabla bidimensional entre fuerza de trabajo y rangos de edad.
datos %>%
    group_by(fuerza_trabajo) %>%
    summarise(
        "15-44" = sum(rango_edad %in% c("15-24", "25-34", "35-44")),
        "45-64" = sum(rango_edad %in% c("45-54", "55-64")),
        "total" = n()
    )

## Problema 3
## a) Realice la tabla bidimensional entre género y estado laboral, para
## aquellos que pertenecen a la fuerza de trabajo.
datos %>%
    filter(fuerza_trabajo == "SI") %>%
    group_by(genero) %>%
    summarise(
        ocupado = sum(
            estado_laboral %in% c("Trabajo Formal", "Trabajo Informal")
        ),
        desocupado = sum(estado_laboral == "Sin trabajo"),
    )
