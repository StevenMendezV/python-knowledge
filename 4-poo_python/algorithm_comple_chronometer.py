import sys
import time
sys.setrecursionlimit(10000)

def factorial(n):
    answer = 1

    while n > 1:
        answer *= n
        n -= 1
    
    return answer

def recursive_factorial(n):
    if n == 1:
        return 1
    return recursive_factorial(n - 1)

if __name__ == "__main__":
    n = 3492   # solo llega hasta 3492
    start = time.time()
    factorial(n)
    end = time.time()
    print(f"En loop tarda {end - start}")

    start = time.time()
    print("Hasta aquí funciona 1")
    print(recursive_factorial(n))
    print("Hasta aquí funciona 2")
    end = time.time()
    print(f"En recursivo tarda {end - start}")
