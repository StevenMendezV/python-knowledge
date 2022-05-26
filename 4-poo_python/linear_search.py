import random

def linear_search(list, target):
    match = False

    for element in list:
        if element == target:
            match = True
            break
    return match 

if __name__ == "__main__":
    
    list_size = int(input("¿De qué tamaño será la lista? "))
    target = int(input("¿Qué número quieres encontrar? "))

    list = [random.randint(0, 100) for i in range(list_size)]

    found = linear_search(list, target)
    print(list) 
    print(f"El elemento {target} {'está' if found else 'no está'} en la lista")
