import random

def binary_search(list, start, end, target, num_iterations= 0):
    print(list)
    print(f"buscando {target} entre {list[start]} y {list[end - 1]}")
    num_iterations += 1
    print(f"Han pasado {num_iterations} pasos")

    try:
        if start > end:
            print(f"La cuenta acabó en {num_iterations} pasos")
            return (False, num_iterations)
            
        
        middle = (start + end) // 2

        if list[middle] == target:
            print(f"La cuenta acabó en {num_iterations} pasos")
            return (True, num_iterations)
        
        elif list[middle] < target:
            return binary_search(list, middle + 1, end, target, num_iterations=num_iterations)
        
        else:
            return binary_search(list, start, middle - 1, target, num_iterations=num_iterations)
    except IndexError:
        print(f"El número solicitado no se encuentra en el rango de la lista creada")


if __name__ == "__main__":
    
    list_size = int(input("¿De qué tamaño será la lista? "))
    target = int(input("¿Qué número quieres encontrar? "))

    list = sorted([random.randint(0, 100) for i in range(list_size)])

    found = binary_search(list, 0, len(list), target)
    print(list) 
    print(f"El elemento {target} {'está' if found else 'no está'} en la lista")