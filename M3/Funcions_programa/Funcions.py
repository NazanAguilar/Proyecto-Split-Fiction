from Funcions_programa.BBDD import * 
from Funcions_programa.Variables import *
import os

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

def insertUser(id, name, pwd):
    pwd = cifrar(pwd)
    connection = connect_to_database()

    if not connection:
        return False

    try:
        # Comprobar si el username ya existe
        query_user = "SELECT 1 FROM users WHERE username = %s;"
        exists_user = execute_query(connection, query_user, (name,))

        if exists_user:
            return False   # Usuario duplicado

        id_actual = id
        while True:
            # Comprobar si el ID existe
            query_check = "SELECT 1 FROM users WHERE id_users = %s;"
            exists_id = execute_query(connection, query_check, (id_actual,))

            if not exists_id:
                query = """
                    INSERT INTO users (id_users, username, password, date_reg, user_reg)
                    VALUES (%s, %s, %s, NOW(), %s);
                """
                execute_query(connection, query, (id_actual, name, pwd, id_actual))
                connection.commit()
                return True   # Usuario creado correctamente

            id_actual += 1

    except Exception as e:
        print("Error creating user:", e)
        return False

    finally:
        close_connection(connection)


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

def getReport1():
    """Informe 1: Respuesta más usada"""
    query = "SELECT a.name AS 'aventura', s.id_steps, LEFT(s.description, 50) AS 'paso', " + \
            "d.description AS 'respuesta', COUNT(c.id_choices) AS 'votos' " + \
            "FROM choices c JOIN decisions d ON c.fk_choices_decisions = d.id_decisions " + \
            "JOIN steps s ON c.fk_choices_steps = s.id_steps " + \
            "JOIN adventures a ON s.fk_steps_adventures = a.id_adventures " + \
            "GROUP BY a.name, s.id_steps, d.description ORDER BY a.name ASC, votos DESC;"
    connection = connect_to_database()
    res = execute_query(connection, query)
    connection.close()
    return res

def showReport1():
    datos_reporte = getReport1() 
    cabecera = getHeadeForTableFromTuples(
        ("Aventura", "Paso", "Respuesta", "Votos"), 
        (15, 40, 30, 10), 
        "MOST USED ANSWERS"
    )
    print(cabecera)
    
    for fila in datos_reporte:
        # RECORTAMOS los textos para que no superen el ancho de la columna
        # Usamos el rebanado de strings [0:35] para dejar espacio
        txt_paso = str(fila["paso"])
        if len(txt_paso) > 37:
            txt_paso = txt_paso[0:34] + "..."
            
        txt_resp = str(fila["respuesta"])
        if len(txt_resp) > 27:
            txt_resp = txt_resp[0:24] + "..."

        # Ahora enviamos los textos ya recortados
        celdas = (str(fila["aventura"]), txt_paso, txt_resp, str(fila["votos"]))
        anchos = (15, 40, 30, 10)
        
        print(getFormatedBodyColumns(celdas, anchos, 2))


def getReport2():
    """Informe 2: Tots els jugadors ordenats per partides jugades"""
    query = "SELECT u.username, COUNT(g.id_game) AS 'total', u.date_reg " + \
            "FROM users u JOIN game g ON u.id_users = g.fk_game_users " + \
            "GROUP BY u.id_users ORDER BY total DESC, u.date_reg ASC;"
    connection = connect_to_database()
    res = execute_query(connection, query)
    connection.close()
    return res

def showReport2():
    datos_lista = getReport2() 
    
    cabecera = getHeadeForTableFromTuples(
        ("Nom de l'Usuari", "Total Partides", "Data de Registre"), 
        (40, 30, 35), 
        "RANKING DE JUGADORS"
    )
    print(cabecera)
    
    if not datos_lista:
        print("Encara no hi ha dades de joc.".center(105))
    else:
        for jugador_dict in datos_lista:
            # Formateig manual de data per slicing
            f_raw = str(jugador_dict["date_reg"])
            fecha_texto = f_raw[8:10] + "/" + f_raw[5:7] + "/" + f_raw[0:4]
            
            # Preparem les dades per a les columnes
            celdas = (str(jugador_dict["username"]), str(jugador_dict["total"]), fecha_texto)
            anchos = (40, 30, 35)
            
            # Fem servir la teva funció per mantenir el teu estil visual
            print(getFormatedBodyColumns(celdas, anchos, 2))



def getReport3(username):
    """Informe 3: Aventuras jugadas por el usuario X"""
    query = "SELECT a.id_adventures, a.name, MAX(g.game_date) AS 'fecha' " + \
            "FROM game g JOIN users u ON g.fk_game_users = u.id_users " + \
            "JOIN adventures a ON g.fk_game_adventures = a.id_adventures " + \
            "WHERE u.username = %s GROUP BY a.id_adventures, a.name ORDER BY fecha DESC;"
    connection = connect_to_database()
    res = execute_query(connection, query, (username,))
    connection.close()
    return res
 
