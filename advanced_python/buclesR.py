def potencias(comparador, repeat):
    sumador = 1
    valor = repeat
    print(2**comparador)
    if comparador == repeat:
        print("Se acabo")
    else: 
        comparador2 = comparador + sumador 
        potencias(comparador2, valor)


        
        

def run():
    potencias(1, num)

    

if __name__ == '__main__':
    num=int(input("Cuantas potencias de 2 quieres imprimir: "))
    run()

