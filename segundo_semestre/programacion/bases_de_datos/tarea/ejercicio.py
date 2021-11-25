import pymysql
from sys import exit


def error(e):
    print(f"Error {e.args[0]}: {e.args[1]}")


def menu():
    print("\n1 - Buscar vehículo")
    print("2 - Listar vehículos")
    print("3 - Insertar / actualizar vehículo")
    print("4 - Eliminar vehículo")
    print("5 - Realizar commit")
    print("6 - Salir")


class ConexionBD:
    def __init__(self):
        try:
            print("Iniciando conexión en localhost en la base de datos"
                " bd_ejercicio1.")
            self.connection = pymysql.connect(
                host="localhost",
                user="root",
                passwd="",
                db="bd_ejercicio1"
            )
            self.cursor = self.connection.cursor()
            print("Conexión exitosa.")
        except pymysql.Error as e:
            error(e)
            print("Finalizando sesión...")
            exit(1)

    def listar_vehiculos(self):
        try:
            consulta = "select * from tb_vehiculo;"
            self.cursor.execute(consulta)
            if self.cursor.rowcount > 0:
                vehiculos = self.cursor.fetchall()
                print("\n", "".center(30, "-"), sep="")
                for i, vehiculo in enumerate(vehiculos):
                    print(f"Vehículo {i + 1}.")
                    print(f"Patente: {vehiculo[0]}")
                    print(f"Marca:   {vehiculo[1]}")
                    print(f"Modelo:  {vehiculo[2]}")
                    print(f"Año:     {vehiculo[3]}")
                    if i != len(vehiculos) - 1:
                        print()
                print("".center(30, "-"))
            else:
                print("\nNo hay vehículos que mostrar.")
        except pymysql.Error as e:
            error(e)

    def buscar_vehiculo(self, patente):
        try:
            consulta = f"select marca, modelo, anio from tb_vehiculo \
                where patente = '{patente}';"
            self.cursor.execute(consulta)
            vehiculo = self.cursor.fetchone()
            if self.cursor.rowcount == 1:
                print("\nVehículo encontrado.")
                print("".center(30, "-"))
                print(f"Marca:   {vehiculo[0]}")
                print(f"Modelo:  {vehiculo[1]}")
                print(f"Año:     {vehiculo[2]}")
                print("".center(30, "-"))
            else:
                print("\nVehículo no encontrado.")
        except pymysql.Error as e:
            error(e)

    def eliminar_vehiculo(self, patente):
        try:
            consulta = f"select patente from tb_vehiculo \
                where patente = '{patente}';"
            self.cursor.execute(consulta)
            if self.cursor.rowcount == 1:
                consulta = f"delete from tb_vehiculo where patente \
                    = '{patente}';"
                self.cursor.execute(consulta)
                print("\nVehículo eliminado correctamente.")
            else:
                print("\nNo existe el vehículo.")
        except pymysql.Error as e:
            error(e)

    def insertar_actualizar_vehiculo(self, patente, marca, modelo, año):
        try:
            consulta = f"select patente from tb_vehiculo where patente \
                = '{patente}';"
            self.cursor.execute(consulta)
            if self.cursor.rowcount == 1:
                consulta = f"update tb_vehiculo set marca = '{marca}', modelo \
                    = '{modelo}', anio = '{año}' where patente = '{patente}';"
                self.cursor.execute(consulta)
                print("\nVehículo actualizado.")
            else:
                consulta = f"insert into tb_vehiculo values('{patente}', \
                    '{marca}', '{modelo}', {año});"
                self.cursor.execute(consulta)
                print("\nVehículo ingresado.")
        except pymysql.Error as e:
            error(e)

    def commit(self):
        try:
            print("\nIniciando commit...")
            self.connection.commit()
            print("Commit finalizado.")
        except pymysql.Error as e:
            error(e)


bd = ConexionBD()

estado = True

while(estado):
    menu()
    opcion = input("\nIngrese una opción: ")

    # Buscar vehículo
    if opcion == "1":
        print("\nBuscar vehículo.")
        patente = input("Patente: ")
        bd.buscar_vehiculo(patente)

    # Listar vehículos
    elif opcion == "2":
        print("\nListar vehículos.")
        bd.listar_vehiculos()

    # Insertar / actualizar vehículo
    elif opcion == "3":
        print("\nInsertar / actualizar vehículo.")
        patente = input("Patente: ")
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        año = input("Año: ")
        bd.insertar_actualizar_vehiculo(patente, marca, modelo, año)

    # Eliminar vehículo
    elif opcion == "4":
        print("\nEliminar vehículo.")
        patente = input("Patente: ")
        bd.eliminar_vehiculo(patente)

    # Realizar commit
    elif opcion == "5":
        menu()

    # Salir
    elif opcion == "6":
        estado = False
        print("\nSaliendo...")

    else:
        print("\nOpción no válida.")
