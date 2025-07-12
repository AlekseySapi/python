# Конвертация Кандзи, Хираганы и Катаканы в Ромадзи

line = '\n############### ############### ###############'

import re
from sudachipy import dictionary, Tokenizer
import sudachidict_full


# Инициализация анализатора
tokenizer_obj = dictionary.Dictionary(resource_dir=sudachidict_full.__path__[0]).create()
mode = Tokenizer.SplitMode.C

english_re = re.compile(r'^[A-Za-z0-9\s\.,\'"!?\-:;]+$')

def kanji_to_katakana(text: str) -> str:
    result_lines = []
    for line in text.splitlines():
        tokens = tokenizer_obj.tokenize(line, mode)
        result = []
        for token in tokens:
            surface = token.surface()
            # print(token.surface(), token.part_of_speech())
            if english_re.match(surface) or (token.part_of_speech()[0] in ['空白', '補助記号']):
                result.append(surface)
            else:
                reading = token.reading_form()
                result.append(reading if reading else surface)
        result_lines.append(' '.join(result))
    return '\n'.join(result_lines)


import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


import pykakasi

def katakana_to_romaji(text):
    kks = pykakasi.kakasi()
    # kks.setMode("J", "a")         # кандзи → латиница
    # kks.setMode("H", "a")         # хирагана → латиница
    kks.setMode("K", "a")         # катакана → латиница
    kks.setMode("r", "Hepburn")   # стиль: Хэпбёрн
    conv = kks.getConverter()

    # Замена японской пунктуации
    punct_map = {
        '。': '.',
        '、': ',',
        '！': '!',
        '？': '?',
        '「': ' "',
        '」': '" ',
        '『': ' "',
        '』': '" ',
        '・': '/',
        '〜': '~',
        '…': '...',
        '　': ' '      # японский пробел
    }

    result_lines = []

    for line in text.splitlines():
        result = conv.convert(line)
        romaji = ""

        for item in result:
            token = item['hepburn']
            orig = item['orig']

            if orig in punct_map:
                romaji = romaji.rstrip() + punct_map[orig]
            else:
                romaji += token
        result_lines.append(romaji.strip())

    return '\n'.join(result_lines)


def postprocess_romaji(text: str) -> str:
    # Таблица замен чисел
    digit_map = {
        r'\b0\b': 'zero',
        r'\b1\b': 'ichi',
        r'\b2\b': 'ni',
        r'\b3\b': 'san',
        r'\b4\b': 'yon',
        r'\b5\b': 'go',
        r'\b6\b': 'roku',
        r'\b7\b': 'nana',
        r'\b8\b': 'hachi',
        r'\b9\b': 'kyuu',
        r'\b10\b': 'juu',
    }
    '''
    r'\bna i\b': 'nai',
    r'\bshi ta\b': 'shita',
    r'\bshi te\b': 'shite',
    r'\bde shi ta\b': 'deshita',
    r'tsu ta\b': 'tta',
    r'\bta i\b': 'tai',
    r'\bma shi ta\b': 'mashita',
    r'\bma shi te\b': 'mashite',
    r'\bde su\b': 'desu',
    r'\bwa a\b': 'waa',
    r'\bo\b': 'wo',
    r'\boo\b': 'ou',
    r'oo\b': 'ou',
    '''

    # Базовые замены (разрывы и формы)
    pattern_map = {
        r'\bha\b': 'wa',
        r'ha\b': 'wa',
        r'\bwo\b': 'o',
        r'\bhe\b': 'e',
        r'tsu t': 'tt',
        r'\bswa\b': 'sha',

        r'\bVerse ichi\b': 'Verse 1',
        r'\bVerse ni\b': 'Verse 2',
        r'\brei\b': 'zero',
        r'\bhito tsu\b': 'hitotsu',
        r'\bfuta tsu\b': 'futatsu',
        r'\bwatakushi\b': 'watashi',
        r'\bboku ra\b': 'bokura',
        r'\bshu\b': 'tane',
        r'\bshibatataku\b': 'matataku',
        r'\bgomi\b': 'chiri',
        r'\bkai ri\b': 'mawari',
        r'\bmamori tai\b': 'mamoritai',
        r'\bkizutsui te\b': 'kizutsuite',
        r'\bwarae nai\b': 'waraenai',
        r'\bmise ta\b': 'miseta',
        r'\bie ta\b': 'ieta',
        r'\bsugi te\b': 'sugite',
        r'\bo sake\b': 'osake',
        r'\bmashi ta\b': 'mashita',
        r'\bsuki de\b': 'sukide',
        r'\byugama nai\b': 'yugamanai',
    }

    # Пробельные и пунктуационные чистки
    text = re.sub(r'" ', '"', text)
    text = re.sub(r'  +', ' ', text)
    text = re.sub(r'/ ', '-', text)
    text = re.sub(r'\s+([?!.,])', r'\1', text)

    # Применим числовые замены
    for pattern, repl in digit_map.items():
        text = re.sub(pattern, repl, text)

    # Применим паттерны склеек
    for pattern, repl in pattern_map.items():
        text = re.sub(pattern, repl, text)

    return text.strip()


def main():
    print('\n       === Конвертация в Ромадзи ===')
    while True:
        print(line)
        file_path = 'w.txt'
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        katakana_text = kanji_to_katakana(text)
        romaji_text = katakana_to_romaji(katakana_text)
        romaji_text = postprocess_romaji(romaji_text)

        with open(file_path, 'a', encoding='utf-8') as file:
            file.write("\n\n\n=== Ромадзи ===\n")
            file.write(romaji_text)

        print("\n\n  ✅ Конвертация в ромадзи завершена.\n")
        input()


if __name__ == "__main__":
	main()