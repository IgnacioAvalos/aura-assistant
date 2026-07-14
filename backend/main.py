from database import guardar_usuario, obtener_usuario


print("🤖 AURA iniciada")
print("Escribe 'salir' para terminar\n")


while True:

    mensaje = input("Ignacio: ")

    if mensaje.lower().strip() == "salir":
        print("AURA: Hasta pronto Ignacio. Seguimos construyendo.")
        break


    mensaje_minuscula = mensaje.lower().strip()


    # Consultar nombre
    if "cómo me llamo" in mensaje_minuscula or "como me llamo" in mensaje_minuscula:

        usuario = obtener_usuario()

        if usuario and usuario[0]:

            print(f"AURA: Te llamas {usuario[0]}.")

        else:

            print("AURA: Todavía no conozco tu nombre.")



    # Guardar nombre
    elif "me llamo" in mensaje_minuscula:

        nombre = mensaje.replace("me llamo", "").strip()

        guardar_usuario(nombre=nombre)

        print(f"AURA: Encantada de conocerte {nombre}. Lo recordaré.")



    # Guardar objetivo
    elif "mi objetivo es" in mensaje_minuscula:

        objetivo = mensaje.replace("mi objetivo es", "").strip()

        usuario = obtener_usuario()

        nombre = None

        if usuario:
            nombre = usuario[0]


        guardar_usuario(
            nombre=nombre,
            objetivo=objetivo
        )


        print("AURA: Perfecto. Guardé tu objetivo.")



    # Consultar objetivo
    elif "cuál es mi objetivo" in mensaje_minuscula or "cual es mi objetivo" in mensaje_minuscula:

        usuario = obtener_usuario()


        if usuario and usuario[1]:

            print(f"AURA: Tu objetivo es {usuario[1]}.")

        else:

            print("AURA: Todavía no tengo registrado tu objetivo.")



    else:

        usuario = obtener_usuario()


        if usuario and usuario[0]:

            print(f"AURA: Estoy aquí contigo, {usuario[0]}. Sigo aprendiendo.")

        else:

            print("AURA: Estoy aprendiendo todavía.")