# forma tecnica
# def message(func):
#     def wrap():
#         print("Esto se añade a eso")
#         func()
#     return wrap 

# def func():
#     print("algo escrito aqui")

# func = message(func)
# func()

# suggar sintac

def decorador(func):
    def wrap():
        print("Esto se añade a eso")
        func()
    return wrap 

@decorador
def func():
    print("algo escrito aqui")

func()