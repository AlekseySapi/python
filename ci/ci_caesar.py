# Шифр Цезаря

import os

line = "\n####### ####### ####### ####### #######\n# [Шифр Цезаря (классический сдвиг: 3)]\n#"


def caesar_cipher(text, shift, language, alphabet):
    if language != 'hebr' or language != 'phnx' or language != 'arab' or language != 'rune':
        lower_alphabet = alphabet.lower()
        result = []
        for char in text:
            if char in lower_alphabet:
                idx = lower_alphabet.index(char)
                new_idx = idx + shift
                result.append(lower_alphabet[new_idx % len(lower_alphabet)])
            elif char in alphabet:
                idx = alphabet.index(char)
                new_idx = idx + shift
                result.append(alphabet[new_idx % len(alphabet)])
            else:
                result.append(char)  # Пропуск символов, не входящих в алфавит
    else:
        result = []
        for char in text:
            if char in alphabet:
                idx = alphabet.index(char)
                new_idx = idx + shift
                result.append(alphabet[new_idx % len(alphabet)])
            else:
                result.append(char)  # Пропуск символов, не входящих в алфавит
    return ''.join(result)


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
        choice2 = input("  1 - Зашифровать, 2 - Расшифровать:\n> ")
        if choice2 == "1" or choice2 == "2":
            break

    while True:

        if choice2 == "1":
            while True:
                shift = input(">> На сколько нужно сдвинуть? ").strip()
                if shift.lstrip('-').isdigit():
                    shift = int(shift)
                    break
        
        if choice2 == "2":
            while True:
                shift = input(">> Какой сдвиг был у шифра? ").strip()
                if shift.lstrip('-').isdigit():
                    shift = int(shift)
                    shift *= -1
                    break


        shift %= len(alphabet)

        encrypted_text = caesar_cipher(original_text, shift, language, alphabet)

        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(f"\n\n===== Сдвиг на {shift} =====\n")
            file.write(encrypted_text)

        print("Результат добавлен в файл.")
        print(line)
        


if __name__ == "__main__":
    main()