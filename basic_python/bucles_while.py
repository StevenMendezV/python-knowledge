# PRIMER EJEMPLO DE BUCLE WHILE //////////////

# def run():
#     LIMITE = 10000
    
#     counter = 0
#     potencia_2 = 2**counter
#     while potencia_2 < LIMITE:
#         print("2 elevado a " + str(counter) + " es igual a: " + str(2**counter))
#         counter = counter + 1
#         potencia_2 = 2**counter


# if __name__ == "__main__":
#     run()

# SEGUNDO EJEMPLO DE BUCLE WHILE ///////////////////////

# counter = 0 
# print(counter)

# while counter < 1000:
#     counter += 1
#     print(counter)

# TERCER EJEMPLO DE BUCLE WHILE ///////////////////////

def run():
    message = input("Escribe un tweet: ")
    message_characters = len(message)
    tweet = 30
    while True:
        print("\n💙Tweet original: " + message + "💙\n")
        desicion = input("¿Deseas enviar el mensaje?: ")
        if desicion.lower().replace("í","i") == "si":
            if message_characters > tweet:
                print("Te excediste en la cantidad de caracteres, que son 30 ")
                print("Tu tweet tiene " + str(message_characters) + " caracteres.")
                break
            else:
                print("!Has tweeteado un tweet!")
        else:
            print("Error al enviar el tweet")
        break





    


if __name__ == "__main__":
    run()