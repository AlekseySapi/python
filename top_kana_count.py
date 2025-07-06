# Счётчик всех символов японской каны в тексте (суммарно Хирагана и Катакана) и составление топа по их частоте

from collections import Counter
import pandas as pd
import unidic
import fugashi
import os

line = '\n################# ################# #################'


# Создаём таггер
dicdir = os.path.normpath(unidic.DICDIR)
tagger = fugashi.Tagger(f'-d "{dicdir}"')

def get_reading(word):
    # features - это список из разных полей словаря Unidic
    features = word.feature
    # Чтение (読み) в 9-м элементе (индекс 9)
    try:
        reading = features[9]
        if reading == '*':
            return None
        return reading
    except Exception:
        return None

def kanji_to_katakana(text: str) -> str:
    result = []
    for line in text.splitlines(keepends=True):
        line_result = []
        for word in tagger(line):
            reading = get_reading(word)
            # print(f'{word.surface} -> {reading}')  # Отладка
            if reading:
                line_result.append(reading)
            else:
                line_result.append(word.surface)
        result.append(''.join(line_result))
    return '\n'.join(result)


def get_char_frequency(text):
    text = text.replace('\n', '')   # удаляем все переводы строк
    counts = Counter(text)
    total = sum(counts.values())
    df = pd.DataFrame(
        counts.items(),
        columns=['Символ', 'Кол-во']
    )
    df['Частота (%)'] = (df['Кол-во'] / total * 100).round(2)
    df = df.sort_values(by='Кол-во', ascending=False).reset_index(drop=True)
    df.index += 1
    pd.set_option('display.max_rows', None)  # показать все строки без сокращений
    return df


def main():
    print('\n    === Топ символов японской каны по частоте ===')
    while True:
        print(line)
        file_path = 'w.txt'
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        katakana_text = kanji_to_katakana(text)


        ''' Просмотр полей словаря

        for word in tagger('今日は雨です'):
            print(f'Слово: {word.surface}')
            for i, f in enumerate(word.feature):
                print(f'  {i}: {f}')
            print('---')

        '''

        with open(file_path, 'a', encoding='utf-8') as file:
            file.write("\n\n\n=== Катакана ===\n")
            file.write(katakana_text)
            file.write("\n\n\n===== Топ символов этого текста =====\n\n")
            file.write(str(get_char_frequency(katakana_text)))

        print("\n\n\n  ✅ Топ символов составлен и записан в файл.\n")
        input()


if __name__ == "__main__":
	main()