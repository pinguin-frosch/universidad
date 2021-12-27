# Creado conjuntamente por Gabriel Barrientos y Charlotte Rodriguez

import requests
import pymysql
import json
from sys import exit

URL = "http://www.mindicador.cl/api"

def main():
    print("Actualizando valores, espere un momento.")
    response = json.loads(requests.get(URL).text.encode("utf-8"))
    dolar = response["dolar"]
    euro = response["euro"]
    uf = response["uf"]
    divisas = compraDivisas("localhost", "root", "", "bd_divisas")

    while True:
        print("\n1 - Comprar dólares.")
        print("2 - Comprar euros.")
        print("3 - Comprar uf.")
        print("4 - Listar compras de un usuario.")
        print("5 - Listar todas las compras.")
        print("6 - Commit.")
        print("7 - Salir.")

        opcion = input("\nIngrese una opción: ")

        if opcion == "1":
            run = input("\nRun: ")
            nombre = input("Nombre: ")
            while True:
                cantidad = input("Cantidad comprada: ")
                try:
                    cantidad = float(cantidad)
                    break
                except ValueError:
                    print("Valor incorrecto.")
            divisas.comprar_divisa(run, nombre, dolar["nombre"], cantidad, dolar["valor"])

        if opcion == "2":
            run = input("\nRun: ")
            nombre = input("Nombre: ")
            while True:
                cantidad = input("Cantidad comprada: ")
                try:
                    cantidad = float(cantidad)
                    break
                except ValueError:
                    print("Valor incorrecto.")
            divisas.comprar_divisa(run, nombre, euro["nombre"], cantidad, euro["valor"])

        if opcion == "3":
            run = input("\nRun: ")
            nombre = input("Nombre: ")
            while True:
                cantidad = input("Cantidad comprada: ")
                try:
                    cantidad = float(cantidad)
                    break
                except ValueError:
                    print("Valor incorrecto.")
            divisas.comprar_divisa(run, nombre, uf["nombre"], cantidad, uf["valor"])

        if opcion == "4":
            run = input("\nRun: ")
            divisas.info_compra_divisas(run)

        if opcion == "5":
            divisas.listar_divisas()

        if opcion == "6":
            respuesta = input("\nSí para hacer commit: ")
            if respuesta.lower() in ("sí", "si", "s"):
                divisas.commit()
                print("\nCommit realizado.")
            else:
                print("\nCommit descartado.")

        if opcion == "7":
            print("\nSaliendo...")
            break

URL = "http://www.mindicador.cl/api"

class ConexionBD:
    def __init__(self, host, user, password, db):
        try:
            self.connection = pymysql.connect(
                host=host,
                user=user,
                passwd=password,
                db=db
            )
            self.cursor = self.connection.cursor()
        except pymysql.Error as e:
           error(e)
           exit(1)

    def commit(self):
        try:
            self.connection.commit()
        except pymysql.Error as e:
            error(e)

class compraDivisas(ConexionBD):
    folio: int
    run_persona: str
    nombre_persona: str
    fecha: str
    tipo_moneda: str
    valor_moneda: float
    cantidad_divisas: float

    def comprar_divisa(self, run, nombre, tipo_moneda, cantidad_divisas, precio_divisa):
        consulta = f"INSERT INTO tb_compradivisas VALUES (NULL, '{run}', '{nombre}', DATE_FORMAT(NOW(), '%d-%m-%Y %H:%i:%s'), '{tipo_moneda}', {cantidad_divisas}, {precio_divisa});"
        self.cursor.execute(consulta)

    def info_compra_divisas(self, run):
        consulta = f"SELECT runPersona, fecha, nombrePersona, tipoMoneda, precioDivisa, cantidadDivisa, ROUND(precioDivisa * cantidadDivisa, 2) FROM tb_compradivisas WHERE runPersona = '{run}';"
        self.cursor.execute(consulta)
        if self.cursor.rowcount > 0:
            divisas = self.cursor.fetchall()
            for i, d in enumerate(divisas):
                if i == 0:
                    print("\n", "".center(30, "-"), sep="")
                print(f"Transacción {i + 1}.")
                print(f"Fecha:             {d[1]}")
                print(f"Run:               {d[0]}")
                print(f"Nombre:            {d[2]}")
                print(f"Tipo moneda:       {d[3]}")
                print(f"Cantidad comprada: {d[5]}")
                print(f"Precio moneda:     {d[4]} CLP")
                print(f"Precio en CLP:     {d[6]}")
                if i != len(divisas) - 1:
                    print()
                else:
                    print("".center(30, "-"))
        else:
            print("\nNo hay divisas.")

    def listar_divisas(self):
        consulta = "SELECT runPersona, fecha, nombrePersona, tipoMoneda, precioDivisa, cantidadDivisa, ROUND(precioDivisa * cantidadDivisa, 2) FROM tb_compradivisas;"
        self.cursor.execute(consulta)
        if self.cursor.rowcount > 0:
            divisas = self.cursor.fetchall()
            for i, d in enumerate(divisas):
                if i == 0:
                    print("\n", "".center(30, "-"), sep="")
                print(f"Transacción {i + 1}.")
                print(f"Fecha:             {d[1]}")
                print(f"Run:               {d[0]}")
                print(f"Nombre:            {d[2]}")
                print(f"Tipo moneda:       {d[3]}")
                print(f"Cantidad comprada: {d[5]}")
                print(f"Precio moneda:     {d[4]} CLP")
                print(f"Precio en CLP:     {d[6]}")
                if i != len(divisas) - 1:
                    print()
                else:
                    print("".center(30, "-"))
        else:
            print("\nNo hay divisas.")

def error(e):
    print(f"\nError{e.args[0]}: {e.args[1]}")

if __name__ == "__main__":
    main()