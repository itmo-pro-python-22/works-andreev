def f(x: int) -> int:
    return 5 * x + 8


def transform(numbers: list) -> list:
    result: list = []
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


data: list = [3, 4, 5, 1]
res: list = transform(data)
print(res)

values: dict = {'x': 91, 'y': 2, 'z': 35}

s1: int = sum_numbers(3, 5, c=9)
s2: int = sum_numbers(3, 5, 8)
s3: int = sum_numbers(3, 5, 8, 8, 4, 6, 10, 55, 5, 41, 23, x=91, y=2, z=35)
average: float = (s1 + s2 + s3) / 3

print(s1, s2, s3, average)

# another = [3, "data", 8]
# another_res = transform(another)
# print(another_res)
