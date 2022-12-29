# Сначала указываются стандартные модули
import random
import os
# Потом сторонние
import requests
# Потом свои
import food

# Вот так никогда не делайте
# import random, os, requests, food

# Но если вы импортируете часть модуля, то так делать можно
from math import gcd, log

# А вот так не очень хорошо
from math import asin
from math import acos


# Названия классов в PascalCase
class StudyCourse:
    def __init__(self):
        pass

    def get_name(self):
        return 'Test course'


# По стилю названия функций совпадают с переменными
# Перед и после функции оставляем две строчки
def get_sum(numbers):
    return sum(numbers)


def greet():
    print('Hi!')


# Варианты именования переменных (и прочего всякого)
# snake_case, правильно
number_of_items = 0
# camelCase, не рекомендуется
numberOfItems = 0
# PascalCase, неправильно
NumberOfItems = 0
# Что-то страшное, неправильно
Number_Of_Items = 0

# Константы набираются ЗАГЛАВНЫМИ_БУКВАМИ
PI = 3.14159265

a, b = 9, 5
# Длинные выражения лучше сокращать,
# убирая пробелы у более сильных операций
f = (a ** 2 + b ** 3) / 2
# То есть вот так будет неправильно
f = (a**2 + b**3) / 2

# В списках и прочих структурах первый и последний элементы
# должны стоять рядом со скобкой, т.е. вот так неправильно
data = [ 5, 7, 8, 3 ]
s = { 8, 8, 5, 4, 0 }
# А так правильно
data = [5, 7, 8, 3]
s = {8, 8, 5, 4, 0}

# Проверку на наличие элементов лучше делать не через длину ...
if len(data) > 0:
    print('Non-empty')
# А вот такой проверкой
if data:
    print('Non-empty')

result = a > b
# Сравнивать логическую переменную с True/False не стоит
if result == True:
    print('OK')
# Лучше вот так
if result:
    print('OK')

# Если в файле уже есть свой стиль кода, то придерживайтесь его :)
