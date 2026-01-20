from Funcions_programa.BBDD import *
from Funcions_programa.Variables import *
from Funcions_programa.Funcions import *

while not salir:
    while menu0:
        if not login:
            opc = int(getOpt(textMenu0_login,inputOptText,rangeList=lista_menu0,exceptions=excepciones))
        else:
            opc = int(getOpt(textMenu0_logout,inputOptText,rangeList=lista_menu0,exceptions=excepciones))
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
            menu0 = False

    while create_user:
        print(getHeader("NEW USER"))
        comp_user = False

        while not comp_user:
            user = input("Username:\n")
            if checkUser(user):
                if not userExists(user):
                    comp_user = True


        
        comp_pass = False
        while not comp_pass:
            password = input("Password:\n")
            if checkPassword(password):
                add_user(user,password)
                comp_pass = True
                menu0 = True
                create_user = False