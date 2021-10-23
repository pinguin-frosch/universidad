# 7.- Crear un algoritmo que, al ingresar una cantidad de segundos, permita obtener el número de horas, minutos y segundos totales.

# Hecho por Gabriel Barrientos

print(" Transformar de segundos a horas, minutos y segundos restantes ".center(71, "="))

def repetir():
    eleccion = input("\n¿Ejecutar de nuevo? (S/N): ")
    if eleccion.upper() in ("SÍ", "SI", "S"):
        calcular()
    else:
        input("\nGracias por usar. Pulse intro para salir. ")

def respuesta(x, y, z):
    """
    Permite obtener el artículo correcto según la cantidad de horas, minutos y segundos. 
    """
    if x != 1 and y != 1 and z != 1:
        return "Son {} horas, {} minutos y {} segundos."
    elif x != 1 and y != 1 and z == 1:
        return "Son {} horas, {} minutos y {} segundo."
    elif x != 1 and y == 1 and z != 1:
        return "Son {} horas, {} minuto y {} segundos."
    elif x != 1 and y == 1 and z == 1:
        return "Son {} horas, {} minuto y {} segundo."
    elif x == 1 and y != 1 and z != 1:
        return "Es {} hora, {} minutos y {} segundos."
    elif x == 1 and y != 1 and z == 1:
        return "Es {} hora, {} minutos y {} segundo."
    elif x == 1 and y == 1 and z != 1:
        return "Es {} hora, {} minuto y {} segundos."
    elif x == 1 and y == 1 and z == 1:
        return "Es {} hora, {} minuto y {} segundo."

def calcular():
    try:
        segundos = int(input("\nIngrese una cantidad de segundos: "))
        if segundos < 0:
            raise ValueError

        horas = segundos // 3600
        minutos = (segundos - (horas * 3600)) // 60
        segundos_restantes = segundos - ((horas * 3600) + (minutos * 60))

        print(respuesta(horas, minutos, segundos_restantes).format(horas, minutos, segundos_restantes))
    except ValueError:
        print("Solo ingrese segundos que sean enteros positivos, no ingrese letras u otros símbolos.")
    finally:
        repetir()

calcular()