import json
import datetime
import random

def main():
    configuracion = open('configuracion.json')
    datos = json.load(configuracion)
    resultados = generar_recorridos(datos)
    print(resultados)

def generar_recorridos(datos):
    resultados = []

    for empresa in datos:
        e = {"nombre": empresa["nombre"], "recorridos": []}
        recorridos_diarios = len(empresa["recorridos"])
        for mes in empresa["meses"]:
            m = {
                "nombre": mes["nombre"],
                "recorridos": [],
                "ingresos_estudiantes": 0,
                "ingresos_adultos": 0,
                "ingresos": 0
            }
            estudiantes_totales_mes = 0
            adultos_totales_mes = 0
            dias_al_mes = obtener_dias_en_mes(mes["mes"])
            estudiantes_por_recorrido = round(mes["estudiantes"] / dias_al_mes / recorridos_diarios)
            adultos_por_recorrido = round(mes["adultos"] / dias_al_mes / recorridos_diarios)

            fecha = datetime.date(2023, mes["mes"], 1)
            while fecha.month == mes["mes"]:
                fecha_siguiente = fecha + datetime.timedelta(days=1)
                for recorrido in empresa["recorridos"]:
                    r = recorrido
                    estudiantes = 0
                    adultos = 0
                    if fecha_siguiente.month != mes["mes"]:
                        estudiantes = mes["estudiantes"] - estudiantes_totales_mes
                        adultos = mes["adultos"] - adultos_totales_mes
                    else:
                        estudiantes = random.randint(max(0, estudiantes_por_recorrido - 3), estudiantes_por_recorrido + 2)
                        adultos = random.randint(max(0, adultos_por_recorrido - 3), adultos_por_recorrido + 2)
                    if estudiantes < 0 or adultos < 0:
                        print("Pasó algo raro, hay valores negativos", estudiantes, adultos)
                    r["estudiantes"] = estudiantes
                    r["adultos"] = adultos
                    estudiantes_totales_mes += estudiantes
                    adultos_totales_mes += adultos

                    m["ingresos_estudiantes"] += r["estudiantes"] * 600
                    m["ingresos_adultos"] += r["adultos"] * 1850
                fecha = fecha_siguiente
            m["ingresos"] += m["ingresos_estudiantes"] + m["ingresos_adultos"]

            e["recorridos"].append(m)
        resultados.append(e)

    return resultados

def obtener_dias_en_mes(numero_mes):
    fecha = datetime.date(2023, numero_mes, 1)
    dias = 0
    while fecha.month == numero_mes:
        dias += 1
        fecha = fecha + datetime.timedelta(days=1)
    return dias

if __name__ == '__main__':
    main()
