# Перевод раскладки (en -> ru / ru -> en)

import os

line = "\n####### ####### ####### ####### #######\n# [Перевод раскладки (en -> ru / ru -> en)]\n#"


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
    print(line)
    
    while True:
        while True:
            file_path = input("# Введите путь к файлу:\n> ").strip()
            if not os.path.exists(file_path):
                print("Файл не найден.")
            else:
                break

        with open(file_path, 'r', encoding='utf-8') as file:
            original_text = file.read()

        language = detect_language(original_text)
        if not language:
            print("Не удалось определить язык текста.")
            return
        
        print(f"Язык определён как -> [{language}]")

        if language == 'ru':
            alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        elif language == 'en':
            alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            

        while True:
            choice = input("  t / y / 1 - Перевести раскладку:\n> ")
            if choice == "t" or choice == "y" or choice == "1":
                break
        
        translated_text = translate_layout(original_text, language)

        with open(file_path, 'a', encoding='utf-8') as file:
            file.write("\n\n===== Раскладка переведена =====\n")
            file.write(translated_text)

        print("Результат добавлен в файл.")
        print(line)
        


if __name__ == "__main__":
    main()