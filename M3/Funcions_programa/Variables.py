import datetime

salir = False
portada_flg = True  # == Menu00
conectado_flg = False  # == Menu 01 (Conexion)
login = False
user_login = None
create_user = False
menu0 = False
comp_user = False
comp_pass = True
in_users = False
user = ""
password = ""

textMenu0_login="\n1)Login\n2)Create user\n3)Replay Adventures\n4)Reports\n5)Exit"
textMenu0_logout="\n1)Logout\n2)Create user\n3)Replay Adventures\n4)Reports\n5)Exit"
inputOptText="\nElige tu opción:"
lista_menu0 = [1,2,3,4]
dic_range = {"1":1,"2":2,"3":3,"4":4}
excepciones = ["w","e",-1]



portada = (
    "****************************************************************************************",
    "|                                                                                      |",
    "|                                                                                      |",
    "|    _________      .__  .__  __    ___________.__        __  .__                      |",
    "|   /   _____/_____ |  | |__|/  |_  \_   _____/|__| _____/  |_|__| ____   ____         |",
    "|   \_____  \/____ \|  | |  \   __\  |    __)  |  |/ ___\   __\  |/  _ \ /    \        |",
    "|   /        \  |_> >  |_|  ||  |    |     \   |  \  \___|  | |  (  <_> )   |  \       |",
    "|  /_______  /   __/|____/__||__|    \___  /   |__|\___  >__| |__|\____/|___|  /       |",
    "|          \/|__|                        \/            \/                    \/        |",
    "|                                                                                      |",
    "|                        1) New User     2) Conect     3) Exit                         |",
    "****************************************************************************************")



pantalla_principal = (
    "****************************************************************************************",
    "|                                                                                      |",
    "|      1) Play History                        (\\                                       |",
    "|                                              \\'\\                                     |",
    "|      2) Replay Mode                          \\'\\     __________                      |",
    "|                                               / '|   ()_________)                    |",
    "|      3) Reports                              \\ '/    \\ ~~~~~~~~ \\                    |",
    "|                                               \\       \\ ~~~~~~   \\                   |",
    "|      4) Log Out                               ==).      \\__________\\                 |",
    "|                                               (__)       ()__________)               |",
    "|                                                                                      |",
    "****************************************************************************************")
