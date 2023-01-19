from abc import abstractmethod


class Item:
    count: int = 0
    name: str
    price: int
    _amount: int

    def __init__(self, name: str, price: int, amount: int = 1) -> None:
        self.name = name
        self.price = price
        self._amount = amount
        self.__class__.count += amount

    @property
    def amount(self) -> int:
        return self._amount

    @amount.setter
    def amount(self, new_amount: int) -> None:
        if new_amount > 0:
            self.__class__.count += new_amount - self._amount
            self._amount = new_amount
        else:
            raise ValueError('Cannot save negative amount')

    def __str__(self):
        return f'{self.name} ({self.price}), {self._amount} left'


class ItemFileExporter:
    def __init__(self, filename):
        self._filename = filename

    def export(self, items):
        file = open(self._filename, 'w', encoding='utf-8')
        for item in items:
            print(item, file=file)
        file.close()


class ItemCsvExporter(ItemFileExporter):
    def export(self, items):
        file = open(self._filename, 'w', encoding='utf-8')
        for item in items:
            print(item.name, item.price, item.count, sep=',', file=file)
        file.close()


class IConsumable:
    @abstractmethod
    def consume(self):
        pass


class ICookable:
    @abstractmethod
    def cook(self):
        pass


class IBrewable:
    @abstractmethod
    def brew(self):
        pass


class Food(Item, IConsumable, ICookable):
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

    def cook(self):
        pass


class Drink(Item, IConsumable, IBrewable):
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

    def brew(self):
        pass


cake = Food('Торт', 'вкусный', 360)
sushi = Food('Суши', 'вегетарианские', 550, 3)
latte = Drink('Латте', 'Кофе', 330)
kvass = Drink('Натуральный', 'Квас', 150, 5)
dual_sense = Item('DualSense 5', 7000)

cake.amount += 5
cake.amount -= 10


for item in cake, sushi, latte, kvass, dual_sense:
    print(item)

exporter = ItemFileExporter('items.txt')
exporter.export([cake, sushi, latte, kvass, dual_sense])

table_exporter = ItemCsvExporter('items.csv')
table_exporter.export([cake, sushi, latte, kvass, dual_sense])
