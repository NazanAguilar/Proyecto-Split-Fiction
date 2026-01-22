# Projecte-Split-Fiction
AWS1 (Choose Your Story) NazanAguilar-MarcLosada-StyvenCatagua


# Informació de contacte

-->Marc Losada:

-Correu: mlosadasoler2.eb@iesesteveterradas.cat



-->Nazan Aguilar:

-Correu: naguilarperez.cf@iesesteveterradas.cat



-->Styven Catagua:

-Correu: scataguafortiz.25cf@iesesteveterradas.cat



Motor d'aventures de text on les decisions de l'usuari alteren el curs de la història.

## Estructura del Projecte

*   **/M2**: Conté els scripts SQL de la base de dades.
    *   `Split Fiction Create_DB (Nazan Marc Styven).sql`: Creació de taules.
    *   `Split Fiction Alter_DB (Nazan Marc Styven).sql`: Restriccions (PK, FK, Unique).
    *   `Split Fiction Insert_DB (Nazan Marc Styven).sql`: Dades inicials (Aventures, Personatges, Matrix).

*   **/M3**: Conté els arxius del programa.
    *   **/Funcions_programa**: Conté totes les funcions del programa.
        *   **/__pycache__**: serveix per emmagatzemar Bytecode els archius .pyc que són versions "precompiladas" del   teu codi font (.py) transformades a un llenguatge intermedi anomenat bytecode. Accelerar l'Inici i Gestio Automtic.
        *   `__init__.py`: Serveix per a identificar els arxius i inicialitzar-los
    *   `joc.py`: Aquí està el programa del joc.
    *   `proves.txt`: Aqui estaran totes les proves que hem anat fent al llarg del projecte omitint el tipic:
            print(no se que) 
            input()
    
    **/M4**: Conté la pàgina web pujada al proxmox.
    *   `index.html`: Pàgina principal del proyecte.
    *   **`estils.css`**: Estil amb capzalera i peu de pàgina, funcional en totes les pàgines web 
    *   `instruccions.html`: Instruccions de com es juga el videojoc.
    *   `historia.html`: Història de que consiteix el videojoc + serie d'imatges en format carrousel on es mostra les imatges de la nostra versió del Split Fiction .
    *   `sobre_nosaltres.html`: Nom del equip desenvolupador + un video de YouTube.
    *   `contacte.html`: Formulari (No funcional) + les nostres dades de contacte.
    *   **/img**: Imatges introduides a la pàgina web.