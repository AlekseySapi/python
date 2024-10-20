# Класс - это шаблон для создания объектов

class Human:
    def __init__(self, name, age):      # Задаём начальные значения
        self.name = name
        self.age = age

    def hello(self):
        print(f"Привет, меня зовут {self.name}!")


human1 = Human("Алексей", 31)
human1.hello()


# Наследование

class Worker(Human):
    def __init__(self, name, age, job):
        super().__init__(name, age)     # Вызываем конструктор родительского класса
        self.job = job

worker1 = Worker("Виктор", 40, "Инженер")

print("=== ===")
print(f"Имя работника: {worker1.name}")
print(f"Возраст: {worker1.age}")
print(f"Должность: {worker1.job}")


# Инкапсуляция - скрытие атрибутов и методов из публичного доступа

class Account:
    def __init__(self):
        self.__cash = 0     # Приватный атрибут
        
    def add_cash(self, money):
        self.__cash += money

    def get_cash(self):
        return self.__cash
    
my_acc = Account()

print("===")
print(f"Начальный баланс: {my_acc.get_cash()}")
my_acc.add_cash(1000)       # Добавляем 1000 кредитов
print(f"Текущий баланс: {my_acc.get_cash()}")