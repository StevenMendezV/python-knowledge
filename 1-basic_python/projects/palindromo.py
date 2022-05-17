def palindrome(word):
    word = word.lower().replace(" ","")
    word_invertida = word[::-1]
    if word == word_invertida:
        return True
    else:
        return False



def run():
    word = input("Escribe una palabra: ")
    is_palindrome = palindrome(word)
    if is_palindrome == True:
        print("Es palíndromo")
    else: 
        print("No es palíndromo")


if __name__ == "__main__":
    run()
