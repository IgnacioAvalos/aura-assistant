from database import guardar_usuario, obtener_usuario
from cerebro import analizar_mensaje


print("🤖 AURA iniciada")
print("Escribe 'salir' para terminar\n")


while True:

    mensaje = input("Ignacio: ")


    if mensaje.lower().strip() == "salir":

        print("AURA: Hasta pronto Ignacio. Seguimos construyendo.")
        break


    resultado = analizar_mensaje(mensaje)


    accion = resultado["accion"]


    # Guardar nombre

    if accion == "guardar_nombre":

        nombre = resultado["dato"]

        guardar_usuario(nombre=nombre)

        print(
            f"AURA: Encantada de conocerte {nombre}. Lo recordaré."
        )


    # Consultar nombre

    elif accion == "consultar_nombre":

        usuario = obtener_usuario()


        if usuario and usuario[0]:

            print(
                f"AURA: Te llamas {usuario[0]}."
            )

        else:

            print(
                "AURA: Todavía no conozco tu nombre."
            )



    # Guardar objetivo

    elif accion == "guardar_objetivo":

        objetivo = resultado["dato"]


        usuario = obtener_usuario()

        nombre = None


        if usuario:

            nombre = usuario[0]


        guardar_usuario(
            nombre=nombre,
            objetivo=objetivo
        )


        print(
            "AURA: Perfecto. Guardé tu objetivo."
        )



    # Consultar objetivo

    elif accion == "consultar_objetivo":

        usuario = obtener_usuario()


        if usuario and usuario[1]:

            print(
                f"AURA: Tu objetivo es {usuario[1]}."
            )

        else:

            print(
                "AURA: Todavía no tengo registrado tu objetivo."
            )



    # No entendido

    else:

        usuario = obtener_usuario()


        if usuario and usuario[0]:

            print(
                f"AURA: Estoy aquí contigo, {usuario[0]}. Sigo aprendiendo."
            )

        else:

            print(
                "AURA: Estoy aprendiendo todavía."
            )