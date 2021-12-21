#tarea creada por Charlotte Rodriguez
import requests
import pymysql
from sys import exit

class ConexionBD:
    baseDeDatos = "bd_multass1"
    servidor = "localhost"
    usuario = "root"
    contraseña = ""

    def __init__(self):
        try:
            self.connection = pymysql.connect(
                host=self.servidor,
                passwd=self.contraseña,
                db=self.baseDeDatos,
                user=self.usuario
            )
            self.cursor = self.connection.cursor()
        except pymysql.Error as e:
            print("Error {}: {}".format(e.args[0], e.args[1]))
            exit(1)

class PersonaMulta(ConexionBD):
    run = ""
    nombreInfraccion = ""
    nombreCompleto = ""
    montoUtm = 0
    cantidadUtm = 0

    def getRun(self):
        return self.run

    def getNombreInfraccion(self):
        return self.nombreInfraccion

    def getNombreCompleto(self):
        return self.nombreCompleto

    def getMontoUtm(self):
        return self.montoUtm

    def getCantidadUtm(self):
        return self.cantidadUtm

    def setRun(self, run):
        self.run = run

    def setNombreInfraccion(self, nombreInfraccion):
        self.nombreInfraccion = nombreInfraccion

    def setNombreCompleto(self, nombreCompleto):
        self.nombreCompleto = nombreCompleto

    def setMontoUtm(self, montoUtm):
        self.montoUtm = montoUtm

    def setCantidadUtm(self, cantidadUtm):
        self.cantidadUtm = cantidadUtm

    def insertarMulta(self):
        try:
            consulta = f"insert into tb_personamultas values ('{self.getRun()}', '{self.getNombreCompleto()}', '{self.getNombreInfraccion()}', {self.getCantidadUtm()}, now(), {self.getMontoUtm()})"
            self.cursor.execute(consulta)
        except pymysql.Error as e:
            print("Error {}: {}".format(e.args[0], e.args[1]))

    def listarMultas(self):
        try:
            consulta = "select run, nombres, nombreInfraccion, cantUTM, montoUTM, montoUTM * cantUTM from tb_personamultas"
            self.cursor.execute(consulta)
            if self.cursor.rowcount > 0:
                personas = self.cursor.fetchall()
                print("listando multas")
                for  p in personas:
                    print(f"run: {p[0]}")
                    print(f"nombre: {p[1]}")
                    print(f"infraccion: {p[2]}")
                    print(f"cantidad utm: {p[3]}")
                    print(f"monto utm: {p[4]}")
                    print(f"total: {p[5]}")
                    print()
            else:
                print("\nno hay ninguna multa")
        except pymysql.Error as e:
            print("Error {}: {}".format(e.args[0], e.args[1]))

    def buscarMultas(self, run):
        try:
            consulta = f"select * from tb_personamultas where run = '{run}'"
            self.cursor.execute(consulta)
            if self.cursor.rowcount > 0:
                multas = self.cursor.fetchall()
                print("listando multas")
                for multa in multas:
                    print(f"run: {multa[0]}")
                    print(f"nombre: {multa[1]}")
                    print(f"infraccion: {multa[2]}")
                    print(f"cantidad utm: {multa[3]}")
                    print(f"monto utm: {multa[4]}")
                    print(f"total: {multa[5]}")
                    print()
            else:
                print("\nno hay ninguna multa")
        except pymysql.Error as e:
            print("Error {}: {}".format(e.args[0], e.args[1]))

url = "https://mindicador.cl/api"
response = requests.get(url).json()
valorUtm = response["utm"]["valor"]
personamulta = PersonaMulta()

print("Mini base de datos de multas")

while True:
    print("\n1 - ingresar multa")
    print("2 - listar las multas")
    print("3 - buscar multas")
    print("4 - salir")

    opcion = input("\nelija una opcion: ")

    if opcion == "1":
        run = input("\nrun: ")
        nombreCompleto = input("nombre: ")
        infraccion = input("infraccion: ")
        cantidadUtm = input("cantidad utm: ")
        personamulta.setRun(run)
        personamulta.setNombreCompleto(nombreCompleto)
        personamulta.setNombreInfraccion(infraccion)
        personamulta.setCantidadUtm(cantidadUtm)
        personamulta.setMontoUtm(valorUtm)
        personamulta.insertarMulta()

    elif opcion == "2":
        personamulta.listarMultas()

    elif opcion == "3":
        run = input("\nrun: ")
        personamulta.buscarMultas(run)

    elif opcion == "4":
        print("gracias por usar mi programa :D")
        break

    else:
        print("\nno existe esa opcion")