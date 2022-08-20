import requests
import json


def main():
    def menu():
        print("\n1 - Peso")
        print("2 - Euro")
        print("3 - Utm")
        print("4 - Dolar")
        print("5 - Uf")
        print("6 - Salir")

    def posible_int(x):
        x = int(x) if x.is_integer() else x
        return x

    def conversion(cantidad_inicial, moneda_1, moneda_2):
        valor_conversion = moneda_1 / moneda_2
        cantidad_final = round(cantidad_inicial * valor_conversion, 4)
        cantidad_final = posible_int(cantidad_final)
        return cantidad_final

    def asignar_moneda(opcion):
        if opcion == "1":
            moneda = valores["peso"]
            nombre = "CLP"
        elif opcion == "2":
            moneda = valores["euro"]
            nombre = "EUR"
        elif opcion == "3":
            moneda = valores["utm"]
            nombre = "UTM"
        elif opcion == "4":
            moneda = valores["dolar"]
            nombre = "USD"
        elif opcion == "5":
            moneda = valores["uf"]
            nombre = "UF"
        return moneda, nombre

    response = requests.get("https://mindicador.cl/api")
    # response.status_code = 300
    if response.status_code != 200:
        print("No se pudo obtener la información del servidor.")
        return
    data = json.loads(response.text.encode("utf-8"))

    valores = {}
    valores["uf"] = float(data["uf"]["valor"])
    valores["dolar"] = float(data["dolar"]["valor"])
    valores["euro"] = float(data["euro"]["valor"])
    valores["utm"] = float(data["utm"]["valor"])
    valores["peso"] = float(1)

    print(" Conversor de monedas ".center(50, "-"))
    while(True):
        menu()
        opcion = input("\n¿Qué moneda quiere convertir?: ")
        if opcion == "6":
            break
        try:
            (moneda_inicial, nombre_inicial) = asignar_moneda(opcion)
        except UnboundLocalError:
            print("\nOpción no válida.")
            continue

        opcion = input("\n¿A qué moneda quiere convertir?: ")
        if opcion == "6":
            break
        try:
            (moneda_final, nombre_final) = asignar_moneda(opcion)
        except UnboundLocalError:
            print("\nOpción no válida.")
            continue

        while(True):
            cantidad_inicial = input("\nIngrese la cantidad a convertir: ")
            try:
                cantidad_inicial = round(float(cantidad_inicial), 4)
                cantidad_inicial = posible_int(cantidad_inicial)
                break
            except ValueError:
                print("\nNo es un número.")

        cantidad_final = conversion(cantidad_inicial, moneda_inicial, moneda_final)

        print(f"\n{cantidad_inicial} {nombre_inicial} = {cantidad_final} {nombre_final}")


if __name__ == "__main__":
    main()
