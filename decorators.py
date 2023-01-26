from typing import List, Callable


def f(x: int) -> int:
    return 7 ** x - 9


data: List[int] = [3, -2, -7, 6, 4, 0, -5]
data.sort(key=lambda x: x ** 2)
print(*data)

# Callable[[Типы параметров], Тип возвр. значения]
calc: Callable[[int], int] = f

data.sort(key=calc)
print(*data)
