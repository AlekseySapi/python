for i in range(3):
    print(i)


print("===")

k = 5
print(f"Печатаем {k} строк:")
count = 1
while count <= k:
    print(count)
    count += 1



# === Тренировка ===

# Вывод чётных чисел с помощью цикла for
print("=== ===\nЧётные числа от 1 до 21: ")
for n in range(2, 21, 2): # Написал до 21, чтобы число 20 также было учтено
    print(n)    # Использовал шаг - 2 (третье число)

# Найти первое число после 10, которое делится на 9 (с помощью while)
print("=== === ===")
m = 11
while m % 9 != 0:
    print(f":: {m} не делится на 3")
    m += 1
print(f"Первое число после 10, которое делится на 3: {m}")

# Вывод чисел, которые не делятся на 2
print(f"=== === ===\nЧисла, которые не делятся на 2:")
for p in range(1, 10):
    if p % 2 == 0:
        continue
    else:
        print(p)

# Поиск числа с помощью break
start_num = 100
find_num = 27
t = start_num
while True:
    if t % find_num == 0:
        break
    t += 1
print(f"=== === ===\nПервое число после {start_num}, которое делится на {find_num}: {t}")


# Использую синтаксический сахар (i for i..), для сокращения кода
print("\n\n=== === ===\nОднострочный цикл")
nums = [i for i in range(105, 99, -1)]  # Шаг -1
print(nums)

print("\n=== === ===\nТолько чётные")
print([i for i in range(105, 95, -1) if i % 2 == 0])

print("\n=== === ===\nУмноженные на 10")
print([i * 10 for i in range(105, 95, -1) if i % 2 == 0])