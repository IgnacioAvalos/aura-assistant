usuario = {
    "nombre": "",
    "objetivo_principal": "",
    "profesion": ""
}


def guardar_dato(campo, valor):
    usuario[campo] = valor


def obtener_dato(campo):
    return usuario.get(campo)