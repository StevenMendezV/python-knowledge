def tables(number):
    if number == 5:
        multipler = int(input("Escoger a ver si es multiplo o no "))
        ONE = 5
        list = [num for num in range(1,100) if num % 2 == 0 ]
        for element in list:
            result = ONE * element 
            if result % multipler == 0:
                print(f""" {ONE}  x  {element}  =  {result}""")





def run():
    selection = int(input("""
Elija una de las tablas:
Tabla del 1 --> [1]
Tabla del 2 --> [2]
Tabla del 3 --> [3]
Tabla del 4 --> [4]
Tabla del 5 --> [5]
    
Opcion elegida: """))

    while selection != 1 and selection != 2 and selection != 3 and selection != 4 and selection != 5:
        selection = int(input("""
Elija una de las tablas:
Tabla del 1 --> [1]
Tabla del 2 --> [2]
Tabla del 3 --> [3]
Tabla del 4 --> [4]
Tabla del 5 --> [5]
    
Opcion elegida: """))
        continue
    print("Elegiste una tabla correcta, veremos que sucede")
    tables(selection)


if __name__ == "__main__":
    run()
