# def run():
    # for contador in range(1000):
    #     if contador % 2 == 0:
    #         continue
    #     print(contador)
    # for i in range(10000):
    #     print(i)
    #     if i == 9995:
    #         break
#     texto = input("Escribe un texto: ")
#     for i in texto:
#         if i == texto[0]:
#             continue
#         print(i)


# if __name__=='__main__':
#     run()

opcion = int(input("Escribe 1 o 2: "))

while opcion != 1  and opcion != 2:
    print("Ingrese una opcion valida") #47
    opcion = int(input("Escribe 1 o 2: "))
    continue
print("Esa si era una opcion valida")