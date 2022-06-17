def with_custom_message(message):
    def with_message(func):
        print(f'{message}:')
        def wrapper(*args, **kwargs):
            func(*args, **kwargs)
        return wrapper
    return with_message

@with_custom_message('Hello')
def multiply(a, b):
    c= a*b
    print(f'The result of {a} * {b} is {c}')

multiply(10, 2)
