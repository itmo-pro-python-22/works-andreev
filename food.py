class Food:
    def __init__(self, name, taste):
        self.name = name
        self.taste = taste

    def get_full_name(self):
        return f'{self.name} ({self.taste})'


class Drink:
    def __init__(self, name, drink_type, price):
        self.name = name
        self.type = drink_type
        self.price = price

    def get_full_name(self):
        return f'{self.type} "{self.name}" ({self.price})'


cake = Food('Торт', 'вкусный')
print(cake.get_full_name())

sushi = Food('Суши', 'вегетарианские')
print(sushi.get_full_name())

latte = Drink('Латте', 'Кофе', 220)
print(latte.get_full_name())
