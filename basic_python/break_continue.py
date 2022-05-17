# PRIMER EJEMPLO DE INTERRUPCION EN CICLOS CON CONTINUE ////////////7

# def run():
#     for counter in range(1000):
#         if counter % 2 != 0:
#             continue
#         print(counter)

# if __name__ == "__main__":
#     run()

# SEGUNDO EJEMPLO DE INTERRUPCION EN CICLOS CON BREAK //////////////////////

# def run():
#     for i in range(0, 10000):
#         print(i)
#         if i == 5678:
#             break


# if __name__ == "__main__":
#     run()

# TERCER EJEMPLO DE INTERRUPCION EN CICLOS CON BREAK CON STRINGS //////////////////////

def run():
    text = input("Escribe un texto: ")
    for letter in text:
        if letter == "o":
            break
        print(letter)


if __name__ == "__main__":
    run()
