from typing import List, Callable


def operator(operation: str) -> Callable[[int, int], int]:
    if operation == '+':
        return lambda a, b: a + b
    elif operation == '*':
        return lambda a, b: a * b
    else:
        raise ValueError(f'Wrong operation {operation}')


def f(x: int) -> int:
    return 7 ** x - 9


print(operator('*')(5, 8))

data: List[int] = [3, -2, -7, 6, 4, 0, -5]
data.sort(key=lambda x: x ** 2)
print(*data)

# Callable[[Типы параметров], Тип возвр. значения]
another_f: Callable[[int], int] = f

data.sort(key=another_f)
print(*data)
