# Hecho por Gabriel Barrientos

import pymysql
from sys import exit

def error(error):
    print(f"{error.args[0]}: {error.args[1]}")

class ConexionBD:
    host: str
    user: str
    password: str
    db: str

    def __init__(self, host, user, password, db) -> None:
        self.host = host
        self.user = user
        self.password = password
        self.db = db

    def conectar_bd(self) -> str:
        try:
            self.connection = pymysql.connect(
                host=self.host,
                user=self.user,
                passwd=self.password,
                db=self.db
            )
            self.cursor = self.connection.cursor()
            print("Conexión exitosa.")
        except pymysql.Error as e:
            error(e)
            print("Conexión fallida, inténtelo de nuevo.")
            exit(1)


class Postulante(ConexionBD):
    run: str
    nombres: str
    apellidos: str
    correo: str
    telefono: int
    direccion: str
    comuna: str
    provincia: str
    region: str
    profesion: str
    clave: str

    def __init__(self, host, user, password, db) -> None:
        super().__init__(host, user, password, db)

    def gestionar_registro_postulante(self, run, nombres, apellidos, correo, telefono, direccion
        , comuna, provincia, region, profesion, clave):
        try:
            consulta = f"SELECT run FROM tb_postulante WHERE run = '{run}';"
            self.cursor.execute(consulta)
            if self.cursor.rowcount == 1:
                # Actualizar
                consulta = f"UPDATE tb_postulante SET nombres = '{nombres}', apellidos = '{apellidos}'"\
                f", correo = '{correo}', telefono = {telefono}, direccion = '{direccion}'"\
                f", comuna = '{comuna}', provincia = '{provincia}', region = '{region}'"\
                f", profesion = '{profesion}', clave = '{clave}' WHERE run = '{run}';"
                self.cursor.execute(consulta)
                print("\nRegistro actualizado.")
            else:
                # Insertar
                consulta = f"INSERT INTO tb_postulante VALUES('{run}', '{nombres}'"\
                f", '{apellidos}', '{correo}', {telefono}, '{direccion}', '{comuna}', '{provincia}'"\
                f", '{region}', '{profesion}', '{clave}');"
                self.cursor.execute(consulta)
                print("\nRegistro insertado.")
        except pymysql.Error as e:
            error(e)

    def autentificar_postulante(self, run, clave):
        try:
            consulta = f"SELECT run, clave FROM tb_postulante WHERE run = '{run}' AND clave = '{clave}';"
            self.cursor.execute(consulta)
            if self.cursor.rowcount == 1:
                consulta = f"SELECT CONCAT(nombres, ' ', apellidos), telefono"\
                f", CONCAT(direccion, ', ', comuna, ', ', provincia, ', ', region)"\
                f", profesion FROM tb_postulante WHERE run = '{run}' AND clave = '{clave}';"
                self.cursor.execute(consulta)
                postulante = self.cursor.fetchone()
                print(f"\nNombre:    {postulante[0]}")
                print(f"Teléfono:  {postulante[1]}")
                print(f"Dirección: {postulante[2]}")
                print(f"Profesión: {postulante[3]}")
            else:
                print("\nUsuario y/o contraseña incorrectos.")
        except pymysql.Error as e:
            error(e)

    def buscar_postulante(self, run):
        try:
            consulta = f"SELECT run FROM tb_postulante WHERE run = '{run}';"
            self.cursor.execute(consulta)
            if self.cursor.rowcount == 1:
                print("\nPostulante encontrado.")
                consulta = f"SELECT run, nombres, apellidos, correo, telefono, direccion, comuna, provincia"\
                f", region, profesion FROM tb_postulante WHERE run = '{run}';"
                self.cursor.execute(consulta)
                postulante = self.cursor.fetchone()
                print(f"Run:       {postulante[0]}")
                print(f"Nombres:   {postulante[1]}")
                print(f"Apellidos: {postulante[2]}")
                print(f"Correo:    {postulante[3]}")
                print(f"Teléfono:  {postulante[4]}")
                print(f"Dirección: {postulante[5]}")
                print(f"Comuna:    {postulante[6]}")
                print(f"Provincia: {postulante[7]}")
                print(f"Región:    {postulante[8]}")
                print(f"Profesión: {postulante[9]}")
            else:
                print("\nNo existe el postulante.")
        except pymysql.Error as e:
            error(e)

    def listar_postulantes(self):
        try:
            consulta = "SELECT run, nombres, apellidos, correo, telefono, direccion, comuna, provincia"\
            ", region, profesion FROM tb_postulante;"
            self.cursor.execute(consulta)
            postulantes = self.cursor.fetchall()
            if self.cursor.rowcount > 0:
                for i, postulante in enumerate(postulantes):
                    if i == 0:
                        print("\n", "".center(70, "-"), sep="")
                    print(f"Postulante {i + 1}.")
                    print(f"Run:       {postulante[0]}")
                    print(f"Nombres:   {postulante[1]}")
                    print(f"Apellidos: {postulante[2]}")
                    print(f"Correo:    {postulante[3]}")
                    print(f"Teléfono:  {postulante[4]}")
                    print(f"Dirección: {postulante[5]}")
                    print(f"Comuna:    {postulante[6]}")
                    print(f"Provincia: {postulante[7]}")
                    print(f"Región:    {postulante[8]}")
                    print(f"Profesión: {postulante[9]}")
                    if i != len(postulantes) - 1:
                        print()
                print("".center(70, "-"))
            else:
                print("\nNo hay ningún postulante.")
        except pymysql.Error as e:
            error(e)

    def eliminar_postulante(self, run, clave):
        try:
            consulta = f"SELECT run, clave FROM tb_postulante WHERE run = '{run}' AND clave = '{clave}';"
            self.cursor.execute(consulta)
            if self.cursor.rowcount == 1:
                consulta = f"DELETE FROM tb_postulante WHERE run = '{run}' AND clave = '{clave}';"
                self.cursor.execute(consulta)
                print("\nPostulante eliminado.")
            else:
                print("\nNo existe tal participante.")
        except pymysql.Error as e:
            error(e)

    def commit(self):
        try:
            self.connection.commit()
            print("\nCommit realizado.")
        except pymysql.Error as e:
            error(e)


