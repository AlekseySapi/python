# Шифр Виженера

import os

line = "\n##### ##### ##### ##### #####"

eng_alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
rus_alph = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"



# TODO -> Доработать, пока неверно шифрует


def vigenere_cipher(text, key, mode):
    result = []
    key_index = 0

    for char in text:
        if 'А' <= char <= 'Я' or char in 'Ё':
            alphabet = rus_alph
        if 'а' <= char <= 'я' or char in 'ё':
            alphabet = rus_alph.lower()
        elif 'A' <= char <= 'Z':
            alphabet = eng_alph
        elif 'a' <= char <= 'z':
            alphabet = eng_alph.lower()
        else:
            result.append(char)  # Если не буква, добавляем без изменений
            continue

        char_index = alphabet.index(char)
        key_char = key[key_index % len(key)]
        if 'А' <= key_char <= 'Я' or key_char in 'Ё':
            key_alphabet = rus_alph
        if 'а' <= key_char <= 'я' or key_char in 'ё':
            key_alphabet = rus_alph.lower()
        elif 'A' <= key_char <= 'Z':
            key_alphabet = eng_alph
        elif 'a' <= key_char <= 'z':
            key_alphabet = eng_alph.lower()
        key_shift = key_alphabet.index(key_char)  # Сдвиг по букве ключа

        # Шифрование или дешифровка
        if mode == "encrypt":
            new_index = (char_index + key_shift) % len(alphabet)
        else:  # Дешифровка
            new_index = (char_index - key_shift) % len(alphabet)

        result.append(alphabet[new_index])
        key_index += 1  # Переход к следующему символу ключа

    return ''.join(result)



def main():
    print(line)
    while True:
        file_path = input("# Введите путь к файлу:\n> ").strip()
        if not os.path.exists(file_path):
            print("Файл не найден.")
        else:
            break

    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()


    while True:
        print(line)
        while True:
            choice = input("  1 - Зашифровать, 2 - Расшифровать:\n> ")
            if choice == "1" or choice == "2":
                key = input("pass = ")
                break


        if choice == "1":

            ciphed_text = vigenere_cipher(text, key, 'encrypt')

            with open(file_path, 'a', encoding='utf-8') as file:
                file.write("\n\n=== Зашифрованный текст ===\n")
                file.write(ciphed_text)

            print("Зашифровано.")

        elif choice == "2":

            unciphed_text = vigenere_cipher(text, key, 'decrypt')

            with open(file_path, 'a', encoding='utf-8') as file:
                file.write("\n\n=== Расшифрованный текст ===\n")
                file.write(unciphed_text)

            print("Расшифровано.")



if __name__ == "__main__":
    main()