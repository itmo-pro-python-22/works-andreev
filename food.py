class Food:
    def __init__(self):
        self.name = 'Торт'
        self.taste = 'вкусный'

    def get_full_name(self):
        return f'{self.name} ({self.taste})'

cake = Food()
print(cake.name, cake.taste)

sushi = Food()
sushi.name = 'Суши'
sushi.taste = 'вегетарианские'
print(sushi.name, sushi.taste)
