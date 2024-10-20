# Класс - это шаблон для создания объектов

class Human:
    def __init__(self, name, age): # Задаём начальные значения
        self.name = name
        self.age = age

    def hello(self):
        print(f"Привет, меня зовут {self.name}!")


human1 = Human("Алексей", 31)
human1.hello()


# Наследование

class Worker(Human):
    def __init__(self, name, age, job):
        super().__init__(name, age)  # Вызываем конструктор родительского класса
        self.job = job

worker1 = Worker("Виктор", 40, "Инженер")

print("=== ===")
print(f"Имя работника: {worker1.name}")
print(f"Возраст: {worker1.age}")
print(f"Должность: {worker1.job}")