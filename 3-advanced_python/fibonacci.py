import time 

def fibo_gen(max: int= 10):
    n1: int = 0
    n2: int = 1 
    counter:int = 0
    if counter != max:
        while True:
            if counter == 0:
                counter += 1
                yield n1
            elif counter == 1:
                counter += 1
                yield n2
            else:
                counter += 1
                aux:int + int= n1 + n2 
                n1, n2 = n2, aux
                yield n2
    else:
        raise StopIteration
        
def run():
    fibonacci = fibo_gen()
    for element in fibonacci:
        print(element)
        time.sleep(1)

if __name__ == '__main__':
    run()