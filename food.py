class Item:
    count = 0

    def __init__(self, name, price, amount=1):
        self.name = name
        self.price = price
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

    def __str__(self):
        return f'{self.name} ({self.price}), {self._amount} left'


class ItemFileExporter:
    def __init__(self, filename):
        self.__filename = filename

    def export(self, items):
        file = open(self.__filename, 'w')
        for item in items:
            print(item, file=file)
        file.close()


class Food(Item):
    def __init__(self, name, taste, price, amount=1):
        super().__init__(name, price, amount)
        self.taste = taste

    def __str__(self):
        return f'{self.name} ({self.taste}) ({self.price}), {self._amount} left'

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


class Drink(Item):
    def __init__(self, name, drink_type, price, amount=1):
        super().__init__(name, price, amount)
        self.type = drink_type

    def __str__(self):
        return f'{self.type} "{self.name}" ({self.price}), {self._amount} left'

    @classmethod
    def get_report(cls):
        return f'We have {cls.count} drinks'

    def consume(self):
        if self._amount > 0:
            print(f'{self.name} was drunk')
            self._amount -= 1
            self.__class__.count -= 1
        else:
            print(f'No {self.name} left')


cake = Food('Торт', 'вкусный', 360)
sushi = Food('Суши', 'вегетарианские', 550, 3)
latte = Drink('Латте', 'Кофе', 220)
kvass = Drink('Натуральный', 'Квас', 150, 5)
dual_sense = Item('DualSense 5', 7000)


for item in cake, sushi, latte, kvass, dual_sense:
    # item.consume()
    print(item)

exporter = ItemFileExporter('items.txt')
exporter.export([cake, sushi, latte, kvass, dual_sense])
