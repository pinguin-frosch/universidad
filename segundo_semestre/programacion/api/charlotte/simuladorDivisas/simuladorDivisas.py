#tarea creada por Charlotte Rodriguez
import pymysql
import requests
from sys import exit

class ConexionBD:
    def __init__(self, servidor, usuario, contraseña, baseDeDatos):
        try:
            self.connection = pymysql.connect(
                host=servidor,
                user=usuario,
                passwd=contraseña,
                db=baseDeDatos
            )
            self.cursor = self.connection.cursor()
        except pymysql.Error as e:
           error(e)
           exit(1)

class compraDivisas(ConexionBD):
    folio = 0
    runPersona = ""
    nombrePersona = ""
    fecha = ""
    tipoMoneda = ""
    valorMoneda = 0
    cantidadDivisas = 0

    def comprarDivisa(self, run, nombre, tipoMoneda, cantidadDivisas, precioDivisa):
        consulta = f"insert into tb_compradivisas values (null, '{run}', '{nombre}', now(), '{tipoMoneda}', {cantidadDivisas}, {precioDivisa})"
        self.cursor.execute(consulta)

    def infoCompraDivisas(self, run):
        consulta = f"select runPersona, fecha, nombrePersona, tipoMoneda, precioDivisa, cantidadDivisa, precioDivisa * cantidadDivisa from tb_compradivisas where runPersona = '{run}'"
        self.cursor.execute(consulta)
        if self.cursor.rowcount > 0:
            divisas = self.cursor.fetchall()
            for d in divisas:
                print(f"fecha: {d[1]}")
                print(f"run: {d[0]}")
                print(f"nombre: {d[2]}")
                print(f"tipo moneda: {d[3]}")
                print(f"cantidad: {d[5]}")
                print(f"precio moneda: {d[4]} clp")
                print(f"precio total: {d[6]}")
                print()
        else:
            print("\nno hay divisas.")

    def listarDivisas(self):
        consulta = "select runPersona, fecha, nombrePersona, tipoMoneda, precioDivisa, cantidadDivisa, precioDivisa * cantidadDivisa from tb_compradivisas"
        self.cursor.execute(consulta)
        if self.cursor.rowcount > 0:
            divisas = self.cursor.fetchall()
            for d in divisas:
                print(f"fecha: {d[1]}")
                print(f"run: {d[0]}")
                print(f"nombre: {d[2]}")
                print(f"tipo moneda: {d[3]}")
                print(f"cantidad: {d[5]}")
                print(f"precio moneda: {d[4]} clp")
                print(f"precio total: {d[6]}")
                print()
        else:
            print("\nno hay divisas.")

def error(e):
    print(f"\nError{e.args[0]}: {e.args[1]}")

url = "http://www.mindicador.cl/api"
response = requests.get(url).json()
euro = response["euro"]
dolar = response["dolar"]
gestor = compraDivisas("localhost", "root", "", "bd_divisas")

while True:
    print("\n1) compra de dolares")
    print("2) comprar de euros")
    print("3) listar compras por usuario")
    print("4) listar las compras")
    print("5) salir")

    opcion = input("\nelija una opcion: ")

    if opcion == "1":
        run = input("\nrun: ")
        nombre = input("nombre: ")
        cantidad = input("cantidad comprada: ")
        gestor.comprarDivisa(run, nombre, dolar["nombre"], cantidad, dolar["valor"])
    if opcion == "2":
        run = input("\nrun: ")
        nombre = input("nombre: ")
        cantidad = input("cantidad comprada: ")
        gestor.comprarDivisa(run, nombre, euro["nombre"], cantidad, euro["valor"])
    if opcion == "3":
        run = input("\nrun: ")
        gestor.infoCompraDivisas(run)
    if opcion == "4":
        gestor.listarDivisas()
    if opcion == "5":
        print("\ngracias por usar el programa :D")
        break