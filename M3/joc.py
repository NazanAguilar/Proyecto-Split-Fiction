from Funcions_programa.BBDD import *
from Funcions_programa.Variables import *
from Funcions_programa.Funcions import *


# print(autoreplay_games(1))

while not salir:

    while portada_flg:

        for linea in portada:
            print(linea)

        opc = input(">Option --> ")

        if not opc.isdigit():
            print("No numeric option")
            input("enter to continue")
            clear_screen()

        elif not (int(opc) in range(1,4)):
            print("Option out of range")
            input("enter to continue")
            clear_screen()

        else:
            opc = int(opc)

            if opc == 1:
                create_user = True

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
                            insertUser(len(getUserIds()[1]), user, password)
                            comp_pass = True
                            menu0 = True
                            create_user = False

            elif opc == 2:
                input("Aqui te conectas")
                # Luego asles de portada_flg
                conectado_flg = True
                portada_flg = False

            else:
                salir = True

    while conectado_flg:

        for linea in pantalla_principal:
            print(linea)

        opc = input(">Option --> ")

        if not opc.isdigit():
            print("No numeric option")
            input("enter to continue")
            clear_screen()

        elif not (int(opc) in range(1, 5)):
            print("Option out of range")
            input("enter to continue")
            clear_screen()

        else:
            opc = int(opc)

            if opc == 1:
                input("Aqui Juegas")

            elif opc == 2:
                input("Aqui tienes el reply mode")

            elif opc == 3:
                input("Aqui tienes los reportes / informes")

            else:
                conectado_flg = False
                portada_flg = True





    while not login and user_login == None:
        print("--- LOGIN ---")
        user_input = input("Usuario: ")
        pass_input = input("Contraseña: ")
        
        # Llamamos a la función de la BBDD que creamos antes
        # Suponiendo que la llamaste login_user o similar
        resultado = login_user(user_input, pass_input) 
        
        if resultado:
            menu0 = True
            user_login = resultado # Guardamos los datos del usuario (id, nombre...)
            login = True
            print("Bienvenido de nuevo")
        else:
            print("Usuario o contraseña incorrectos")


    while menu0:
        opc = int(getOpt(textMenu0_logout,inputOptText,rangeList=lista_menu0,exceptions=excepciones))
        if opc == 1:
            login = False
            user_login = None
            menu0 = False
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
                insertUser(len(getUserIds()[1]),user,password)
                comp_pass = True
                menu0 = True
                create_user = False