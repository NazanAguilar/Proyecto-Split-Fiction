import pymysql
from distutils import util
from Funcions import cifrar
from Funcions import descifrar

# Configuración de conexión
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'admin',
    'database': 'split_fiction',
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
        print(f"Error al ejecutar la consulta: {e}")
        return None

def execute(self, func, args, msg=None, level=1):
    util.execute(func, args, msg, dry_run=self.dry_run)

def get_characters():
    """Consulta la tabla de Partidas y devuelve los resultados como un diccionario."""
    query = "SELECT * FROM characters;"  # Consulta a la tabla Partidas
    connection = connect_to_database()

    if connection:
        results = execute_query(connection, query)
        close_connection(connection)
        if results:
            # Diccionario con ID_Partida como clave
            partidas_dict = {
                row['id_characters']: row['name']
                 for row in results
            }
            return partidas_dict
        return results
    return {}

def get_users():
    """Consulta la tabla de Partidas y devuelve los resultados como un diccionario."""
    query = "SELECT * FROM users;"  # Consulta a la tabla Partidas
    connection = connect_to_database()

    if connection:
        results = execute_query(connection, query)
        close_connection(connection)
        if results:
            users_dict = {
                row['id_users']: {
                    "username": row['username'],
                    "password": row['password'],
                    "date_reg": row['date_reg'],
                    "user_reg": row['user_reg'],
                    "date_mod": row['date_mod'],
                    "user_mod": row['user_mod']
                } for row in results
            }
            return users_dict
        return results
    return {}

def get_adventures():
    """Consulta la tabla de Partidas y devuelve los resultados como un diccionario."""
    query = "SELECT * FROM adventures;"  # Consulta a la tabla Partidas
    connection = connect_to_database()

    if connection:
        results = execute_query(connection, query)
        close_connection(connection)
        if results:
            adventures_dict = {
                row['id_adventures']: {
                    "name": row['name'],
                    "description": row['description']
                } for row in results
            }            
            
            adventures_dict["characters"] = []
            connection = connect_to_database()

            query = "SELECT fk_adventure_characters_characters from adventure_characters where fk_adventure_characters_adventures = %s;"

            for key in adventures_dict:
                results = execute_query(connection, query, (key))

                adv_characters = [
                                row['fk_adventure_characters_characters']
                                for row in results
                            ]
                
                for character in adv_characters:
                    adventures_dict["characters"].append(character)
        
            return adventures_dict
        return results
    return {}

def add_user(name,pwd):
    pwd = cifrar(pwd)

    query = "INSERT INTO users (username, password, date_reg, user_reg) VALUES (%s, %s, NOW(), (SELECT COUNT(*) + 1 FROM users AS t));"
    connection = connect_to_database()
    results = execute_query(connection, query, (name, pwd))
    if connection:
        connection.commit() 
        close_connection(connection)


dic_users = get_users()

adventures = get_adventures()

characters = get_characters()

print(characters)