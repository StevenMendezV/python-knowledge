def divisors(num):
    divisors = [numbers for numbers in range(1, num + 1) if num % numbers == 0]
    return divisors

def run():
    num = input("Ingrese un número entero: ")
    assert num.isnumeric() and int(num.isnumeric()) > 0, "Solamente ingrese números enteros positivos"
    print(divisors(int(num)))
    print("Programa finalizado")


if __name__ == "__main__":
    run()