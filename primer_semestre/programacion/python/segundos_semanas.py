print(" Transformar de segundos a semanas, días, horas, minutos y segundos restantes ".center(100, "="))

def respuesta(x, y, z, w, v):
    if x != 1 and y != 1 and z != 1 and w != 1 and v != 1:
        return "Son {} semanas, {} días, {} horas, {} minutos y {} segundos."
    elif x != 1 and y != 1 and z != 1 and w != 1 and v == 1:
        return "Son {} semanas, {} días, {} horas, {} minutos y {} segundo."
    elif x != 1 and y != 1 and z != 1 and w == 1 and v != 1:
        return "Son {} semanas, {} días, {} horas, {} minuto y {} segundos."
    elif x != 1 and y != 1 and z != 1 and w == 1 and v == 1:
        return "Son {} semanas, {} días, {} horas, {} minuto y {} segundo."
    elif x != 1 and y != 1 and z == 1 and w != 1 and v != 1:
        return "Son {} semanas, {} días, {} hora, {} minutos y {} segundos."
    elif x != 1 and y != 1 and z == 1 and w != 1 and v == 1:
        return "Son {} semanas, {} días, {} hora, {} minutos y {} segundo."
    elif x != 1 and y != 1 and z == 1 and w == 1 and v != 1:
        return "Son {} semanas, {} días, {} hora, {} minuto y {} segundos."
    elif x != 1 and y != 1 and z == 1 and w == 1 and v == 1:
        return "Son {} semanas, {} días, {} hora, {} minuto y {} segundo."
    elif x != 1 and y == 1 and z != 1 and w != 1 and v != 1:
        return "Son {} semanas, {} día, {} horas, {} minutos y {} segundos."
    elif x != 1 and y == 1 and z != 1 and w != 1 and v == 1:
        return "Son {} semanas, {} día, {} horas, {} minutos y {} segundo."
    elif x != 1 and y == 1 and z != 1 and w == 1 and v != 1:
        return "Son {} semanas, {} día, {} horas, {} minuto y {} segundos."
    elif x != 1 and y == 1 and z != 1 and w == 1 and v == 1:
        return "Son {} semanas, {} día, {} horas, {} minuto y {} segundo."
    elif x != 1 and y == 1 and z == 1 and w != 1 and v != 1:
        return "Son {} semanas, {} día, {} hora, {} minutos y {} segundos."
    elif x != 1 and y == 1 and z == 1 and w != 1 and v == 1:
        return "Son {} semanas, {} día, {} hora, {} minutos y {} segundo."
    elif x != 1 and y == 1 and z == 1 and w == 1 and v != 1:
        return "Son {} semanas, {} día, {} hora, {} minuto y {} segundos."
    elif x != 1 and y == 1 and z == 1 and w == 1 and v == 1:
        return "Son {} semanas, {} día, {} hora, {} minuto y {} segundo."
    elif x == 1 and y != 1 and z != 1 and w != 1 and v != 1:
        return "Es {} semana, {} días, {} horas, {} minutos y {} segundos."
    elif x == 1 and y != 1 and z != 1 and w != 1 and v == 1:
        return "Es {} semana, {} días, {} horas, {} minutos y {} segundo."
    elif x == 1 and y != 1 and z != 1 and w == 1 and v != 1:
        return "Es {} semana, {} días, {} horas, {} minuto y {} segundos."
    elif x == 1 and y != 1 and z != 1 and w == 1 and v == 1:
        return "Es {} semana, {} días, {} horas, {} minuto y {} segundo."
    elif x == 1 and y != 1 and z == 1 and w != 1 and v != 1:
        return "Es {} semana, {} días, {} hora, {} minutos y {} segundos."
    elif x == 1 and y != 1 and z == 1 and w != 1 and v == 1:
        return "Es {} semana, {} días, {} hora, {} minutos y {} segundo."
    elif x == 1 and y != 1 and z == 1 and w == 1 and v != 1:
        return "Es {} semana, {} días, {} hora, {} minuto y {} segundos."
    elif x == 1 and y != 1 and z == 1 and w == 1 and v == 1:
        return "Es {} semana, {} días, {} hora, {} minuto y {} segundo."
    elif x == 1 and y == 1 and z != 1 and w != 1 and v != 1:
        return "Es {} semana, {} día, {} horas, {} minutos y {} segundos."
    elif x == 1 and y == 1 and z != 1 and w != 1 and v == 1:
        return "Es {} semana, {} día, {} horas, {} minutos y {} segundo."
    elif x == 1 and y == 1 and z != 1 and w == 1 and v != 1:
        return "Es {} semana, {} día, {} horas, {} minuto y {} segundos."
    elif x == 1 and y == 1 and z != 1 and w == 1 and v == 1:
        return "Es {} semana, {} día, {} horas, {} minuto y {} segundo."
    elif x == 1 and y == 1 and z == 1 and w != 1 and v != 1:
        return "Es {} semana, {} día, {} hora, {} minutos y {} segundos."
    elif x == 1 and y == 1 and z == 1 and w != 1 and v == 1:
        return "Es {} semana, {} día, {} hora, {} minutos y {} segundo."
    elif x == 1 and y == 1 and z == 1 and w == 1 and v != 1:
        return "Es {} semana, {} día, {} hora, {} minuto y {} segundos."
    elif x == 1 and y == 1 and z == 1 and w == 1 and v == 1:
        return "Es {} semana, {} día, {} hora, {} minuto y {} segundo."

def repetir():
    eleccion = input("\n¿Ejecutar de nuevo? (S/N): ")
    if eleccion.upper() in ("SÍ", "SI", "S"):
        calcular()
    else:
        input("\nGracias por usar. Pulse intro para salir. ")

def calcular():
    try:
        segundos = int(input("\nIngrese una cantidad de segundos: "))
        if segundos < 0:
            raise ValueError

        semanas = segundos // 604800
        dias = (segundos - (semanas * 604800)) // 86400
        horas = (segundos - ((semanas * 604800) + (dias * 86400))) // 3600
        minutos = (segundos - ((semanas * 604800) + (dias * 86400) + (horas * 3600))) // 60
        segundos_restantes = segundos - ((semanas * 604800) + (dias * 86400) + (horas * 3600) + (minutos * 60))

        print(respuesta(semanas, dias, horas, minutos, segundos_restantes).format(semanas, dias, horas, minutos, segundos_restantes))

    except ValueError:
        print("Solo ingrese segundos que sean enteros positivos, no ingrese letras u otros símbolos.")
    finally:
        repetir()

calcular()