# Использую здесь данные и функции из своего модуля

import my_module

print(my_module.hello("Алексей"))
print("Число Пи = " + str(my_module.PI))


'''
r = float(input("=== === ===\nВведите радиус круга: "))
area = my_module.circle_area(r)
print(f"Площадь круга с радиусом {r} = {area}")
'''

while True:
    while True:
        user_input = input("=== === ===\nВведите степень двойки: ")
        try:
            p = int(user_input)  # Пробуем преобразовать в число
            break  # Выход из цикла, если ввод корректный
        except ValueError:
            print("Ошибка: Нужно вводить только числа. Попробуйте снова.")

    res = my_module.power_of_two(p)
    print(f"2^{p} = {res}")