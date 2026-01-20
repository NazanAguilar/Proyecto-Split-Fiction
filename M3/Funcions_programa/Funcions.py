from Funcions_programa.BBDD import * 
from Funcions_programa.Variables import *

#FUNCIONES BBDD
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

    check_query = "SELECT 1 FROM users WHERE username = %s"
    connection = connect_to_database()
    exists = execute_query(connection, check_query, (name,))
    
    if exists:
        print("El usuario ya existe, no se intentará el registro.")
        close_connection(connection)
        return False

    query = "INSERT INTO users (username, password, date_reg, user_reg) VALUES (%s, %s, NOW(), (SELECT COUNT(*) + 1 FROM users AS t));"
    connection = connect_to_database()
    results = execute_query(connection, query, (name, pwd))
    if connection:
        connection.commit() 
        close_connection(connection)

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

def getFormatedAdventures(adventures):
    cabezera = getHeadeForTableFromTuples(("Id Adventure","Adventure","Description"),(15,40,50),title="Adventures")
    datos = ""

    for i in range(len(adventures)):
        id = str(i+1)
        nombre = adventures[i+1]["Name"]
        descripcion = adventures[i+1]["Description"]
        columnas = (id,nombre,descripcion)
        espaciado = (15,40,50)
        datos += getFormatedBodyColumns(columnas,espaciado)
    
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

    if len(password) >= 8 and len(password) <= 12:
        if " " in password:
            print("Password cannot contain spaces")
        
        else:
            for i in range(len(password)):
                if password[i] in accentos:
                    print("Accents are not allowed")
                    return False
                if password[i] in esp:
                    especial_corr = True
                if password[i] in mayus:
                    may_corr = True
                if password[i] in num:
                    num_corr = True
                if password[i] in minus:
                    min_corr = True
            if especial_corr == False:
                print("Password has to contain some especial character")
            else:
                if num_corr == False:
                    print("Password has to contain some digit")
                else:
                    if may_corr == False or min_corr == False:
                        print("Password have to include some uppercase and some lowercase")
                    else:
                        return True
    else:
        print("Length of password is not correct")
    return False

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
    usuarios = get_users()
    list_users = list(str(usuarios.get("username")))

    for id in usuarios:
        list_users.append(usuarios[id]["username"])

    if user in list_users:
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

#-----------------PRUEBAS----------------------

#print(formatText(text1,20,split=" "))

#print(getHeader("Adventures"))

#print(getFormatedBodyColumns((text1,text1,text1),(20,30,50),margin=2))

#print(getFormatedAdventures(adventures))

#print(getHeadeForTableFromTuples(("column1","column2","column3"),(10,20,30)))

#print(getTableFromDict(tuple_of_keys, weigth_of_columns, diccionari))

"""opc = getOpt(textOpts,inputOptText,rangeList=lista,exceptions=excepciones)
print(opc)
print(type(opc))
opc = getOpt(textOpts,inputOptText,dictionary=dic_range,exceptions=excepciones)
print(opc)
print(type(opc))"""

"""print(getFormatedTable((('ID AVENTURA - NOMBRE', 'ID PASO - DESCRIPCION', 'ID RESPUESTA - DESCRIPCION', 'NUMERO VECES SELECCIONADA'), 
                        ('10 - Todos los h├®roes necesitan su princesa', '101 - Son las 6 de la ma├▒ana, %personaje% est├í profundamente dormido. Le suena la alarma!', '101 - Apaga la alarma porque quiere dormir, han sido d├¡as muy duros y %personaje% necesita un descanso.', 7)
                        , ('10 - Todos los h├®roes necesitan su princesa', '103 - Nuestro h├®roe %personaje% se viste r├ípidamente y va an direcci├│n al ciber, hay mucho jaleo en la calle, tambi├®n mucha polic├¡a.', '108 - Entra en el ciber a revisar si la princesa Wyoming sigue dentro.', 5))
                       ,title="Most used answer"))"""

# --- EJEMPLOS DE PRUEBA PARA LA CONTRASEÑA---

"""print("--- Test 1: Longitud corta ---")
print(checkPassword("Ab1!")) 

print("\n--- Test 2: Longitud larga ---")
print(checkPassword("PasswordMuyLarga123!") )

print("\n--- Test 3: Contiene espacios ---")
print(checkPassword("Ab 123456!") )

print("\n--- Test 4: Sin caracteres especiales ---")
print(checkPassword("Password123") )

print("\n--- Test 5: Sin números (dígitos) ---")
print(checkPassword("Password!!") )

print("\n--- Test 6: Sin mayúsculas o sin minúsculas ---")
print(checkPassword("password123!") )
print(checkPassword("PASSWORD123!") )

print("\n--- Test 7: TODO CORRECTO (No imprimirá nada) ---")
print(checkPassword("Admin123!"))"""

#print(userExists("Jordi"))