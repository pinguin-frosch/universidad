from errno import ESHUTDOWN
import pymysql


def error(error):
    print(f"{error.args[0]}: {error.args[1]}")


def main():
    con = ConexionBD('localhost', 'usuario_normal',
                     'contrasena_normal', 'biblioteca')
    con.listar_editoriales()


class ConexionBD:
    def __init__(self, host, user, passwd, db):
        try:
            print(
                f"\nIniciando conexión en {host} en la base de datos {db}...")
            self.connection = pymysql.connect(
                host=host,
                user=user,
                passwd=passwd,
                db=db
            )
            self.cursor = self.connection.cursor()
            print("Conexión exitosa.")
        except pymysql.Error as e:
            print("Finalizando sesión...")
            exit(1)

    def listar_editoriales(self):
        try:
            consulta = f"SELECT * FROM editorial;"
            self.cursor.execute(consulta)
            editoriales = self.cursor.fetchall()
            if self.cursor.rowcount > 0:
                for editorial in editoriales:
                    print(f'Id editorial:     {editorial[0]} 🍁')
                    print(f'Nombre:           {editorial[1]} 🎃')
                    print(f'Correo:           {editorial[2]} 🌰')
                    print(f'Telefono:         {editorial[3]} 🍂')
                    print(f'Fecha fundacion:  {editorial[4]} 🏮')
                    print()
            else:
                print('🥸 no hay registros...')
        except pymysql.Error as e:
            error(e)


if __name__ == "__main__":
    main()
