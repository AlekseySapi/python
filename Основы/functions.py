# Изучаю функции в Python!


# Привет
def hello():
    print("Hello, User!")

hello()


# Функция с возвращением значения (return)
a = 10
b = 20
def sum(a, b):
    return a + b

print (f"Сумма {a} и {b} = {sum(a, b)}")


# Привет с запросом имени (с аргументом)
def hello_func(name):
    print(f"Привет, {name}")

user_name = input("Как вас зовут? ")
hello_func(user_name)


print("== Функция с значением по умолчанию ==")
# Функция с значением по умолчанию
def hello_guest(name = "Guest"):
    print(f"Hello, {name}")

hello_guest()           # Default
hello_guest(user_name)  # Передал значение user_name


print(".............................")
# Если количество аргументов заранее неизвестно используют:
# *args - для передачи переменного числа позиционных аргументов
# **kwargs - для передачи переменного числа именованных аргументов
# kwargs - keyword arguments


def print_all(*args):
    return args

print(f"Все введённые числа: {print_all(1, 2, 3, 4)}")


print(".. .. .. .. .. .. .. ..")
def printPetNames(owner, **pets):
   print(f"Владелец: {owner}")
   for pet,name in pets.items():
      print(f"{pet}: {name}")
printPetNames("Иван", dog="Шарик", fish=["Коралл", "Дори", "Спарки"], turtle="Тефтелька")


# Область видимости переменных
print("== Область видимости переменных ==")


x = 10  # Глобальная переменная

def print_num():
    x = 5  # Локальная переменная
    print(f"Локальная переменная x: {x}")

print_num()  # Вывод: 5
print(f"Вывод глобальной переменной x: {x}")   # Вывод: 10 (глобальная переменная не изменилась)