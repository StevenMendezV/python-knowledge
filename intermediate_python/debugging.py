# DEBUGGING CON LIST COMPREHENSIONS
# def divisors(num):
#     divisors = [numbers for numbers in range(1, num + 1) if num % numbers == 0]
#     return divisors

# def run():
#     num = int(input("Ingrese un número entero: "))
#     print(divisors(num))
#     print("Programa finalizado")


# if __name__ == "__main__":
#     run()

# DEBUGGING CON CICLO FOR 
def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    num = int(input("Ingrese un número entero: "))
    print(divisors(num))
    print("Programa finalizado")


if __name__ == "__main__":
    run()