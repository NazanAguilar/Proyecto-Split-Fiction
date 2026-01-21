import pymysql
from distutils import util

"""
# Configuración de conexión En local
db_config = {
    'host': 'localhost',
    'user': 'Nazan',
    'password': 'Pacman36575681',
    'database': 'split_fiction',
}

"""

# Configuración de conexión En local
db_config = {
    'host': 'localhost',
    'user': 'Nazan',
    'password': 'Pacman36575681',
    'database': 'split_fiction',
}


# Configuración de conexión Servidor en nube
# db_config = {
#     'host': '127.0.0.1',  # ieticloudpro.ieti.cat
#     'user': 'equipo7',
#     'password': 'P@ssw0rd',
#     'database': 'equipo7_SplitFiction',
#     'puerto': 3307
# }

def connect_to_database():
    """Establece una conexión con la base de datos MySQL."""
    try:
        # Crear la conexión
        connection = pymysql.connect(
            host=db_config['host'],
            user=db_config['user'],
            password=db_config['password'],
            database=db_config['database'],
            # port=db_config['puerto']
        )

        print("Conectado a la base de datos")
        return connection
    except pymysql.MySQLError as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None


def close_connection(connection):
    """Cierra la conexión con la base de datos."""
    if connection:
        connection.close()
        print("Conexión cerrada.")


def execute_query(connection, query, params=None):
    """Ejecuta una consulta SQL y devuelve los resultados."""
    try:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:  # Usar DictCursor
            cursor.execute(query, params)

            if query.strip().upper().startswith(("INSERT", "UPDATE", "DELETE")):
                connection.commit()
            results = cursor.fetchall()
            return results
    except pymysql.MySQLError as e:
        print(f"Error al ejecutar la consulta: {e}")
        return None


def execute(self, func, args, msg=None, level=1):
    util.execute(func, args, msg, dry_run=self.dry_run)


# connect_to_database()


portada = (
    "****************************************************************************************",
    "|                                                                                      |",
    "|                                                                                      |",
    "|    _________      .__  .__  __    ___________.__        __  .__                      |",
    "|   /   _____/_____ |  | |__|/  |_  \_   _____/|__| _____/  |_|__| ____   ____         |",
    "|   \_____  \/____ \|  | |  \   __\  |    __)  |  |/ ___\   __\  |/  _ \ /     \       |",
    "|   /        \  |_> >  |_|  ||  |    |     \   |  \  \___|  | |  (  <_> )   |  \       |",
    "|  /_______  /   __/|____/__||__|    \___  /   |__|\___  >__| |__|\____/|___|  /       |",
    "|          \/|__|                        \/            \/                    \/        |",
    "|                                                                                      |",
    "|                        1) New User     2) Conect     3) Exit                         |",
    "****************************************************************************************")


pantalla_principal = (
    "****************************************************************************************",
    "|                                                                                      |",
    "|      1) Play History                        (\\                                       |",
    "|                                              \\'\\                                     |",
    "|      2) Replay Mode                          \\'\\     __________                      |",
    "|                                               / '|   ()_________)                    |",
    "|      3) Reports                              \\ '/    \\ ~~~~~~~~ \\                    |",
    "|                                               \\       \\ ~~~~~~   \\                   |",
    "|      4) Log Out                               ==).      \\__________\\                 |",
    "|                                               (__)       ()__________)               |",
    "|                                                                                      |",
    "****************************************************************************************")


for linea in pantalla_principal:
    print(linea)

for linea in portada:
    print(linea)

input(">Option --> ")
input(">Escribe tu nombre de usuario--> ")
input(">Escribe tu contraseña--> ")