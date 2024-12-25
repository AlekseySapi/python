import os
from collections import Counter

line = '\n======= ======= ======='


print(line)
while True:

    while True:
        file_path = input("Введите путь к файлу:\n> ").strip()
        if not os.path.exists(file_path):
            print("Файл не найден.")
        else:
            break

    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()


    # Оставляем только буквы, приводим к верхнему регистру
    letters = [char.upper() for char in text if char.isalpha()]

    # Подсчитываем частоту каждой буквы
    letter_counts = Counter(letters)

    # Получаем топ самых частых букв
    n = 15
    top = letter_counts.most_common(n)


    print(line)
    print(f"Топ {n} самых частых букв:")
    for i, (letter, count) in enumerate(top, start=1):
        print(f"{i}) '{letter}'  x{count}")


    
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write("\n\n===== Топ букв =====\n")
        file.write(str([char for char, _ in top]))

    print("\nРезультат в виде массива добавлен в файл.")
    print(line)