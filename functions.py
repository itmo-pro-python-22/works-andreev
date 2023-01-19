from typing import List, Dict, Tuple, Union, Optional

Number = Union[int, float]
OptionalInt = Optional[int]


def f(x: Number) -> Number:
    return 5 * x + 8


def transform(numbers: List[Number]) -> List[Number]:
    result: List[Number] = []
    for x in numbers:
        result.append(f(x))
    return result


def sum_numbers(a, b, *args, **kwargs):
    print(kwargs)
    s = 0
    for x in args:
        s += x
    for key in kwargs:
        s += kwargs[key]
    return a + b + s


print(f(5))
print(f(5.0))

x: OptionalInt = 8
y: OptionalInt = None
z: OptionalInt = 'aewrth'

data: List[int] = [3, 4, 5, 1]
# data.append('Test')
res: List[int] = transform(data)
print(res)

values: Dict[str, int] = {'x': 91, 'y': 2, 'z': 35}
# values[5] = 5
# values['u'] = 'aesrdgh'

info: Tuple[str, int] = ("Андреев Н.В.", 24)

s1: int = sum_numbers(3, 5, c=9)
s2: int = sum_numbers(3, 5, 8)
s3: int = sum_numbers(3, 5, 8, 8, 4, 6, 10, 55, 5, 41, 23, x=91, y=2, z=35)
average: float = (s1 + s2 + s3) / 3

print(s1, s2, s3, average)

# another: List[str] = ["aefsrgdfc", "data", "dsfghjfhgre"]
# another_res: List[str] = transform(another)
# print(another_res)