def showReport3(username_string):
    """Muestra las aventuras jugadas por el usuario X"""
    # getReport3 espera un string (el nombre de usuario)
    listado_aventuras = getReport3(username_string) 
    
    print(getHeader("MY ADVENTURE LOG"))
    
    if not listado_aventuras:
        # Aquí puedes usar el string del nombre sin problemas
        print(("Todavia no has empezado ninguna historia: " + username_string).center(105))
    else:
        for registro in listado_aventuras:
            m = registro["fecha"]
            f_texto = str(m.day) + "/" + str(m.month) + "/" + str(m.year) + " " + \
                      str(m.hour) + ":" + str(m.minute)
            
            id_str = str(registro["id_adventures"])
            nom_str = str(registro["name"])
            
            linea_final = id_str.ljust(10) + nom_str.ljust(30) + f_texto.ljust(30)
            print(linea_final.center(105))




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

def wrap_text(text, width):
    """
    Divide texto en líneas sin cortar palabras.
    """
    if not text:
        return []

    lines = []
    for raw_line in text.split("\n"):
        words = raw_line.split(" ")
        current = ""

        for word in words:
            if len(current) + len(word) + 1 > width:
                lines.append(current.rstrip())
                current = word + " "
            else:
                current += word + " "

        if current:
            lines.append(current.rstrip())

    return lines

# =========================================================
# ===================== CAJA REPLAY =======================
# =========================================================

def printReplayBox(step_text, decision_text, result_text=None, width=88):

    def print_block(title, text):
        print("| " + title.center(width) + " |")
        print("|" + " " * (width + 2) + "|")

        for line in wrap_text(text, width):
            print("| " + line.ljust(width) + " |")

    border = "*" * (width + 4)
    print(border)

    print_block("ESCENA", step_text)
    print("|" + " " * (width + 2) + "|")
    print_block("DECISIÓN", decision_text)

    if result_text:
        print("|" + " " * (width + 2) + "|")
        print_block("RESULTADO", result_text)

    print("|" + " " * (width + 2) + "|")
    print(border)

def formatTextHistorias(text, max_len, split_char=" "):
    """
    Formatea un texto largo en líneas de longitud máxima max_len.
    Usa split_char (por ejemplo ;) como separador lógico.
    NO usa join().
    """

    if not text:
        return ""

    resultado = ""

    # Separación lógica (escenas, párrafos, etc.)
    bloques = text.split(split_char)

    for bloque in bloques:
        palabras = bloque.strip().split(" ")
        linea = ""

        for palabra in palabras:
            if len(linea) + len(palabra) + 1 > max_len:
                resultado += linea.rstrip() + "\n"
                linea = palabra + " "
            else:
                linea += palabra + " "

        if linea:
            resultado += linea.rstrip() + "\n"

        # Línea en blanco entre bloques
        resultado += "\n"

    return resultado.rstrip()


def getHeader(text):
    resultado = "*"*105 + "\n" + text.center(105, "=") + "\n" + "*"*105

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
        print("Password length has to be minimum 8 or maximum 12")
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

    # =========================
    # 1. OBTENER PARTIDAS
    # =========================
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

    # Matriz: [num, id_game, fecha, nombre]
    matrix = []
    counter = 1
    for g in games:
        matrix.append([counter, g["id_game"], g["game_date"], g["name"]])
        counter += 1

    bubble_sort_by_date(matrix)

    print("\n=== PARTIDAS DISPONIBLES ===")
    for row in matrix:
        print(str(row[0]) + ") " + str(row[3]) + " (" + str(row[2]) + ")")

    try:
        choice = int(input("\nElige una partida: "))
    except ValueError:
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

    # =========================
    # 2. REPLAY DE DECISIONES
    # =========================
    query_replay = """
        SELECT 
            s.id_steps,
            s.description AS step_text,
            d.description AS decision_text,
            d.result_text,
            d.fk_decisions_next_step
        FROM choices c
        JOIN steps s ON c.fk_choices_steps = s.id_steps
        JOIN decisions d ON c.fk_choices_decisions = d.id_decisions
        WHERE c.fk_choices_game = %s
        ORDER BY c.id_choices ASC;
    """

    replay_data = execute_query(connection, query_replay, (selected_game_id,))

    print("\n=== AUTOREPLAY DE LA PARTIDA ===\n")

    last_next_step = None

    if replay_data:
        for r in replay_data:

            # Guardamos el siguiente paso (para mostrar el final después)
            last_next_step = r["fk_decisions_next_step"]

            # Formateamos los textos
            step_text = formatText(r["step_text"], 105, ";")
            decision_text = formatText(r["decision_text"], 105, ";")

            if r["result_text"]:
                result_text = formatText(r["result_text"], 105, ";")
            else:
                result_text = None

            # Mostramos la escena completa
            printReplayBox(
                step_text,
                decision_text,
                result_text
            )

            input("\nEnter to continue")
            print("\n")

    # =========================
    # 3. MOSTRAR STEP FINAL
    # =========================
    if last_next_step:
        query_final = """
            SELECT description
            FROM steps
            WHERE id_steps = %s;
        """
        final_step = execute_query(connection, query_final, (last_next_step,))

        if final_step:
            final_text = formatText(final_step[0]["description"], 110, ";")

            printReplayBox(
                final_text,
                "FIN",
                None
            )

            input("\nEnter to finish")

    close_connection(connection)


def clear_screen():
    """
    Limpia la pantalla de la terminal.
    Funciona en Windows, Linux y macOS.
    """
    # Windows usa 'cls', Linux/macOS usan 'clear'
    os.system('cls' if os.name == 'nt' else 'clear')