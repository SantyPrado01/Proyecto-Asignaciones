import sqlite3

base_datos = sqlite3.connect('hermanos.bd')
cursor = base_datos.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS fecha(
        fecha_id INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha DATE          
    )   
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS fechaxhermano(
        hermano_id INT,
        fecha_id INT,
        PRIMARY KEY (hermano_id, fecha_id),
        FOREIGN KEY (hermano_id) REFERENCES hermanos(hermano_id),
        FOREIGN KEY (fecha_id) REFERENCES fecha(fecha_id)
    )   
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS asignacion(
        asignacion_id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre VARCHAR(255) NOT NULL          
    )   
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS asignacionxhermano(
        hermano_id INT,
        asignacion_id INT,
        PRIMARY KEY (hermano_id, asignacion_id),
        FOREIGN KEY (hermano_id) REFERENCES hermanos(hermano_id),
        FOREIGN KEY (asignacion_id) REFERENCES asignacion(asignacion_id)
    )   
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS ayudante(
        ayudante_id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre VARCHAR(255) NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS ayudantexhermano(
        ayudante_id INT,
        hermano_id INT,
        PRIMARY KEY (ayudante_id, hermano_id),
        FOREIGN KEY(ayudante_id) REFERENCES ayudante(ayudante_id),
        FOREIGN KEY (hermano_id) REFERENCES hermanos(hermano_id)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS salas(
        sala_id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre VARCHAR(255) NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS salaxhermano(
        sala_id INT,
        hermano_id INT,
        PRIMARY KEY (sala_id, hermano_id),
        FOREIGN KEY (sala_id) REFERENCES salas(sala_id),
        FOREIGN KEY (hermano_id) REFERENCES hermanos(hermano_id)              
    )
''')


cursor.execute('''
    CREATE TABLE IF NOT EXISTS hermanos(
        hermano_id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre VARCHAR(255) NOT NULL,
        ayudante_id INT,
        asignacion_id INT,
        fecha_id INT,
        sala_id INT,
        FOREIGN KEY (fecha_id) REFERENCES fecha(fecha_id),
        FOREIGN KEY (asignacion_id) REFERENCES asignacion(asignacion_id),
        FOREIGN KEY (ayudante_id) REFERENCES ayudante(ayudante_id),
        FOREIGN KEY (sala_id) REFERENCES sala(sala_id)             
    )
''')

