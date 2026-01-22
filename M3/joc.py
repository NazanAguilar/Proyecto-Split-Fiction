from Funcions_programa.BBDD import *
from Funcions_programa.Variables import *
from Funcions_programa.Funcions import *

# =====================================
# PROGRAMA PRINCIPAL
# =====================================

while not salir:

    # =========================
    # PORTADA
    # =========================
    while portada_flg:

        clear_screen()
        for linea in portada:
            print(linea)

        opc = input(">Option --> ")

        if not opc.isdigit():
            print("No numeric option")
            input("Enter to continue")
            continue

        opc = int(opc)

        # -------- NEW USER --------
        if opc == 1:
            clear_screen()
            print(getHeader("NEW USER"))
            print("Enter 0 at any time to cancel\n")

            # USERNAME
            while True:
                user = input("Username: ")
                if user == "0":
                    break
                if checkUser(user) and not userExists(user):
                    break

            if user == "0":
                continue

            # PASSWORD
            while True:
                password = input("Password: ")
                if password == "0":
                    break
                if checkPassword(password):
                    break

            if password == "0":
                continue

            created = insertUser(len(getUserIds()[1]), user, password)

            if created:
                print("\nUser created successfully!")
            else:
                print("\nUsername already exists. User not created.")

            input("Press Enter to continue")


        # -------- CONNECT / LOGIN --------
        elif opc == 2:
            clear_screen()
            print(getHeader("LOGIN"))
            print("Enter 0 at any time to cancel\n")

            user = input("Username: ")
            if user == "0":
                continue

            password = input("Password: ")
            if password == "0":
                continue

            user_data = login_user(user, password)

            if user_data:
                print("\nLogin successful!")
                user_login = user_data
                conectado_flg = True
                portada_flg = False
                input("Press Enter to continue")
            else:
                print("\nInvalid username or password")
                input("Press Enter to continue")

        # -------- EXIT --------
        elif opc == 3:
            salir = True

        else:
            print("Option out of range")
            input("Enter to continue")

    # =========================
    # PANTALLA PRINCIPAL
    # =========================
    while conectado_flg:

        clear_screen()
        for linea in pantalla_principal:
            print(linea)

        opc = input(">Option --> ")

        if not opc.isdigit():
            print("No numeric option")
            input("Enter to continue")
            continue

        opc = int(opc)

        # -------- PLAY HISTORY --------
        if opc == 1:
            print("\nAquí iría el modo juego")
            input("Enter to continue")

        # -------- REPLAY MODE --------
        elif opc == 2:
            autoreplay_games(user_login["id_users"])

        # -------- REPORTS --------
        elif opc == 3:
            print("\nAquí irán los reportes")
            input("Enter to continue")



        # -------- LOG OUT --------
        elif opc == 4:
            conectado_flg = False
            portada_flg = True
            user_login = None

        else:
            print("Option out of range")
            input("Enter to continue")


"""


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
"""