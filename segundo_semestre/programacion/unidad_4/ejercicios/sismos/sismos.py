import requests
import json
import re

def obtener_distancia(referencia):
    patron = r"([0-9])* km"
    resultado = re.search(patron, referencia)
    if resultado is None:
        return 0
    if resultado:
        return int(resultado.group().strip(" km"))

def informacion_sismo(sismo):
    print(f"Referencia: {sismo['reference']}")
    print(f"Fecha: {sismo['chilean_time']}")
    print(f"Magnitud: {sismo['magnitude']}")
    print()

def main():
    url = "https://chilealerta.com/api/query/?user=demo&select=ultimos_sismos&country=chile"
    respuesta = requests.get(url)

    sismos_filtrados = []

    if respuesta.status_code != 200:
        print("No se pudo obtener la información.")
        return

    sismos_sin_filtrar = json.loads(respuesta.text.encode("utf-8"))
    for sismo in sismos_sin_filtrar["ultimos_sismos_chile"]:
        if sismo["magnitude"] > 4.5 and obtener_distancia(sismo["reference"]) < 90:
            sismos_filtrados.append(sismo)

    print("Sismos filtrados.")
    for sismo in sismos_filtrados:
        informacion_sismo(sismo)

if __name__ == "__main__":
    main()