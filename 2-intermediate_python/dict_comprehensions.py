# EJEMPLO DE DICTIONARY COMPREHENSIONS 
# def run():
#     squares = {i: i**3 for i in range(1 ,101) if i % 3 != 0}
#     print(squares)


# if __name__ == "__main__":
#     run()

# PRACTICA DE DICTIONARY COMPREHENSIONS 
def run():
    roots = {i: round(i**0.5, 2) for i in range(1,1001)}
    print(roots)


if __name__ == "__main__":
    run()