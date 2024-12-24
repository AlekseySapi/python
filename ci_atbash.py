# Шифр Атбаш

import os

line = "\n####### ####### ####### ####### #######\n# [Шифр Атбаш]\n#"


def atbash(text, language, alphabet):
    if language == 'hebr' or language == 'phnx' or language == 'arab' or language == 'rune':
        # Переворачиваем алфавит
        reverse_alphabet = alphabet[::-1]

        # Маппинг букв алфавита на их противоположные
        translation = str.maketrans(alphabet, reverse_alphabet)
    else:
        lower_alphabet = alphabet.lower()

        # Переворачиваем алфавит
        reverse_alphabet = alphabet[::-1]
        reverse_lower_alphabet = lower_alphabet[::-1]
    
        # Маппинг букв алфавита на их противоположные
        translation = str.maketrans(alphabet + lower_alphabet, reverse_alphabet + reverse_lower_alphabet)
    
    return text.translate(translation)


def detect_language(text):
    # Определение языка текста
    if any('а' <= char <= 'я' or 'А' <= char <= 'Я' for char in text):
        return 'ru'
    elif any('a' <= char <= 'z' or 'A' <= char <= 'Z' for char in text):
        return 'en'
    elif any('α' <= char <= 'ω' or 'Α' <= char <= 'Ω' for char in text):
        return 'greek'
    elif any('א' <= char <= 'ת' for char in text):
        return 'hebr'
    elif any('𐤀' <= char <= '𐤕' for char in text):
        return 'phnx'
    elif any('ᚠ' <= char <= 'ᛞ' for char in text):
        return 'rune'
    elif any('أ' <= char <= 'غ' for char in text):
        return 'arab'
    else:
        return None
    


def main():
    print(line)
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
    elif language == 'greek':
        alphabet = 'ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ'
    elif language == 'hebr':
        alphabet = 'אבגדהוזחטיכלמנסעפצקרשת'
    elif language == 'phnx':
        alphabet = '𐤀𐤁𐤂𐤃𐤄𐤅𐤆𐤇𐤈𐤉𐤊𐤋𐤌𐤍𐤎𐤏𐤐𐤑𐤒𐤓𐤔𐤕'
    elif language == 'arab':
        alphabet = 'أبجدﻩوزحطيكلمنسعفصقرشتثخذضظغ'
    elif language == 'rune':
        alphabet = 'ᚠᚢᚦᚨᚱᚲᚷᚹᚺᚾᛁᛃᛈᛇᛉᛊᛏᛒᛖᛗᛚᛜᛟᛞ'
        

    
    while True:

        while True:
            choice = input("  1 - Зашифровать, 2 - Расшифровать:\n> ")
            if choice == "1" or choice == "2":
                break
        
        encrypted_text = atbash(original_text, language, alphabet)

        with open(file_path, 'a', encoding='utf-8') as file:
            file.write("\n\n=== === ===\n")
            file.write(encrypted_text)

        print("Результат добавлен в файл.")
        print(line)
        


if __name__ == "__main__":
    main()