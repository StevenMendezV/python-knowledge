# PRIMER EJEMPLO DE FUNCIONES /////////////////

# def special_message():
#     print("Mensaje Especial: ")
#     print("Estoy aprendiendo a ussar funciones")

# special_message()
# special_message()
# special_message()

# SEGUNDO EJEMPLO DE FUNCIONES //////////////////////

# menu = """
# ELIGE UNA DE ESTAS OPCIONES:

# 1 - OPCION 1 
# 2 - OPCION 2 
# 3 - OPCION 3

# ESCRIBE LA OPCION A ELEGIR: """

# option = int(input(menu))

# def options(message):
#     print("Hola")
#     print("Cómo estás")
#     print(mensaje)
#     print("Adiós")

# if option == 1:
#     options("Elegiste la opción 1")
# elif option == 2: 
#     options("Elegiste la opción 2")
# elif option == 3: 
#     options("Elegiste la opción 3")
# else:
#     options("Elige una opción correcta")

# TERCER EJEMPLO DE FUNCIONES ////////////////////

def sum(a, b): 
    print("Se van a sumar 2 números")
    result = a + b
    return result

summation = sum(1,5)
print(summation)    


