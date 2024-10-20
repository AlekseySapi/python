# Класс - это шаблон для создания объектов

class Human:
    def __init__(self, name, age): # Задаём начальные значения
        self.name = name
        self.age = age

    def hello(self):
        print(f"Привет, меня зовут {self.name}!")


human1 = Human("Алексей", 31)
human1.hello()

