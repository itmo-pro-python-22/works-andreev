class Staff:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.__salary = salary

    def set_salary(self, new_salary):
        if 50_000 <= new_salary <= 100_000:
            self.__salary = new_salary

    def get_salary(self):
        return self.__salary

    def __str__(self):
        return f'Staff({self.name}, {self.position}, {self.__salary})'


admin = Staff('Иванов Иван Иванович', 'Администратор зала', 75_000)
print(admin)
admin.set_salary(750_000)
print(admin)
admin.set_salary(65_000)
print(admin)
print(admin.get_salary())
