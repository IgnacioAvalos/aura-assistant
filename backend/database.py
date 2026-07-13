import sqlite3


def conectar():

    conexion = sqlite3.connect("../database/aura.db")

    return conexion



def crear_tablas():

    conexion = conectar()

    cursor = conexion.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuario (

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        objetivo TEXT

    )
    """)


    conexion.commit()

    conexion.close()



crear_tablas()