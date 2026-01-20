from Funcions_programa.BBDD import *
from Funcions_programa.Variables import *
from Funcions_programa.Funcions import *

while not salir:
    while menu0:
        if login == False:
            opc = int(getOpt(textMenu0_login,inputOptText,rangeList=lista,exceptions=excepciones))
            if opc == 1:
                print("iniciando sesion")
            elif opc == 2:
                create_user = True
                menu0 = False
            elif opc == 3:
                print("reproduciendo")
            elif opc == 4:
                print("reportando")
            else:
                salir = True
    while create_user:
        if comp_user == False:
            user = input("Username:\n")
            comp_user = checkUser(user)   
        else:
            if comp_pass == False:
                password = input("Password:\n")
                comp_pass = checkPassword(password)
            else:
                print