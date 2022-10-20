class Food:
    def __init__(self, name, taste):
        self.name = name
        self.taste = taste

    def get_full_name(self):
        return f'{self.name} ({self.taste})'


cake = Food('Торт', 'вкусный')
print(cake.get_full_name())

sushi = Food('Суши', 'вегетарианские')
print(sushi.get_full_name())
