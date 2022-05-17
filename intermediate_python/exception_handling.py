def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    while True:
        try:
            num = int(input("Ingrese un número entero: "))
            if num < 0:
                raise Exception("No son válidos los números negativos")
            print(divisors(num))
            print("Programa finalizado")
            break
        except ValueError:
            print("Solo puede ingresar numeros expresamente")
        except Exception as ex:
            print(ex)


if __name__ == "__main__":
    run()