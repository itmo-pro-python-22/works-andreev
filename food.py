class Food:
    count = 0

    def __init__(self, name, taste, amount=1):
        self.name = name
        self.taste = taste
        self.__amount = amount
        self.__class__.count += amount

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value):
        if value > 0:
            self.__class__.count += value - self.__amount
            self.__amount = value


    def __str__(self):
        return f'{self.name} ({self.taste}), {self.__amount} left'

    def __eq__(self, other):
        return type(other) == Food and self.name == other.name and self.taste == other.taste

    @classmethod
    def get_report(cls):
        return f'We have {cls.count} food items'

    def consume(self):
        if self.__amount > 0:
            print(f'{self.name} was eaten')
            self.__amount -= 1
            self.__class__.count -= 1
        else:
            print(f'No {self.name} left')


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

    def consume(self):
        print(f'{self.name} was drunk')


cake = Food('Торт', 'вкусный')
print(cake)

sushi = Food('Суши', 'вегетарианские')
print(sushi)

print(Food.get_report())
sushi.consume()
sushi.amount += 3

latte = Drink('Латте', 'Кофе', 220)
print(latte)

kvass = Drink('Натуральный', 'Квас', 150)
print(kvass)

print(sushi == 5)

for item in cake, sushi, latte, kvass:
    item.consume()
    print(item)
