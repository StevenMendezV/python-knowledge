import random

def bubble_sort(list):
    n = len(list)

    for i in range(n):
        print(f"La variable i vale: {i}")
        for j in range(0, n - i - 1): # El 1 lo utilizamos porque la funcion len() arroja longitud, u nosotros queremos referirnos a valores posicionales
            print(f"\nSe resta n: {n} MENOS i: {i} MENOS 1 Y ES IGUAL A ---------> {n - i - 1} ")
            if list[j] > list[j + 1]:
                list[j] , list[j + 1] = list[j + 1] , list[j]
    return list 


if __name__ == "__main__":
    
    list_size = int(input("¿De qué tamaño será la lista? "))

    list = [random.randint(0, 100) for i in range(list_size)]
    print(list)
    sorted_list = bubble_sort(list)
    print(sorted_list)
