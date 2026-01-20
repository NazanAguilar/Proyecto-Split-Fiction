import datetime

salir = False
login = False
create_user = False
menu0 = True
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

diccionari = {4: {'idUser': 2, 'Username': 'Jordi', 'idAdventure': 1, 'Name': 'Este muerto esta muy vivo',
'date': datetime.datetime(2021, 11, 28, 18, 17, 20), 'idCharacter': 1, 'CharacterName':
'Beowulf'}, 5: {'idUser': 2, 'Username': 'Jordi', 'idAdventure': 1, 'Name': 'Este muerto esta muy vivo', 'date': datetime.datetime(2021, 11, 26, 13, 28, 36), 'idCharacter': 1,
'CharacterName': 'Beowulf'}}
tuple_of_keys = ("Username","Name","CharacterName","date")
weigth_of_columns = (20, 30, 20, 20)

inputOptText="\nElige tu opción:"
lista = [1,2,3,4]
dic_range = {"1":1,"2":2,"3":3,"4":4}
excepciones = ["w","e",-1]