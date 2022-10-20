class Food:
    def __init__(self, name, taste):
        self.name = name
        self.taste = taste

    def __str__(self):
        return f'{self.name} ({self.taste})'

    def __eq__(self, other):
        return type(other) == Food and self.name == other.name and self.taste == other.taste


class Drink:
    def __init__(self, name, drink_type, price):
        self.name = name
        self.type = drink_type
        self.price = price

    def __str__(self):
        return f'{self.type} "{self.name}" ({self.price})'


cake_1 = Food('Торт', 'вкусный')
cake_2 = Food('Торт', 'вкусный')
print(cake_1 == cake_2)

sushi = Food('Суши', 'вегетарианские')
print(sushi)

latte = Drink('Латте', 'Кофе', 220)
print(latte)

print(sushi == 5)
