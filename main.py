import sqlite3

# Función para inicializar la base de datos
def initialize_db():
    conn = sqlite3.connect('rpg_game.db')
    cursor = conn.cursor()
    
    # Crear tabla de personajes
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS characters (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            level INTEGER NOT NULL,
            health INTEGER NOT NULL,
            attack INTEGER NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()

# Función para crear un nuevo personaje
def create_character(name, level, health, attack):
    conn = sqlite3.connect('rpg_game.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO characters (name, level, health, attack)
        VALUES (?, ?, ?, ?)
    ''', (name, level, health, attack))
    
    conn.commit()
    conn.close()

# Función para leer y mostrar todos los personajes
def read_characters():
    conn = sqlite3.connect('rpg_game.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM characters')
    rows = cursor.fetchall()
    
    for row in rows:
        print(f'ID: {row[0]}, Name: {row[1]}, Level: {row[2]}, Health: {row[3]}, Attack: {row[4]}')
    
    conn.close()

# Función para actualizar datos de un personaje
def update_character(id, name=None, level=None, health=None, attack=None):
    conn = sqlite3.connect('rpg_game.db')
    cursor = conn.cursor()
    
    if name:
        cursor.execute('UPDATE characters SET name = ? WHERE id = ?', (name, id))
    if level is not None:
        cursor.execute('UPDATE characters SET level = ? WHERE id = ?', (level, id))
    if health is not None:
        cursor.execute('UPDATE characters SET health = ? WHERE id = ?', (health, id))
    if attack is not None:
        cursor.execute('UPDATE characters SET attack = ? WHERE id = ?', (attack, id))
    
    conn.commit()
    conn.close()

# Función para eliminar un personaje
def delete_character(id):
    conn = sqlite3.connect('rpg_game.db')
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM characters WHERE id = ?', (id,))
    
    conn.commit()
    conn.close()

# Documentación del prototipo
def print_documentation():
    print("""
    # Documentación del Prototipo RPG
    
    ## Estructura de la Base de Datos
    La base de datos `rpg_game.db` contiene una tabla `characters` con los siguientes campos:
    - `id` (INTEGER, PRIMARY KEY): Identificador único del personaje.
    - `name` (TEXT): Nombre del personaje.
    - `level` (INTEGER): Nivel del personaje.
    - `health` (INTEGER): Salud del personaje.
    - `attack` (INTEGER): Ataque del personaje.
    
    ## Requisitos del Sistema
    - Python 3.x
    - SQLite3 (integrado en Python)
    
    ## Arquitectura de la Aplicación
    La aplicación está basada en una base de datos SQLite para almacenar los datos de los personajes. La aplicación permite crear, leer, actualizar y eliminar registros a través de funciones Python que interactúan con la base de datos.
    
    ## Flujo de Trabajo de la Aplicación
    1. Inicializa la base de datos con `initialize_db()`.
    2. Usa `create_character()` para agregar nuevos personajes.
    3. Usa `read_characters()` para ver los personajes existentes.
    4. Usa `update_character()` para modificar detalles de un personaje.
    5. Usa `delete_character()` para eliminar un personaje.
    
    ## Ejemplos de Código
    ```python
    # Crear un nuevo personaje
    create_character('Gandalf', 20, 150, 30)
    
    # Leer todos los personajes
    read_characters()
    
    # Actualizar un personaje
    update_character(1, attack=35)
    
    # Eliminar un personaje
    delete_character(1)
    ```
    
    ## Casos de Prueba y Resultados
    1. **Caso de prueba: Crear un personaje**
       - **Entrada:** `create_character('Gandalf', 20, 150, 30)`
       - **Resultado esperado:** El personaje se crea en la base de datos.
    
    2. **Caso de prueba: Leer personajes**
       - **Entrada:** `read_characters()`
       - **Resultado esperado:** Muestra todos los personajes en la base de datos.
    
    3. **Caso de prueba: Actualizar un personaje**
       - **Entrada:** `update_character(1, attack=35)`
       - **Resultado esperado:** El ataque del personaje con ID 1 se actualiza a 35.
    
    4. **Caso de prueba: Eliminar un personaje**
       - **Entrada:** `delete_character(1)`
       - **Resultado esperado:** El personaje con ID 1 se elimina de la base de datos.
    
    ## Guía de Instalación y Configuración
    1. Instalar Python 3.x.
    2. Descargar o clonar el repositorio del proyecto.
    3. Ejecutar `python script.py` para inicializar la base de datos.
    4. Llamar a las funciones disponibles para gestionar los personajes.
    """)

# Inicializar la base de datos
initialize_db()

# Mostrar documentación
print_documentation()

# Ejemplo de uso (descomentar para probar)
# create_character('Aragorn', 10, 100, 20)
# read_characters()
# update_character(1, level=12, health=120)
# delete_character(1)
