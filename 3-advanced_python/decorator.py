
def mayus(func: object) -> object:
    def wrapper(string: str) -> object:
        return func(string).upper()
    return wrapper

@mayus
def message(name: str) -> str:
    return f'{name}, you have received a message!'

print(message('Cesar'))