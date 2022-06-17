from time import sleep
def fibonacci_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

if __name__ == "__main__":
    fibonacci = fibonacci_gen()
    for element in fibonacci:
        print(element)
        sleep(1)
