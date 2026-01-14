import mysql.connector

try:
    conexion = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "admin",
        database="split_fiction"
    )

    if conexion.is_connected():
        print("¡Conexión exitosa a la base de datos!")

        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM characters")
        registro = cursor.fetchone()
        print("Conectado a: {}".format(registro))

except mysql.connector.Error as error:
    print("Error al conectar: {}".format(error))

finally:
    if "conexion" in locals() and conexion.is_connected():
        conexion.close()
        print("Conexion")