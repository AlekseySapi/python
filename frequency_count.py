# Программа для подсчёта частоты слов в тексте

# Напиши программу, которая принимает строку текста и подсчитывает,
#  сколько раз каждое слово встречается в этом тексте.
# Программа должна выводить слова и количество их повторений.

# Программа должна игнорировать регистр букв (например, «Привет» и «привет» — это одно и то же слово).
# Программа должна учитывать только слова, то есть игнорировать знаки пунктуации.
# Вывод должен быть отсортирован по частоте слов (от самых частых к менее частым)

import string


text = "Привет! Как твои дела? Привет, привет. Всё хорошо, спасибо!"
print(text)


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
def count_word_freq(words):
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency


def sort_frequencies(frequency):
    # Преобразуем словарь в список кортежей (слово, частота)
    freq_items = list(frequency.items())
    
    # Сортировка
    for i in range(len(freq_items)):
        max_index = i
        for j in range(i + 1, len(freq_items)):
            if freq_items[j][1] > freq_items[max_index][1]:
                max_index = j
        # Меняем местами
        freq_items[i], freq_items[max_index] = freq_items[max_index], freq_items[i]
    
    return freq_items


frequency = count_word_freq(words)
sorted_frequency = sort_frequencies(frequency)
    
# Вывод результата
for word, count in sorted_frequency:
    print(f"{word}: {count}")
