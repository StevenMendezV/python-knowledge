# def palindromo(palabra):
#     palabra = palabra.strip()
#     palabra = palabra.lower()
#     inv_palabra = palabra[::-1]
#     if palabra == inv_palabra:
#         return True 
#     else: 
#         return False  

# def run():
#     palabra_user = input("Escribe tu palabra: ")
#     t_palindromo = palindromo(palabra_user)
#     if t_palindromo == True:
#         print("Es palindromo")
#     else:
#         print("No es palindroma")            



# if __name__ == '__main__':
#     run()    
# def palindromo(palabra):
#     palabra = str(palabra).lower().strip()
#     state= palabra and print(palabra==palabra[::-1])
#     print(state)
#     return state
    

  

# def run():
#     palabra_user = input("Escribe tu palabra: ")
#     t_palindromo = palindromo(palabra_user)
#     if t_palindromo == True:
#         print("Es palindromo")
#     else:
#         print("No es palindroma")   

  







if __name__ == '__main__':
    print("Es local")   
else:
    print("Es importado")     