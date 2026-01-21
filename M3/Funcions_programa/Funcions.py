from Funcions_programa.BBDD import * 
from Funcions_programa.Variables import *

#FUNCIONES BBDD
def get_adventures_with_chars():
    """Consulta las aventuras y sus personajes asociados."""
    query = "SELECT * FROM adventures;"
    connection = connect_to_database()

    if connection:
        results = execute_query(connection, query)
        if results:
            # Construimos el diccionario base
            adventures_dict = {}
            for row in results:
                adventures_dict[row['id_adventures']] = {
                    "name": row['name'],
                    "description": row['description'],
                    "characters": [] # Lista vacía para cada aventura
                }
            
            # Segunda consulta para los personajes
            query_char = "SELECT fk_adventure_characters_characters " + \
                         "FROM adventure_characters " + \
                         "WHERE fk_adventure_characters_adventures = %s;"

            for id_adv in adventures_dict:
                char_results = execute_query(connection, query_char, (id_adv,))
                if char_results:
                    for char_row in char_results:
                        adventures_dict[id_adv]["characters"].append(
                            char_row['fk_adventure_characters_characters']
                        )
            
            close_connection(connection)
            return adventures_dict
            
        close_connection(connection)
        return results
    return {}

def get_characters():
    query = "SELECT * FROM characters;"
    connection = connect_to_database()
    if connection:
        results = execute_query(connection, query)
        close_connection(connection)
        if results:
            char_dict = {}
            for row in results:
                char_dict[row['id_characters']] = row['name']
                
            return char_dict
    return {}

def getIdGames():
    query = "SELECT * FROM game;"
    connection = connect_to_database()
    if connection:
        results = execute_query(connection, query)
        close_connection(connection)
        if results:
            id_game_dict = ()
            for row in results:
                id_game_dict += (row['id_game'],)
                
            return id_game_dict
    return {}

def insertCurrentGame(idGame,idUser,isChar,idAdventure):
    query = "INSERT INTO game ( fk_game_users,fk_game_characters,fk_game_adventures,game_date,date_reg,user_reg)" \
    " VALUES (%s, %s, %s, NOW(), NOW(), %s);"

    connection = connect_to_database()
    execute_query(connection, query, (idGame, isChar, idAdventure, idUser))
    if connection:
        connection.commit() 
        close_connection(connection)

def getUsers():
    query = "SELECT * FROM users;"  
    connection = connect_to_database()

    if connection:
        results = execute_query(connection, query)
        close_connection(connection)
        if results:
            users_dict = {}

            for row in results:
                users_dict[row['username']] = {
                    "password": row['password'],
                    "idUser": row['id_users']
                } 

            return users_dict
        return {}
    return {}

def getUserIds():
    query = "SELECT * FROM users;"  
    connection = connect_to_database()

    if connection:
        results = execute_query(connection, query)
        close_connection(connection)
        if results:
            user_list_ids = [[],[]]

            for row in results:
                user_list_ids[0].append(row['username'])
                user_list_ids[1].append(row['id_users'])

            return user_list_ids
        return {}
    return {}

def insertUser(id,name,pwd):
    pwd = cifrar(pwd)
    connection = connect_to_database()
    
    if connection:
        id_actual = id
        insert = False
        while not insert:
            # 1. Comprobamos si el ID ya existe
            query_check = "SELECT 1 FROM users WHERE id_users = %s;"
            exists = execute_query(connection, query_check, (id_actual,))

            if not exists:
                query = "INSERT INTO users (id_users, username, password, date_reg, user_reg)" \
                " VALUES (%s, %s, %s, NOW(), %s);"
                execute_query(connection, query, (id_actual, name, pwd, id_actual))
                connection.commit() 
                insert = True
                print("User {} Created".format(name)) 
                input()

            else:
                id_actual = id_actual + 1
        close_connection(connection)
        return
    return None

def checkUserbdd(user,password):
    users_dict = getUsers()
    comp_pass = ""

    if not user in users_dict:
        return 0
    else:
        for user_dict in users_dict:
            if user_dict == user:
                comp_pass = descifrar(users_dict[user_dict]["password"])
                break
        if comp_pass == password:
            return 1
        else:
            return -1 
    

#FUNCIONES PROGRAMA

def formatText(text,lenLine,split):
    resultado = ""
    linia = ""
    if len(text) < lenLine:
        return text
    else:
        palabras = text.split(split)
        for palabra in palabras:
            prevision = len(linia + palabra)
            if prevision > lenLine:

                if resultado != "":
                    resultado += "\n" + linia
                else:
                    resultado += linia
                linia = palabra + " "
            else:
                linia += palabra + " "
        
        resultado += "\n"+linia
    
        return resultado

def getHeader(text):
    resultado = "*"*105 + "\n" + text.center(105,"=") + "\n" + "*"*105

    return resultado
     
