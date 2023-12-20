import json
import datetime
import random
import sys

def main():
    args = sys.argv[1:]
    if len(args) < 1:
        print(f"Uso: python {sys.argv[0]} EMPRESA")
        return

    empresa = args[0]
    configuracion = open('configuracion.json')
    datos = json.load(configuracion)
    datos_empresa = datos[empresa]
    resultados = generar_recorridos(datos_empresa)

    print("Estas son las ganancias por mes:")
    for mes in resultados["meses"]:
        print(mes["nombre"])
        print(f"Estudiantes: {mes['ingresos_estudiantes']}")
        print(f"Adultos: {mes['ingresos_adultos']}")
        print(f"Total: {mes['ingresos']}\n")

    print("Esta es la información sobre sobrecarga")
    sobrecargas = resultados["sobrecargas"]
    sobrecargas = sorted(sobrecargas.items())
    for sobrecarga in sobrecargas:
        print(sobrecarga[0], sobrecarga[1])

    continuar = input("\n¿Traspasar a instrucciones sql? [s/N]: ")
    if continuar == "":
        return

    print("Pasando a instrucciones .sql")

def generar_recorridos(empresa):
    e = {"nombre": empresa["nombre"], "meses": [], "recorridos": [], "sobrecargas": {}}
    recorridos_diarios = len(empresa["recorridos"])
    for mes in empresa["meses"]:
        m = {
            "nombre": mes["nombre"],
            "ingresos_estudiantes": 0,
            "ingresos_adultos": 0,
            "ingresos": 0
        }
        estudiantes_totales_mes = 0
        adultos_totales_mes = 0
        dias_al_mes = obtener_dias_en_mes(mes["mes"])
        estudiantes_por_recorrido = round(mes["estudiantes"] / dias_al_mes / recorridos_diarios)
        adultos_por_recorrido = round(mes["adultos"] / dias_al_mes / recorridos_diarios)
        fecha = datetime.datetime(2023, mes["mes"], 1)
        while fecha.month == mes["mes"]:
            fecha_siguiente = fecha + datetime.timedelta(days=1)
            dias_finales_actualizados = False
            for i, recorrido in enumerate(empresa["recorridos"]):
                r = recorrido
                r["fecha"] = fecha
                estudiantes = 0
                adultos = 0
                if fecha_siguiente.month != mes["mes"] and i == len(empresa["recorridos"]) - 1:
                    estudiantes = mes["estudiantes"] - estudiantes_totales_mes
                    adultos = mes["adultos"] - adultos_totales_mes
                else:
                    if fecha_siguiente.month != mes["mes"] and not dias_finales_actualizados:
                        estudiantes_por_recorrido = round((mes["estudiantes"] - estudiantes_totales_mes) / recorridos_diarios)
                        adultos_por_recorrido = round((mes["adultos"] - adultos_totales_mes) / recorridos_diarios)
                        estudiantes = estudiantes_por_recorrido
                        adultos = adultos_por_recorrido
                        dias_finales_actualizados = True
                    else:
                        estudiantes = random.randint(max(0, estudiantes_por_recorrido - 1), estudiantes_por_recorrido)
                        adultos = random.randint(max(0, adultos_por_recorrido - 1), adultos_por_recorrido + 2)
                if estudiantes < 0 or adultos < 0:
                    print("Pasó algo raro, hay valores negativos", estudiantes, adultos)
                    sys.exit(0)
                r["estudiantes"] = estudiantes
                r["adultos"] = adultos
                estudiantes_totales_mes += estudiantes
                adultos_totales_mes += adultos
                m["ingresos_estudiantes"] += r["estudiantes"] * 600
                m["ingresos_adultos"] += r["adultos"] * 1850
                recorrido_a_guardar = {
                    "nombre": empresa["nombre"],
                    "fecha": (fecha + datetime.timedelta(hours=r["hora"], minutes=r["minuto"])).strftime("%Y-%m-%d %H:%M"),
                    "estudiantes": r["estudiantes"],
                    "adultos": r["adultos"],
                    "capacidad": r["capacidad"],
                    "sobrecarga": (r["estudiantes"] + r["adultos"]) - r["capacidad"]
                }
                if recorrido_a_guardar["sobrecarga"] not in e["sobrecargas"]:
                    e["sobrecargas"][recorrido_a_guardar["sobrecarga"]] = 0
                e["sobrecargas"][recorrido_a_guardar["sobrecarga"]] += 1
                e["recorridos"].append(recorrido_a_guardar)
            fecha = fecha_siguiente
        m["ingresos"] += m["ingresos_estudiantes"] + m["ingresos_adultos"]
        e["meses"].append(m)
    return e

def obtener_dias_en_mes(numero_mes):
    fecha = datetime.date(2023, numero_mes, 1)
    dias = 0
    while fecha.month == numero_mes:
        dias += 1
        fecha = fecha + datetime.timedelta(days=1)
    return dias

if __name__ == '__main__':
    main()
