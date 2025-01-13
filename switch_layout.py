# Перевод раскладки (en -> ru / ru -> en)

import pyperclip


line = "\n####### ####### ####### ####### #######"


# Маппинг (английская и русская раскладки)
en = '`qwertyuiop[]asdfghjkl;\'zxcvbnm,./~@#$%^&QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?'
ru = 'ёйцукенгшщзхъфывапролджэячсмитьбю.Ё"№;%:?ЙЦУКЕНГШЩЗХЪ/ФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,'

# Создание маппинга с помощью str.maketrans
en_to_ru = str.maketrans(en, ru)
ru_to_en = str.maketrans(ru, en)

# Перевод текста между раскладками
def translate_layout(text, current_layout):
    if current_layout == 'en':
        return text.translate(en_to_ru)
    elif current_layout == 'ru':
        return text.translate(ru_to_en)


def detect_language(text):
    # Определение языка текста
    if any('а' <= char <= 'я' or 'А' <= char <= 'Я' for char in text):
        return 'ru'
    elif any('a' <= char <= 'z' or 'A' <= char <= 'Z' for char in text):
        return 'en'
    else:
        return None
    


def main():
    print("\n[Перевод раскладки (en -> ru / ru -> en)]\n")
    print(line)
    while True:
        text = input("# Введите текст для перевода:\n> ")

        language = detect_language(text)
        if not language:
            print("Не удалось определить язык текста.")
            return            

        translated_text = translate_layout(text, language)

        print(f'\nРаскладка изменена:\n> {translated_text}')
        pyperclip.copy(translated_text)

        print("\n>> Текст скопирован в буфер обмена.")

        print(line)
        


if __name__ == "__main__":
    main()