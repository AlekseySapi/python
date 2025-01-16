# Шифр Атбаш

import pyperclip

line = "\n####### ####### ####### ####### #######"


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
        original_text = input("Введите текст:\n> ").strip()

        language = detect_language(original_text)
        if not language:
            print("Не удалось определить язык текста.")
            return
        

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
        
        encrypted_text = atbash(original_text, language, alphabet)

        print(f"\nШифр Атбаш:\n> {encrypted_text}")
        pyperclip.copy(encrypted_text)

        print("\n>> Текст скопирован в буфер обмена.\n")

        print(line)
        


if __name__ == "__main__":
    main()