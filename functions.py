import traceback


def fact(x):
    traceback.print_stack()
    input()
    return x * fact(x - 1)


def f(x):
    return 5 * x + 8


def transform(numbers):
    result = []
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


data = [3, 4, 5, 1]
res = transform(data)
print(res)

print(sum_numbers(3, 5, c=9))
print(sum_numbers(3, 5, 8))
print(sum_numbers(3, 5, 8, 8, 4, 6, 10, 55, 5, 41, 23, x=91, y=2, z=35))
