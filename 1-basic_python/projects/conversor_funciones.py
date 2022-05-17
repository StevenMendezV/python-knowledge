def converter(type_pesos, dollar_valor):
    pesos = int(input("\nIngrese la cantidad de pesos  " + type_pesos + " que tiene: "))
    pesos = float(pesos)
    dollars = pesos / dollar_valor
    dollars = round(dollars, 2)
    dollars = str(dollars)
    print("Tiene " + dollars + " dólares")

menu = """
BIENVENIDO AL CONVERSOR DE MONEDAS 🤑

1 - Pesos Colombianos
2 - Pesos Argentinos 
3 - Pesos Mexicanos

Elige una de estas opciones: """

option = int(input(menu))

if option == 1:
    converter("colombianos", 3949)
elif option == 2:
    converter("argentinos", 65)
elif option == 3:
    converter("mexicanos", 24)
else:
    print("ingrese la opción correcta")


