# Шифр ROT13

import os

line = "\n####### ####### ####### ####### #######\n# [Шифр ROT13 (сдвиг на 13)]\n#"


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
            print("Буквы латинского алфавита не найдены.")
            return

        if language == 'en':
            alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            

        while True:
            choice2 = input("  1 - Зашифровать / Расшифровать:\n> ")
            if choice2 == "1":
                break


        encrypted_text = ROT13(original_text, alphabet)

        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(f"\n\n===== Шифр ROT13 =====\n")
            file.write(encrypted_text)

        print("Результат добавлен в файл.")
        print(line)
        


if __name__ == "__main__":
    main()