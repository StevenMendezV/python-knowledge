import time 

def fibo_gen(max: int= 10):
    n1: int = 0
    n2: int = 1 
    counter:int = 0

    while True:
        try:
            if counter != max:
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
        except StopIteration:
            print('Se acabó la iteración')
            break

        
def run():
    number:int = input('How many iterations do you want to do?: ')
    if len(number) >= 1:
        try:
            number = int(number)
            succession = fibo_gen(number)
            for element in succession:
                print(element)
                time.sleep(0.8)
        except ValueError:
            print('No puedes ingresar strings')   
    else:
        print('No ingresaste nada, por defecto la función tendrá un máximo de 10')
        succession = fibo_gen()
        for element in succession:
            print(element)
            time.sleep(0.8)

if __name__ == '__main__':
    run()