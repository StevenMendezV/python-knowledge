# def run ():
#     squares = []
#     for i in range(1,101):
#         if i % 3 != 0: 
#             squares.append(i**2)

#     print(squares)

# if __name__=='__main__':
#     run()

def run ():
    squares=[i for i in range(1, 100000) if i % 36 == 0]
    print(squares)


if __name__=='__main__':
    run()