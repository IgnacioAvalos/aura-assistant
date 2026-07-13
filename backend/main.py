from memoria import guardar_dato, obtener_dato


print("🤖 AURA iniciada")
print("Escribe 'salir' para terminar\n")


while True:

    mensaje = input("Ignacio: ")

    if mensaje.lower().strip() == "salir":
        print("AURA: Hasta pronto Ignacio. Seguimos construyendo.")
        break


    mensaje_minuscula = mensaje.lower().strip()


    # Consultar nombre (debe ir antes de "me llamo")
    if "cómo me llamo" in mensaje_minuscula or "como me llamo" in mensaje_minuscula:

        nombre = obtener_dato("nombre")

        if nombre:
            print(f"AURA: Te llamas {nombre}.")
        else:
            print("AURA: Todavía no conozco tu nombre.")


    # Guardar nombre
    elif "me llamo" in mensaje_minuscula:

        nombre = mensaje.replace("me llamo", "").strip()

        guardar_dato("nombre", nombre)

        print(f"AURA: Encantada de conocerte {nombre}. Lo recordaré.")


    # Guardar objetivo
    elif "mi objetivo es" in mensaje_minuscula:

        objetivo = mensaje.replace("mi objetivo es", "").strip()

        guardar_dato("objetivo_principal", objetivo)

        print("AURA: Perfecto. Guardé tu objetivo.")


    # Consultar objetivo
    elif "cuál es mi objetivo" in mensaje_minuscula or "cual es mi objetivo" in mensaje_minuscula:

        objetivo = obtener_dato("objetivo_principal")

        if objetivo:
            print(f"AURA: Tu objetivo principal es {objetivo}.")
        else:
            print("AURA: Todavía no tengo registrado tu objetivo.")


    # Respuesta general
    else:

        nombre = obtener_dato("nombre")

        if nombre:
            print(f"AURA: Estoy aquí contigo, {nombre}. Sigo aprendiendo.")
        else:
            print("AURA: Estoy aprendiendo todavía.")