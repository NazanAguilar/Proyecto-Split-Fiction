# Projecte-Split-Fiction
**AWS1 (Choose Your Story)** - Nazan Aguilar, Marc Losada i Styven Catagua

Motor d'aventures de text on les decisions de l'usuari alteren el curs de la història.

## 📧 Informació de Contacte

*   **Marc Losada:** [mlosadasoler2.eb@iesesteveterradas.cat](mailto:mlosadasoler2.eb@iesesteveterradas.cat)
*   **Nazan Aguilar:** [naguilarperez.cf@iesesteveterradas.cat](mailto:naguilarperez.cf@iesesteveterradas.cat)
*   **Styven Catagua:** [scataguafortiz.25cf@iesesteveterradas.cat](mailto:scataguafortiz.25cf@iesesteveterradas.cat)

---

## 📂 Estructura del Projecte

### **/M2: Base de Dades**
Conté els scripts SQL per a la gestió del sistema:
*   `Split Fiction Create_DB (Nazan Marc Styven).sql`: Creació de taules.
*   `Split Fiction Alter_DB (Nazan Marc Styven).sql`: Restriccions (PK, FK, Unique).
*   `Split Fiction Insert_DB (Nazan Marc Styven).sql`: Dades inicials (Aventures, Personatges, Matrix).
*   `Informes.sql`: Scripts dels informes i consultes de seguiment.

### **/M3: Programa (Python)**
*   **/Funcions_programa**:
    *   `BBDD.py`: Funcions de connexió i execució de consultes SQL.
    *   `Funcions.py`: Totes les funcions lògiques i de base de dades.
    *   `Variables.py`: Totes les variables globals utilitzades.
    *   `__pycache__`: Emmagatzema el bytecode (.pyc) per accelerar l'inici del programa evitant la recompilació si el codi no ha canviat.
    *   `__init__.py`: Permet la importació modular de la carpeta.
*   `joc.py`: Arxiu principal que conté el programa del joc.
*   `proves.txt`: Registre de les proves realitzades durant el desenvolupament.

### **/M4: Projecte Web**
Pàgina informativa allotjada al servidor **Proxmox**:
*   `index.html`: Pàgina principal del projecte.
*   `estils.css`: Disseny visual funcional per a totes les pàgines.
*   `instruccions.html`: Guia de com jugar al videojoc.
*   `historia.html`: Descripció de l'argument i carrousel d'imatges.
*   `sobre_nosaltres.html`: Informació de l'equip i vídeo de presentació.
*   `contacte.html`: Formulari de contacte i dades de l'equip.
*   **/img**: Recursos gràfics de la web.

---

## 🛠️ Requisits del Sistema

*   **Python 3.10+** [Pàgina oficial](https://www.python.org)
*   **MySQL Server 8.0**
*   Biblioteca **PyMySQL**:
    ```bash
    pip install PyMySQL
    ```

---

## ⚙️ Configuració de la Connexió

Per a connectar-se a la base de dades, cal editar el fitxer `BBDD.py` segons l'entorn de treball:

**Opció A: Localhost**
Cal descomentar el bloc de configuració local:
```python
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'admin',
    'database': 'split_fiction',
}
```
I comentar:
```python
db_config = {
    'host': '127.0.0.1',
    'user': 'equipo7',
    'password': 'P@ssw0rd',
    'database': 'equipo7_SplitFiction',
    'port': 3307
}
```

**Opció B: Tunel SSH**
Fer lo mateix que en la opcio A pero al reves.

## 🚀 Instal·lació i Ús (Localhost)

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

Projecte desenvolupat per l'Equip 7 - IETI Esteve Terradas.