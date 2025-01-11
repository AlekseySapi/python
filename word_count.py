# Программа для подсчёта частоты слов в тексте

import nltk # type: ignore
import string
from collections import Counter


# Мой список стоп-слов
'''
stop_words = [
    'и', 'в', 'во', 'не', 'что', 'он', 'на', 'я', 'с', 'со',
    'как', 'а', 'то', 'все', 'она', 'так', 'его', 'но', 'да',
    'ты', 'к', 'у', 'же', 'вы', 'за', 'бы', 'по', 'только',
    'ее', 'мне', 'было', 'вот', 'от', 'меня', 'еще', 'нет',
    'о', 'из', 'ему', 'теперь', 'когда', 'даже', 'ну', 'вдруг',
    'ли', 'если', 'уже', 'или', 'ни', 'быть', 'был', 'него',
    'до', 'вас', 'нибудь', 'опять', 'уж', 'вам', 'ведь', 'там',
    'потом', 'себя', 'ничего', 'ей', 'может', 'они', 'тут',
    'где', 'есть', 'надо', 'ней', 'для', 'мы', 'тебя', 'их',
    'чем', 'была', 'сам', 'чтоб', 'без', 'будто', 'чего',
    'раз', 'тоже', 'себе', 'под', 'будет', 'ж', 'тогда', 'кто',
    'этот', 'того', 'потому', 'этого', 'какой', 'совсем',
    'ним', 'здесь', 'этом', 'один', 'почти', 'мой', 'тем',
    'чтобы', 'нее', 'сейчас', 'были', 'куда', 'зачем', 'ужели',
    'разве', 'три', 'эти', 'много', 'эту', 'можно', 'при',
    'наш', 'конечно', 'всю', 'между', 'это',
    'the', 'and', 'to', 'he', 'of', 'was', 'in', 'his',
    'it', 'you', 'had', 'on', 'at', 'they', 'that', 'as',
    'him', 'but', 'with', 'for', 'all', 'be', 'out', 'up',
    'them', 'were', 'have', 'what', 'there', 'from',
    'this', 'if', 'into', 'she', 'their', 'not', 'been',
    'got', 'so', 'off', "didn't", 'could', 'get'
]
'''


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

def main():

    while True:
        # Запрашиваем путь к текстовому файлу
        file_path = input("\nВведите путь к текстовому файлу: ")

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
        except FileNotFoundError:
            print("Файл не найден. Проверьте путь и попробуйте снова.")
            continue
        except Exception as e:
            print(f"Произошла ошибка при чтении файла: {e}")
            return


        words = preprocess_text(text)

        # Убираем слова в 1 символ
        words = [word for word in words if len(word) > 1]


        # Считаем частоту каждого слова
        word_count = Counter(words)

        # Фильтрация стоп-слов и слов с частотой 1
        # И их сортировка
        result_words = [(word, count) for word, count in word_count.most_common() if count > 1 and word not in stop_words]



        # Оставим топ самых частых слов
        top_n = 10
        top_words = result_words[:top_n]


        # Вывод результата
        print(f"\n\n=== Топ {top_n} самых частых слов ===")
        i = 0
        for word, count in top_words:
            i += 1
            print(f"{i}) {word}: {count}")
        print("======= ======= ======= =======")


if __name__ == "__main__":
    # Загрузка стоп-слов
    nltk.download('stopwords')
    
    from nltk.corpus import stopwords # type: ignore

    # Получение стоп-слов для русского и английского языков
    stop_words_ru = set(stopwords.words('russian'))
    stop_words_en = set(stopwords.words('english'))

    # Объединение стоп-слов в один набор
    stop_words = stop_words_ru.union(stop_words_en)
    
    main()