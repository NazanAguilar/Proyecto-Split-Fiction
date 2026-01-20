from Funcions_programa.BBDD import * 
from Funcions_programa.Variables import *

#FUNCIONES BBDD
def get_characters():
    query = "SELECT * FROM characters;"
    connection = connect_to_database()
    if connection:
        results = execute_query(connection, query)
        close_connection(connection)
        if results:
            char_dict = {}
            for row in results:
                char_dict[row['id_characters']] = {
                    "name": row['name'],
                    "description": row['description']
                }
            return char_dict
    return {}

def get_users():
    query = "SELECT * FROM users;"  
    connection = connect_to_database()

    if connection:
        results = execute_query(connection, query)
        close_connection(connection)
        if results:
            users_dict = {}

            for row in results:
                users_dict[row['id_users']] = {
                    "username": row['username'],
                    "password": row['password'],
                    "date_reg": row['date_reg'],
                    "user_reg": row['user_reg'],
                    "date_mod": row['date_mod'],
                    "user_mod": row['user_mod']
                } 

            return users_dict
        return {}
    return {}

def get_adventures():
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

def add_user(name,pwd):
    pwd = cifrar(pwd)

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

def getFormatedAdventures():
    cabezera = getHeadeForTableFromTuples(("Id", "Adventure", "Description"), (15, 40, 50), title="Adventures")
    datos = ""
    
    adventures = get_adventures()

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