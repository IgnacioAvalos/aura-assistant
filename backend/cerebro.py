def analizar_mensaje(mensaje):

    texto = mensaje.lower().strip()


    if "como me llamo" in texto or "cómo me llamo" in texto:

        return {
            "accion": "consultar_nombre"
        }


    if "me llamo" in texto:

        nombre = mensaje.replace("me llamo", "").strip()

        return {
            "accion": "guardar_nombre",
            "dato": nombre
        }


    if "mi objetivo es" in texto:

        objetivo = texto.replace("mi objetivo es", "").strip()

        return {
            "accion": "guardar_objetivo",
            "dato": objetivo
        }


    if "cual es mi objetivo" in texto or "cuál es mi objetivo" in texto:

        return {
            "accion": "consultar_objetivo"
        }


    return {
        "accion": "desconocido"
    }