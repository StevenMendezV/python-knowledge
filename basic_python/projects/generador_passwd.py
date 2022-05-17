import random

def password_generator():
    MAYUS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', \
        'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    MINUS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', \
        'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    CHARS = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', \
        '<', '~', '°', '^', '&', '$', '#', '"']

    characters = MAYUS + MINUS + NUMS + CHARS

    user_password = []

    for i in range(15):
        random_character = random.choice(characters)
        user_password.append(random_character)

    user_password = "".join(user_password)
    return user_password    



def run():
    password = password_generator()
    print("Tu nueva contraseña es: " + password)


if __name__ == "__main__":
    run()

