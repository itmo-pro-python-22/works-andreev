from typing import Any
from time import sleep


class Repeater:
    def __init__(self, value: Any):
        self.value: Any = value

    def __iter__(self):
        return self

    def __next__(self) -> Any:
        return self.value


class Counter:
    def __init__(self, start: int, end: int):
        self.start: int = start
        self.end: int = end
        self.value: int = start

    def __iter__(self):
        self.value = self.start
        return self

    def __next__(self):
        if self.value == self.end:
            print('Raising StopIteration')
            raise StopIteration
        self.value += 1
        return self.value


# data = [8, 4, 3]
# data = Repeater(3)
data = Counter(5, 10)

for x in data:
    print(x)
    sleep(1)

for x in data:
    print(x)
    sleep(1)

# iterator = iter(data)
#
# while True:
#     x = None
#     try:
#         x = next(iterator)
#     except StopIteration:
#         break
#     print(x)
