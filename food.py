class Item:
    count = 0

    def __init__(self, name, amount=1):
        self.name = name
        self._amount = amount
        self.__class__.count += amount

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, new_amount):
        if new_amount > 0:
            self.__class__.count += new_amount - self._amount
            self._amount = new_amount


class Food(Item):
    def __init__(self, name, taste, amount=1):
        super().__init__(name, amount)
        self.taste = taste

    def __str__(self):
        return f'{self.name} ({self.taste}), {self._amount} left'

    def __eq__(self, other):
        return type(other) == Food and self.name == other.name and self.taste == other.taste

    @classmethod
    def get_report(cls):
        return f'We have {cls.count} food items'

    def consume(self):
        if self._amount > 0:
            print(f'{self.name} was eaten')
            self._amount -= 1
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
    print(item.name)
