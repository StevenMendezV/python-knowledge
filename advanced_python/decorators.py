# Tecnico
from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time=datetime.now()
        func(*args, **kwargs)
        final_time=datetime.now()
        time_elapsed=final_time-initial_time
        print("pasaron " + str(time_elapsed.total_seconds()) + " segundos")
    return wrapper

@execution_time
def random_func():
    for _ in range(1,10000000):
        pass
random_func()

def suma(a: int, b: int)-> int:
    return a+b
print(suma(5,2))
suma = execution_time(suma)
suma(5,2)



def saludo(nombre="Cesars"):
    print("hola " + nombre)
saludo = execution_time(saludo)
saludo("Steven")































# sugar sintact
# from datetime import datetime

# def execution_time(func):
#     def wrapper():
#         initial_time=datetime.now()
#         func()
#         final_time=datetime.now()
#         time_elapsed=final_time-initial_time
#         print("pasaron " + str(time_elapsed.total_seconds()) + " segundos")
#     return wrapper

# @execution_time
# def random_func():
#     for _ in range(1,10000000):
#         pass
# random_func()

# def execution_time(func):
#     def wrapper():
#         initial_time=datetime.now()
#         func()
#         final_time=datetime.now()
#         time_elapsed=final_time-initial_time
#         print("pasaron " + str(time_elapsed.total_seconds()) + " segundos")
#     return wrapper


# def random_func():
#     for _ in range(1,10000000):
#         pass

# penelope = execution_time(random_func)
# penelope()