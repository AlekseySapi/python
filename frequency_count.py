# Программа для подсчёта частоты слов в тексте

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

# Убираем слова короче 2 символов
words = [word for word in words if len(word) > 2]


# Считаем частоту каждого слова
word_count = Counter(words)

# Фильтруем слова, которые встречаются больше одного раза, и сортируем их по убыванию
result_words = [(word, count) for word, count in word_count.most_common() if count > 1]



# Оставим топ самых частых слов
top_n = 10
top_words = result_words[:top_n]


# Вывод результата
for word, count in top_words:
    print(f"{word}: {count}")