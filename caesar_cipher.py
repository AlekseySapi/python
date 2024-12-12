import os
import string


def detect_language(text):
    # Определение языка текста
    if any('а' <= char <= 'я' or 'А' <= char <= 'Я' for char in text):
        return 'ru'
    elif any('a' <= char <= 'z' or 'A' <= char <= 'Z' for char in text):
        return 'en'
    else:
        return None


def caesar_cipher(text, shift, lower_alphabet, upper_alphabet):
    result = []
    for char in text:
        if char in lower_alphabet:
            idx = lower_alphabet.index(char)
            new_idx = idx + shift
            result.append(lower_alphabet[new_idx % len(lower_alphabet)])
        elif char in upper_alphabet:
            idx = upper_alphabet.index(char)
            new_idx = idx + shift
            result.append(upper_alphabet[new_idx % len(upper_alphabet)])
        else:
            result.append(char)  # Пропуск символов, не входящих в алфавит
    return ''.join(result)


def main():
    while True:
        file_path = input("Введите путь к файлу: ").strip()
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

    if language == 'en':
        lower_alphabet = string.ascii_lowercase
        upper_alphabet = string.ascii_uppercase
    elif language == 'ru':
        lower_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        upper_alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

    while True:
        shift = input(f"> Введите число сдвига: ").strip()
        if shift.lstrip('-').isdigit():
            shift = int(shift)
            break

    shift %= len(lower_alphabet)

    encrypted_text = caesar_cipher(original_text, shift, lower_alphabet, upper_alphabet)

    with open(file_path, 'a', encoding='utf-8') as file:
        file.write("\n=== === ===\n")
        file.write(encrypted_text)

    print("Результат добавлен в файл.")


if __name__ == "__main__":
    main()