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
    *   `Informes.sql`: Aquí estan els scripts dels informes

*   **/M3**: Conté els arxius del programa.
    *   **/Funcions_programa**: Conté totes les funcions del programa.
        *   **/__pycache__**: Serveix per emmagatzemar Bytecode els arxius .pyc que són versions "precompilades" del   teu codi font (.py) transformades a un llenguatge intermedi anomenat bytecode. Accelerar l'Inici quan s'executa el codi mira si l'arxiu si no ha canviat llavors càrrega el bytecode directament, cosa que estalvia temps de càrrega i Python gestiona automàticament amb una marca de temps i regenera l'arxiu __pycache__.
        *   `__init__.py`: Permet que es pugui fer `import carpeta.arxiu` i l'arxiu `__init__.py` s'executa automàticament.
        *   `BBDD.py`: Aquí estan les funcions que siguin sobre la base de dades com per exemple: execute_query, connect_database, etc.
        *   `Funcions.py`: Aquí estarien totes les funcions de la base de dades.
        *   `Variables.py`: Aquí estarien totes les variables que s'utilitzen per a tot.
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

## 🛠️ Requisits del Sistema

Per a executar el projecte desde localhost correctament, necessitaràs:
*   **Python 3.10+** instalado. [Python Downloads](https://www.python.org)
*   **MySQL Server** (versió 8.0 recomanada).
*   Llibreria **PyMySQL**:
    ```bash
    pip install PyMySQL
    ```
## 🚀 Instal·lació i Ús (Local host)

### 1. Preparar la Base de Dades (M2)
Executa els scripts de la carpeta `/M2` en l'ordre següent en el teu gestor de base de dades (Workbench, phpMyAdmin, etc.):
1. `Split Fiction Create_DB (Nazan Marc Styven).sql`
2. `Split Fiction Alter_DB (Nazan Marc Styven).sql`
3. `Split Fiction Insert_DB (Nazan Marc Styven).sql`

### 2. Executar el Joc (M3)
Un cop configurada la BBDD, accedeix a la carpeta `/M3` i executa el fitxer principal:
```bash
python joc.py
```

## 🚀 Instal·lació i Ús (Tunel SSH)

## 🔒 Seguretat i Connexió Remota (SSH Tunneling)

Atès que la base de dades es troba al servidor **Proxmox** de l'institut, la connexió es realitza mitjançant un **túnel SSH** per garantir la seguretat de les dades.

### Com connectar-se:
1. **Establir el Túnel**: Abans d'executar el joc, cal obrir el túnel des de la terminal o mitjançant un client (com PuTTY o la terminal nativa):
   ```bash
   ssh -p 20127 -L 3307:127.0.0.1:3306 aventura7@ieticloudpro.ieti.cat

### 2. Executar el Joc (M3)
Un cop configurada la BBDD, accedeix a la carpeta `/M3` i executa el fitxer principal:
```bash
python joc.py
```
