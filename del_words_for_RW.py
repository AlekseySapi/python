import re

my_words = {"абсолют", "алхимик", "алхимия"}


file_path = input("Введите путь к файлу: ")

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        file_words = set(re.findall(r'\b\w+\b', file.read()))

    unique_words = file_words - my_words

    with open(file_path, 'a', encoding='utf-8') as file:
        file.write("\n=== === ===\n")
        file.write(" ".join(unique_words))

    print("Уникальные слова успешно добавлены в файл.")
except FileNotFoundError:
    print("Файл не найден. Проверьте путь.")
except Exception as e:
    print(f"Произошла ошибка: {e}")