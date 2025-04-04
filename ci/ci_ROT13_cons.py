# Шифр ROT13

import pyperclip

line = "\n####### ####### ####### ####### #######\n# [Шифр ROT13 (сдвиг на 13)]\n (только для ENG алфавита)\n"


def ROT13(text, alphabet):
    shift = 13
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
    return ''.join(result)


def detect_language(text):
    # Определение языка текста
    if any('a' <= char <= 'z' or 'A' <= char <= 'Z' for char in text):
        return 'en'
    else:
        return None
    


def main():
    print(line)
    while True:
        original_text = input("Введите текст:\n> ").strip()

        language = detect_language(original_text)
        if not language:
            print("Буквы латинского алфавита не найдены.")
            return
        

        if language == 'en':
            alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


        encrypted_text = ROT13(original_text, alphabet)

        print(f"\nШифр ROT13:\n> {encrypted_text}")
        pyperclip.copy(encrypted_text)

        print("\n>> Текст скопирован в буфер обмена.\n")

        print(line)
        


if __name__ == "__main__":
    main()