# NUMEROS DEL 0 AL 100 AL CUADRADO CON CICLO FOR Y ESTRUCTURA LIST 
# def run():
#     squares = []
#     for i in range(0,101):
#         squares.append(i**2)
#     print(squares)


# if __name__ == "__main__":
#     run()

# NUMEROS DEL 0 AL 100 AL CUADRADO QUE NO SON DIVISIBLES POR 3 CON CICLO FOR Y ESTRUCTURA LIST
# def run():
#     squares = []
#     for i in range(0,101):
#         if i % 3 == 0:
#             continue
#         else:
#             squares.append(i ** 2)
#     print(squares)


# if __name__ == "__main__":
#     run()

# NUMEROS DEL 0 AL 100 AL CUBO CON CICLO FOR Y ESTRUCTURA DE DICCIONARIO 
# def run():
#     squares = {}
#     for i in range(1,101):
#         squares[i] = i**3
#     print(squares)


# if __name__ == "__main__":
#     run()

# NUMEROS DEL 0 AL 100 AL CUBO QUE NO SON DIVISIBLES POR 3 CON CICLO FOR Y ESTRUCTURA DICCIONARIO
def run():
    squares = {}
    for i in range(1,101):
        if i % 3 != 0:
            squares[i] = i**3
    print(squares)


if __name__ == "__main__":
    run()
