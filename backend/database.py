import os
import sqlite3


def conectar():

    ruta_base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    ruta_db = os.path.join(
        ruta_base,
        "database",
        "aura.db"
    )

    return sqlite3.connect(ruta_db)


def guardar_usuario(nombre=None, objetivo=None):

    conexion = conectar()
    cursor = conexion.cursor()


    cursor.execute(
        """
        INSERT INTO usuario (nombre, objetivo)
        VALUES (?, ?)
        """,
        (nombre, objetivo)
    )


    conexion.commit()
    conexion.close()



def obtener_usuario():

    conexion = conectar()
    cursor = conexion.cursor()


    cursor.execute(
        """
        SELECT nombre, objetivo
        FROM usuario
        ORDER BY id DESC
        LIMIT 1
        """
    )


    usuario = cursor.fetchone()

    conexion.close()

    return usuario