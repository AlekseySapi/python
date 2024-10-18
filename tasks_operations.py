# Задание. Создать программу, которая:
# Создаёт текстовый файл tasks.txt и записывает в него несколько задач.
# Читает содержимое файла и выводит его на экран.
# Добавляет новую задачу в файл.
# Снова читает и выводит обновлённое содержимое.


file_name = 'tasks.txt'

# Создание файла и запись задач в него
with open(file_name, 'w', encoding='utf-8') as file:
    file.write("1. Изучить Python\n")
    file.write("2. Решить задачи на LeetCode\n")
    file.write("3. Создать проект на GitHub\n")

print("Задачи записаны в файл.")

# Чтение и вывод содержимого файла
with open(file_name, 'r', encoding='utf-8') as file:
    text = file.read()
    print(f"\nСодержимое файла {file_name}:")
    print(text)

# Добавление новой задачи
with open('tasks.txt', 'a', encoding='utf-8') as file:
    file.write("4. Пройти курс по машинному обучению\n")

print("Новая задача добавлена.")


# Повторное чтение и вывод обновлённого содержимого файла
with open(file_name, 'r', encoding='utf-8') as file:
    text = file.read()
    print(f"\nОбновлённое содержимое файла {file_name}:")
    print(text)