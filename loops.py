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
print("=== ===\nЧётные числа с 1 до 20: ")
for n in range(1, 21): # Написал до 21, чтобы число 20 также было учтено
    if n % 2 == 0:
        print(n)
    else:
        continue

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