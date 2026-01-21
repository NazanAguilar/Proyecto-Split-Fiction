import datetime

salir = False
login = False
user_login = None
create_user = False
menu0 = False
comp_user = False
comp_pass = True
in_users = False

textMenu0_login="\n1)Login\n2)Create user\n3)Replay Adventures\n4)Reports\n5)Exit"
textMenu0_logout="\n1)Logout\n2)Create user\n3)Replay Adventures\n4)Reports\n5)Exit"

#variables para pruebas

text1 = "Seguro que más de uno recuerda aquellos libros en los que podías elegir cómo seguir con la aventura que estabas viviendo simplemente"

adventures = {
    1: {
        "Name": "nom de l'aventura",
        "Description": "descripció de l'aventura asrgarsar argrgagrarg argargaergaergaer adrgsergearherhahehe",
        "characters": [1, 2, 3]  # llista amb els IDs dels personatges
    },
    2: {
        "Name": "nom de l'aventura 2",
        "Description": "descripció de la segona aventura",
        "characters": [4, 5]
    }
}

inputOptText="\nElige tu opción:"
lista_menu0 = [1,2,3,4]
dic_range = {"1":1,"2":2,"3":3,"4":4}
excepciones = ["w","e",-1]