def getFormatedBodyColumns(tupla_texts,tupla_sizes,margin=0):
    datos = {}
    max_lin = 0
    resultado = ""

    for i in range(len(tupla_texts)):
        datos[len(datos) + 1] = formatText(tupla_texts[i],tupla_sizes[i]-margin,split=" ")
        datos[i+1] = datos[i+1].split("\n")

        if len(datos[i+1]) > max_lin:
            max_lin = len(datos[i+1])

    for i in range(max_lin):
        for num_columna in datos:            
            if i < len(datos[num_columna]):
                if datos[num_columna][i] != "":
                    resultado += datos[num_columna][i].ljust(tupla_sizes[num_columna-1])
            else:
                resultado += " "*tupla_sizes[num_columna-1]
        
        resultado += "\n" 

    return resultado

def getFormatedAdventures():
    cabezera = getHeadeForTableFromTuples(("Id", "Adventure", "Description"), (15, 40, 50), title="Adventures")
    datos = ""
    
    adventures = get_adventures_with_chars()

    for adv_id in adventures:
        id_str = str(adv_id)
        nombre = adventures[adv_id]["name"]
        descripcion = adventures[adv_id]["description"]
        
        columnas = (id_str, nombre, descripcion)
        espaciado = (15, 40, 50)
        datos = datos + getFormatedBodyColumns(columnas, espaciado)
    
    return cabezera + datos

def getHeadeForTableFromTuples(t_name_columns,t_size_columns,title=""):
    resultado = title.center(105,"=") + "\n"*3

    cantidad_columnas = len(t_name_columns)

    for i in range(cantidad_columnas):
        resultado += t_name_columns[i].ljust(t_size_columns[i])
            
    resultado += "\n" + 105*"*" + "\n"
    return resultado

def getTableFromDict(tuple_keys,weigth_of_columns,dict_of_data):
    resultado = ""
    for id in dict_of_data:
        resultado += str(id).ljust(weigth_of_columns[0])
        resultado += dict_of_data[id][tuple_keys[0]].ljust(weigth_of_columns[0])
        resultado += dict_of_data[id][tuple_keys[1]].ljust(weigth_of_columns[1])
        resultado += dict_of_data[id][tuple_keys[2]].ljust(weigth_of_columns[2])
        resultado += str(dict_of_data[id][tuple_keys[3]]).ljust(weigth_of_columns[3]) + "\n"
    
    return resultado

def getOpt(textOpts="",inputOptText="",rangeList=[],dictionary={},exceptions=[]):
    con_lista = True
    elegido = False

    if dictionary != {}:
        con_lista = False
    
    while not elegido:
        print(textOpts)
        opc = input(inputOptText)
        if opc in exceptions or opc == str(exceptions[2]):
            if opc == str(exceptions[2]):
                return int(opc)
            else:
                return opc
        elif not opc.isdigit():
            print("No existe esa opcion")
            input("Enter para continuar")
        else:
            if con_lista == True:
                if int(opc) in rangeList:
                    return int(opc)
                else:
                    print("Fuera de rango")
                    input("Enter para continuar")
            else:
                if opc in dictionary:
                    return dictionary[opc]
                else:
                    print("Fuera de rango")
                    input("Enter para continuar")

def getFormatedTable(queryTable,title=""):
    cabezera = title.center(120,"=") + "\n"
    datos = ""

    for nom_cap in queryTable[0]:
        cabezera += nom_cap.ljust(30)

    cabezera += "\n" + "*"*120 + "\n"

    num_datos = len(queryTable) - 1
    for i in range(num_datos):
        
        id = queryTable[i+1][0]
        paso = queryTable[i+1][1]
        respuesta = queryTable[i+1][2]
        numero = str(queryTable[i+1][3])
        columnas = (id,paso,respuesta,numero)
        espaciado = (30,30,30,30)
        datos += getFormatedBodyColumns(columnas,espaciado,margin=6) + "\n"

    return cabezera + datos

def checkPassword(password):
    mayus = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    minus = "abcdefghijklmnñopqrstuvwxyz"
    num = "1234567890"
    esp = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~¡¿€¬ºª"

    accentos = "áàéèíìóòúùÁÀÉÈÍÌÓÒÚÙ"    

    especial_corr = False
    num_corr = False
    may_corr = False
    min_corr = False
    num_corr = False

    if len(password) < 8 or len(password) > 12:
        print("Length of password is not correct")
        return False
    if " " in password:
        print("Password cannot contain spaces")
        return False
        
    for letra in password:
        if letra in accentos:
            print("Accents are not allowed")
            return False
        if letra in esp:
            especial_corr = True
        if letra in mayus:
            may_corr = True
        if letra in num:
            num_corr = True
        if letra in minus:
            min_corr = True
    if especial_corr == False:
        print("Password has to contain some especial character")
        return False
    if num_corr == False:
        print("Password has to contain some digit")
        return False
    if may_corr == False or min_corr == False:
        print("Password have to include some uppercase and some lowercase")
        return False
    
    return True
        
