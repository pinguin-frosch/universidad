import requests
import pymysql
import json
import sys

def error(e):
    print(f"Error {e.args[0]}: {e.args[1]}.")

def main():
    class ConexionBD:
        bd = "bd_multass1"
        server = "localhost"
        user = "root"
        password = ""

        def __init__(self):
            try:
                self.connection = pymysql.connect(
                    host=self.server,
                    passwd=self.password,
                    db=self.bd,
                    user=self.user
                )
                self.cursor = self.connection.cursor()
            except pymysql.Error as e:
                error(e)
                sys.exit(1)

    class PersonaMulta(ConexionBD):
        run: str
        nombre_completo: str
        nombre_infraccion: str
        cantidad_utm: float
        monto_utm: float

        def get_run(self):
            return self.run

        def set_run(self, run):
            self.run = run

        def get_nombre_completo(self):
            return self.nombre_completo

        def set_nombre_completo(self, nombre_completo):
            self.nombre_completo = nombre_completo

        def get_nombre_infraccion(self):
            return self.nombre_infraccion

        def set_nombre_infraccion(self, nombre_infraccion):
            self.nombre_infraccion = nombre_infraccion

        def get_cantidad_utm(self):
            return self.cantidad_utm

        def set_cantidad_utm(self, cantidad_utm):
            self.cantidad_utm = cantidad_utm

        def get_monto_utm(self):
            return self.monto_utm

        def set_monto_utm(self, monto_utm):
            self.monto_utm = monto_utm

        def insertar_multa(self):
            try:
                consulta = f"insert into tb_personamultas values ('{self.get_run()}', '{self.get_nombre_completo()}', '{self.get_nombre_infraccion()}', {self.get_cantidad_utm()}, now(), {self.get_monto_utm()});"
                self.cursor.execute(consulta)
            except pymysql.Error as e:
                error(e)

        def listar_multas(self):
            try:
                consulta = "select run, nombres, nombreInfraccion, cantUTM, montoUTM, montoUTM * cantUTM from tb_personamultas;"
                self.cursor.execute(consulta)
                if self.cursor.rowcount > 0:
                    personas = self.cursor.fetchall()
                    for i, p in enumerate(personas):
                        if i == 0:
                            print("\n" + "".center(65, "-"), sep="")
                        print(f"Run: {p[0]}")
                        print(f"Nombre: {p[1]}")
                        print(f"Infracción: {p[2]}")
                        print(f"Cantidad UTM: {p[3]} UTM")
                        print(f"Monto UTM: {p[4]} CLP")
                        print(f"Total: {p[5]} CLP")
                        if i != len(personas) - 1:
                            print()
                        else:
                            print("".center(65, "-"))
                else:
                    print("\nNo hay ninguna multa.")
            except pymysql.Error as e:
                error(e)

        def buscar_multas(self, run):
            try:
                consulta = f"select * from tb_personamultas where run = '{run}';"
                self.cursor.execute(consulta)
                if self.cursor.rowcount > 0:
                    multas = self.cursor.fetchall()
                    for i, m in enumerate(multas):
                        if i == 0:
                            print("\n" + "".center(65, "-"), sep="")
                        print(f"Fecha: {m[4]}")
                        print(f"Run: {m[0]}")
                        print(f"Nombre: {m[1]}")
                        print(f"Infracción: {m[2]}")
                        print(f"Cantidad UTM: {m[3]}")
                        print(f"Monto UTM: {m[5]}")
                        if i != len(multas) - 1:
                            print()
                        else:
                            print("".center(65, "-"))
                else:
                    print("\nNo hay ninguna multa.")
            except pymysql.Error as e:
                error(e)

        def commit(self):
            self.connection.commit()

    url = "https://mindicador.cl/api"
    response = json.loads(requests.get(url).text.encode("utf-8"))
    utm = response["utm"]["valor"]
    p1 = PersonaMulta()

    print("Programa para gestionar multas.")

    while True:
        print("\n1 - Insertar multa")
        print("2 - Listar multas")
        print("3 - Buscar multas")
        print("4 - Commit")
        print("5 - Salir")

        opcion = input("\nEscoja una opción: ")

        if opcion == "1":
            run = input("\nRun: ")
            nombre_completo = input("Nombre: ")
            infraccion = input("Infracción: ")
            while True:
                cantidad_utm = input("Cantidad UTM: ")
                try:
                    cantidad_utm = float(cantidad_utm)
                    break
                except ValueError:
                    print("Ingrese un valor correcto.")
            p1.set_run(run)
            p1.set_nombre_completo(nombre_completo)
            p1.set_nombre_infraccion(infraccion)
            p1.set_cantidad_utm(cantidad_utm)
            p1.set_monto_utm(utm)
            p1.insertar_multa()

        elif opcion == "2":
            p1.listar_multas()

        elif opcion == "3":
            run = input("\nRun: ")
            p1.buscar_multas(run)

        elif opcion == "4":
            respuesta = input("\nSí para hacer un commit: ")
            if respuesta.lower() in ("s", "si", "sí"):
                p1.commit()
                print("\nCommit exitoso.")
            else:
                print("\nCommit descartado.")

        elif opcion == "5":
            print("Saliendo...")
            break

        else:
            print("\nOpción no válida.")

if __name__ == "__main__":
    main()