postulante = Postulante("localhost", "root", "", "certamenPoo_3")
postulante.conectar_bd()

while True:
    print("\n1 - Gestionar registro de postulante.")
    print("2 - Autentificar postulante.")
    print("3 - Buscar postulante.")
    print("4 - Listar postulantes.")
    print("5 - Eliminar postulante.")
    print("6 - Realizar commit.")
    print("7 - Salir del programa.")
    opcion = input("\nIngrese una opción: ")

    if opcion == "1":
        run = input("\nRun:       ")
        nombres = input("Nombres:   ")
        apellidos = input("Apellidos: ")
        correo = input("Correo:    ")
        telefono = input("Teléfono:  ")
        direccion = input("Dirección: ")
        comuna = input("Comuna:    ")
        provincia = input("Provincia: ")
        region = input("Región:    ")
        profesion = input("Profesión: ")
        clave = input("Clave:     ")
        postulante.gestionar_registro_postulante(run, nombres, apellidos, correo, telefono, direccion, comuna, provincia, region, profesion, clave)

    elif opcion == "2":
        run = input("\nRun:   ")
        clave = input("Clave: ")
        postulante.autentificar_postulante(run, clave)

    elif opcion == "3":
        run = input("\nRun: ")
        postulante.buscar_postulante(run)

    elif opcion == "4":
        postulante.listar_postulantes()

    elif opcion == "5":
        run = input("\nRun:   ")
        clave = input("Clave: ")
        postulante.eliminar_postulante(run, clave)

    elif opcion == "6":
        seguro = input("\nEstá a punto de realizar un commit, escriba sí para confirmar: ")
        if seguro.lower() in ("sí", "si", "s"):
            postulante.commit()
        else:
            print("\nCommit descartado.")

    elif opcion == "7":
        print("\nGracias por usar mi programa.")
        print("Saliendo...")
        break

    else:
        print("\nOpción no válida.")