import requests
import json
import datetime
import os
import platform

sistema_operativo = platform.system()
hoy = datetime.datetime.today()
hoy = f"{hoy.day}-{hoy.month}-{hoy.year} {hoy.hour}-{hoy.minute}-{hoy.second}"

print("Obtener datos de estaciones de servicio.")

while True:
    print("\n1 - Maule")
    print("2 - Biobío")
    print("3 - Araucanía")

    opcion = input("\nEscoja una región: ")
    
    if opcion == "1":
        nombre_region = "maule"
        region = 7
        break

    if opcion == "2":
        nombre_region = "biobío"
        region = 8
        break

    if opcion == "3":
        nombre_region = "araucanía"
        region = 9
        break

    else:
        print("\nNo es una opción válida.")

print("\nObtener los datos puede generar miles de líneas de texto.")
opcion = input("¿Quiere guardar los datos en un archivo? (sí o no): ")

if opcion.lower() in ("s", "si", "sí"):
    guardar = True
else:
    guardar = False

token = "Pn1LRz5D3t"
url = f"http://api.cne.cl/v3/combustibles/vehicular/estaciones?token={token}&region={region}"
respuesta = json.loads(requests.get(url).text.encode("utf-8"))
datos = respuesta["data"]

with open(f"datos {nombre_region} {hoy}.txt", "w") as file:
    for i, local in enumerate(datos):
        estacion = f"Estación de servicio {i + 1}."
        razon_social = f"Razón social:     {local['razon_social']}"
        comuna = f"Comuna:           {local['nombre_comuna']}"
        direccion = f"Dirección:        {local['direccion_calle']}, {local['direccion_numero']}"
        horario = f"Horario atención: {local['horario_atencion']}"

        if i == 0:
            print()

        print(estacion)
        print(razon_social)
        print(comuna)
        print(direccion)
        print(horario)
        print("Precios:")

        if guardar:
            file.write(estacion + "\n")
            file.write(razon_social + "\n")
            file.write(comuna + "\n")
            file.write(direccion + "\n")
            file.write(horario + "\n")
            file.write("Precios:" + "\n")

        for nombre, valor in local["precios"].items():
            precio = f"\t{nombre}: ${valor}"

            print(precio)
            if guardar:
                file.write(precio + "\n")

        print("\n")
        if guardar:
            file.write("\n" + "\n")

if not guardar:
    if sistema_operativo == "Windows":
        os.system(f"powershell.exe rm 'datos {nombre_region} {hoy}.txt'")
    else:
        os.system(f"rm 'datos {nombre_region} {hoy}.txt'")