def checkUser(user):
    accentos = "áàéèíìóòúùÁÀÉÈÍÌÓÒÚÙ"    
    
    if len(user) >= 5 and len(user) <= 12:
        for i in range(len(user)):
            if user[i] in accentos:
                print("Accents are not allowed")
                return False
        if user.isalnum():
            return True
        else:
            print("User have to be alphanumeric")
    else:
        print("Length of username have to be longer than 5 and shorter than 11")

def userExists(user):
    users_dict = getUsers()

    if user in users_dict:
        print("User already in use")
        return True
    else:
        return False

#-----------------PERSONALIZAR----------------------

def cifrar(texto):
    abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz1234567890!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~¡¿€¬ºª"
    resultado = ""
    for caracter in texto:
        if caracter in abecedario:
            posicion = abecedario.index(caracter)
            nueva_posicion = (posicion + 13) % len(abecedario)
            resultado += abecedario[nueva_posicion]
        else:
            resultado += caracter
    return resultado

def descifrar(texto):
    abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz1234567890!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~¡¿€¬ºª"
    resultado = ""
    for caracter in texto:
        if caracter in abecedario:
            posicion = abecedario.index(caracter)
            nueva_posicion = (posicion - 13) % len(abecedario)
            resultado += abecedario[nueva_posicion]
        else:
            resultado += caracter
    return resultado

def login_user(name, pwd):
    """Verifica las credenciales y devuelve los datos del usuario si son correctos."""
    # Primero ciframos la contraseña recibida para compararla con la de la BBDD
    pwd_cifrada = cifrar(pwd)
    
    query = "SELECT * FROM users WHERE username = %s AND password = %s;"
    connection = connect_to_database()
    
    if connection:
        # execute_query ya nos devuelve la lista de resultados (o una lista vacía)
        results = execute_query(connection, query, (name, pwd_cifrada))
        close_connection(connection)
        
        if results:
            # Como username es UNIQUE, solo habrá un resultado (results[0])
            return results[0] 
    
    return None

# =========================
# ORDENACIÓN BURBUJA
# =========================

def bubble_sort_by_date(variable):
    n = len(variable)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Comparamos las fechas (índice 2)
            if variable[j][2] > variable[j + 1][2]:
                variable[j], variable[j + 1] = variable[j + 1], variable[j]

# =========================
# AUTOREPLAY DE PARTIDAS
# =========================

def autoreplay_games(user_id):
    connection = connect_to_database()
    if not connection:
        return

    # Obtener partidas del usuario
    query_games = """
        SELECT g.id_game, g.game_date, a.name
        FROM game g
        JOIN adventures a ON g.fk_game_adventures = a.id_adventures
        WHERE g.fk_game_users = %s
    """
    games = execute_query(connection, query_games, (user_id,))

    if not games:
        print("No tienes partidas guardadas.")
        close_connection(connection)
        return


    # Crear matriz: [num, id_game, fecha, nombre]
    matrix = []
    counter = 1
    for g in games:
        matrix.append([counter, g["id_game"], g["game_date"], g["name"]])
        counter += 1

    # Ordenar por fecha
    bubble_sort_by_date(matrix)

    # Mostrar partidas
    print("\n=== PARTIDAS DISPONIBLES ===")
    for row in matrix:
        print(str(row[0]) + ") " + str(row[3]) + " (" + str(row[2]) + ")")

    # Elegir partida
    try:
        choice = int(input("\nElige una partida: "))
    except ValueError:
        print("Entrada no válida.")
        close_connection(connection)
        return

    selected_game_id = None
    for row in matrix:
        if row[0] == choice:
            selected_game_id = row[1]
            break

    if not selected_game_id:
        print("Selección inválida.")
        close_connection(connection)
        return

    # Autoreplay
    query_replay = """
        SELECT s.description AS step_text,
               d.description AS decision_text,
               d.result_text
        FROM choices c
        JOIN steps s ON c.fk_choices_steps = s.id_steps
        JOIN decisions d ON c.fk_choices_decisions = d.id_decisions
        WHERE c.fk_choices_game = %s
        ORDER BY c.id_choices ASC;
    """
    replay_data = execute_query(connection, query_replay, (selected_game_id,))

    print("\n=== AUTOREPLAY DE LA PARTIDA ===\n")
    if replay_data:
        for r in replay_data:
            print("ESCENA:")
            print(formatText(r["step_text"], 100, ";")) # Usamos tu función de formato
            print("\nDECISIÓN TOMADA: " + str(r["decision_text"]))
            if r["result_text"]:
                print("RESULTADO: " + str(r["result_text"]))
            input("Enter to continue")
            print("\n" + "-"*50 + "\n")
    
    close_connection(connection)

# =========================
# EJECUCIÓN
# =========================

if __name__ == "__main__":
    # Usuario logueado (ejemplo: admin = 1)
    autoreplay_games(user_id=1)