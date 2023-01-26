from typing import Callable, Any


def f(x: int) -> int:
    return x // 2 + 7 ** x


def logger(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        print('Start function')
        func(*args, **kwargs)
        print('End function')
    return wrapper


@logger
def greet(name: str) -> None:
    print(f'Hello {name}!')


greet('Nick')
greet('money')
