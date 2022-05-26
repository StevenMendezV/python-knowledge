# def funcion_decoradora(funcion):
# 	def wrapper():
# 		print("Este es el último mensaje...")
# 		funcion()
# 		print("Este es el primer mensaje ;)")
# 	return wrapper

# def zumbido():
# 	print("Buzzzzzz")

# zumbido = funcion_decoradora(zumbido)
# zumbido()

# def multiplicacion(x):
#     def multiplicar(n):
#         return x * n
#     return multiplicar

# test = multiplicacion(10)
# print(test(5))

def decorator(func):
    def wrapper():
        print("Ya domino los decoradores")
        func()
        print("Excelente")
    return wrapper

@decorator
def message():
    print("Prueba")

message()

        
