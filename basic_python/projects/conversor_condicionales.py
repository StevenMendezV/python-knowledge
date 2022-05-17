menu = """
BIENVENIDO AL CONVERSOR DE MONEDAS 🤑

1 - Pesos Colombianos
2 - Pesos Argentinos 
3 - Pesos Mexicanos

Elige una de estas opciones: """

option = int(input(menu))

if option == 1:
    pesos = input("Ingrese la cantidad de pesos colombianos: ")
    pesos = float(pesos)
    dollar_valor = 3949
    dollars = pesos / dollar_valor
    dollars = round(dollars, 2)
    dollars = str(dollars)
    print("Tienes $" + dollars + " dólares ❤💙")
elif option == 2:
    pesos = input("Ingrese la cantidad de pesos argentinos: ")
    pesos = float(pesos)
    dollar_valor = 65
    dollars = pesos / dollar_valor
    dollars = round(dollars, 2)
    dollars = str(dollars)
    print("Tienes $" + dollars + " dólares ❤💙")
elif option == 3:
    pesos = input("Ingrese la cantidad de pesos mexicanos: ")
    pesos = float(pesos)
    dollar_valor = 24
    dollars = pesos / dollar_valor
    dollars = round(dollars, 2)
    dollars = str(dollars)
    print("Tienes $" + dollars + " dólares ❤💙")
else:
    print("Ingrese una opción correcta")