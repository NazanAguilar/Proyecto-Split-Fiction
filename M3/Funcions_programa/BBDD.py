import pymysql
from distutils import util

"""db_config = {
    'host': '127.0.0.1', #ieticloudpro.ieti.cat
    'user': 'equipo7',
    'password': 'P@ssw0rd',
    'database': 'equipo7_SplitFiction',
    'puerto': 3307
}"""


# Configuración de conexión
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'admin',
    'database': 'equipo7_splitfiction',
}

def connect_to_database():
    """Establece una conexión con la base de datos MySQL."""
    try:
        # Crear la conexión
        connection = pymysql.connect(
            host=db_config['host'],
            user=db_config['user'],
            password=db_config['password'],
            database=db_config['database'],
        )

        #print("Conectado a la base de datos")
        return connection
    except pymysql.MySQLError as e:
        print("Error al conectar a la base de datos: {}".format(e))
        return None

def close_connection(connection):
    """Cierra la conexión con la base de datos."""
    if connection:
        connection.close()
        #print("Conexión cerrada.")

def execute_query(connection, query, params = None):
    """Ejecuta una consulta SQL y devuelve los resultados."""
    try:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:  # Usar DictCursor
            cursor.execute(query, params)

            if query.strip().upper().startswith(("INSERT", "UPDATE", "DELETE")):
                connection.commit()
            results = cursor.fetchall()
            return results
    except pymysql.MySQLError as e:
        print("Error al ejecutar la consulta: {}".format(e))
        return None

def execute(self, func, args, msg=None, level=1):
    util.execute(func, args, msg, dry_run=self.dry_run)
