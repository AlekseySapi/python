import os


line = "\n##### ##### ##### ##### #####"
line2 = "\n=== === === === ==="


def detect_language(text):
    # Определение языка текста
    if any('а' <= char <= 'я' or 'А' <= char <= 'Я' for char in text):
        return 'ru'
    elif any('a' <= char <= 'z' or 'A' <= char <= 'Z' for char in text):
        return 'en'
    else:
        return None
    

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


# Шифр Цезаря
def caesar_cipher(text, shift, alphabet):
    lower_alphabet = alphabet.lower()
    result = []
    shift *= -1
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
    return ''.join(result)


# Шифр Атбаш
def atbash(text, alphabet):
    lower_alphabet = alphabet.lower()

    # Переворачиваем алфавит
    reverse_alphabet = alphabet[::-1]
    reverse_lower_alphabet = lower_alphabet[::-1]
    
    # Маппинг букв алфавита на их противоположные
    translation = str.maketrans(alphabet + lower_alphabet, reverse_alphabet + reverse_lower_alphabet)
    
    return text.translate(translation)


# Переворот слова
def reverse_word(word):
    res = word[::-1]
    return res


def main():

    print(line)
    while True:
        while True:
            word = input("# Зашифрованное слово / фраза [len: 3 - 30]:\n> ")
            if word == "q" or word == "Q":
                exit()
            elif len(word) > 2 and len(word) < 31:
                break
        

        language = detect_language(word)
        if not language:
            print("Не удалось определить язык текста.")
            return

        if language == 'en':
            alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        elif language == 'ru':
            alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'



        print(line2)
        print("## Смена раскладки")
        translated_word = translate_layout(word, language)
        print("  " + translated_word + "\n")

        print("## Переворот слова")
        reversed_word = reverse_word(word)
        print("  " + reversed_word + "\n")

        print("## Шифр Атбаш")
        atbashed_word = atbash(word, alphabet)
        print("  " + atbashed_word + "\n")

        print("## Шифр Цезаря")
        for i in range(len(alphabet)-1):
            caesared_word = caesar_cipher(word, i+1, alphabet)
            print(f"  {caesared_word} < {i+1}")

        print(line)


if __name__ == "__main__":
    main()