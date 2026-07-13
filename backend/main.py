def aura_responde(mensaje):

    mensaje = mensaje.lower()

    if "hola" in mensaje:
        return "Hola Ignacio, soy AURA. ¿Cómo estás hoy?"

    elif "objetivo" in mensaje:
        return "Perfecto. Puedo ayudarte a organizar tus objetivos y crear un plan."

    elif "trabajo" in mensaje:
        return "Recuerdo que uno de tus objetivos es crecer profesionalmente y encontrar una oportunidad donde te sientas valorado."

    else:
        return "Estoy aprendiendo todavía, pero pronto podré ayudarte con más cosas."


print("🤖 AURA iniciada")
print("Escribe 'salir' para cerrar la conversación.\n")


while True:

    usuario = input("Ignacio: ")

    if usuario.lower() == "salir":
        print("AURA: Hasta pronto Ignacio. Seguimos construyendo.")
        break

    respuesta = aura_responde(usuario)

    print("AURA:", respuesta)