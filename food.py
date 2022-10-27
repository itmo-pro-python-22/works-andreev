class Food:
    count = 0

    def __init__(self, name, taste):
        self.name = name
        self.taste = taste
        self.__class__.count += 1

    def __str__(self):
        return f'{self.name} ({self.taste})'

    def __eq__(self, other):
        return type(other) == Food and self.name == other.name and self.taste == other.taste

    @classmethod
    def get_report(cls):
        return f'We have {cls.count} food items'

    @staticmethod
    def eat():
        print('Food was eaten')


class Drink:
    count = 0

    def __init__(self, name, drink_type, price):
        self.name = name
        self.type = drink_type
        self.price = price
        self.__class__.count += 1

    def __str__(self):
        return f'{self.type} "{self.name}" ({self.price})'

    @classmethod
    def get_report(cls):
        return f'We have {cls.count} drinks'

    @staticmethod
    def drink():
        print('Drink was drunk')


cake_1 = Food('Торт', 'вкусный')
cake_2 = Food('Торт', 'вкусный')
cake_1.name = 'Тортик'
print(cake_1 == cake_2)

sushi = Food('Суши', 'вегетарианские')
print(sushi)

print(Food.get_report())
Food.eat()
sushi.eat()

latte = Drink('Латте', 'Кофе', 220)
print(latte)

kvass = Drink('Натуральный', 'Квас', 150)
print(kvass)

Drink.drink()

print(sushi == 5)
