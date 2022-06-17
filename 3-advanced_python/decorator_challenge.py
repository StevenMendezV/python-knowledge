from datetime import datetime

def execution_time(func: object) -> object:
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        total_time = final_time - initial_time
        print(f'{total_time.total_seconds()} seconds elapsed')
    return wrapper

@execution_time
def random_func():
    for _ in range(1, 100000000):
        pass

@execution_time
def sum(a: int, b:int) -> int:
    return a + b

@execution_time
def greetings(name: str= 'Cesar') -> None:
    print(f'Hello {name}')


def run():
    random_func()
    sum(5, 5)
    greetings()

if __name__ == "__main__":
    run()