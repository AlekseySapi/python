# Множество - это неупорядоченная коллекция уникальных элементов.
# Элементы множества должны быть неизменяемыми типами данных.

# Пустое множество
my_set = set()

# Множество с элементами
unique_numbers = {1, 2, 3, 2, 1}
print(unique_numbers)  # Вывод: {1, 2, 3}


set_a = {4, 5, 6}
set_b = {4, 10, 20, 5}
print(f"Набор 1: {set_a}")
print(f"Набор 2: {set_b}")

set_a.add(7)
set_a.add(8)
set_a.add(6)

print(f"Набор 1 после добавления 7, 8 и 6: {set_a}")
set_a.remove(6) # discard удаляет мягче (если есть элемент)
print(f"Набор 1 после удаления 6: {set_a}")

union_set = set_a.union(set_b)
print(f"Набор 1 + Набор 2: {union_set}")

# Пересечение множеств
intersection_set = set_a.intersection(set_b)
print(f"Набор 1 && Набор 2: {intersection_set}")


# Тренировка
print("== Тренировка ==")

set_1st = {1, 2, 3, 4}
set_2nd = {1, 2, 100, 1000, 9999}
print("Исходные множества:")
print("Set 1:", set_1st)
print("Set 2:", set_2nd)

set_1st.add(777)
print("Set 1 после добавления 777:", set_1st)
set_2nd.remove(1000)
print("Set 2 после удаления 1000:", set_2nd)

print("Объединение Set 1 и Set 2:", set_1st.union(set_2nd))
print("Пересечение Set 1 и Set 2:", set_1st.intersection(set_2nd))