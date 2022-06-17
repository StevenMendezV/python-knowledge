import time 

class FiboIter():

    def __init__(self, max: int= 10) -> None:
        self.max = max 
    
    def __iter__(self):
        self.n1: int = 0
        self.n2: int = 1
        self.counter: int = 0
        return self

    def __next__(self):
        if self.counter != self.max:
            if self.counter == 0:   
                self.counter += 1 
                return self.n1
            elif self.counter == 1:
                self.counter += 1 
                return self.n2
            else:
                self.aux: int = self.n1 + self.n2
                # self.n1 = self.n2
                # self.n2 = self.aux
                self.n1 , self.n2 = self.n2, self.aux
                self.counter += 1
                return self.n2
        else:
            raise StopIteration

if __name__ == '__main__':
    number:int = input('How many iterations do you want to do?: ')
    if len(number) >= 1:
        try:
            number = int(number)
            succession = FiboIter(number)
            for element in succession:
                print(element)
                time.sleep(0.8)
        except ValueError:
            print('No puedes ingresar strings ni espacios en blanco.')   
    else:
        print('No ingresaste nada, por defecto la función tendrá un máximo de 10')
        succession = FiboIter()
        for element in succession:
            print(element)
            time.sleep(0.8)