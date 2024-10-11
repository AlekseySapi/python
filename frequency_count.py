# Программа для подсчёта частоты слов в тексте

# Напиши программу, которая принимает строку текста и подсчитывает,
#  сколько раз каждое слово встречается в этом тексте.
# Программа должна выводить слова и количество их повторений.

# Программа должна игнорировать регистр букв (например, «Привет» и «привет» — это одно и то же слово).
# Программа должна учитывать только слова, то есть игнорировать знаки пунктуации.
# Вывод должен быть отсортирован по частоте слов (от самых частых к менее частым)

import string
from collections import Counter


text = input("Введите текст: ")


def preprocess_text(text):
    # Преобразуем строку в нижний регистр
    text = text.lower()

    # Создаём таблицу перевода: каждый символ пунктуации будет заменён на None
    translator = str.maketrans('', '', string.punctuation)

    # Удаляем пунктуацию
    text = text.translate(translator)

    # Разделяем строку на слова
    words = text.split()

    return words

words = preprocess_text(text)
# print(words)


# Подсчёт частоты слова в тексте
frequency = Counter(words)
# Сортировка частоты
sorted_frequency = frequency.most_common()

    
# Вывод результата
for word, count in sorted_frequency:
    print(f"{word}: {count}")
