# Использую здесь данные и функции из своего модуля

import my_module

print(my_module.hello("Алексей"))
print("Число Пи = " + str(my_module.PI))


r = float(input("=== === ===\nВведите радиус круга: "))
area = my_module.circle_area(r)
print(f"Площадь круга с радиусом {r} = {area}")