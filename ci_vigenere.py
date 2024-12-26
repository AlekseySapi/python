# Шифр Виженера

import os

line = "\n##### ##### ##### ##### #####"


def vigenere_cipher(text, key):
    eng_alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    rus_alph = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    text = text.upper()  # Преобразуем весь текст в заглавные буквы
    key = key.upper()
    
    encrypted_text = []
    key_index = 0
    
    for char in text:
        if char in eng_alph:
            text_index = eng_alph.index(char)
            key_char = key[key_index % len(key)]  # Перебираем ключ
            key_index_char = eng_alph.index(key_char)
            encrypted_index = (text_index + key_index_char) % len(eng_alph)
            encrypted_text.append(eng_alph[encrypted_index])
            key_index += 1  # Переходим к следующему символу ключа
        elif char in rus_alph:
            text_index = rus_alph.index(char)
            key_char = key[key_index % len(key)]  # Перебираем ключ
            key_index_char = rus_alph.index(key_char)
            encrypted_index = (text_index + key_index_char) % len(rus_alph)
            encrypted_text.append(rus_alph[encrypted_index])
            key_index += 1  # Переходим к следующему символу ключа
        else:
            encrypted_text.append(char)  # Не изменяем символы, которые не в алфавите (например, пробелы)
    
    return ''.join(encrypted_text)


def vigenere_decipher(text, key):
    eng_alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    rus_alph = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    text = text.upper()
    key = key.upper()
    
    decrypted_text = []
    key_index = 0
    
    for char in text:
        if char in eng_alph:
            text_index = eng_alph.index(char)
            key_char = key[key_index % len(key)]
            key_index_char = eng_alph.index(key_char)
            decrypted_index = (text_index - key_index_char) % len(eng_alph)
            decrypted_text.append(eng_alph[decrypted_index])
            key_index += 1
        if char in rus_alph:
            text_index = rus_alph.index(char)
            key_char = key[key_index % len(key)]
            key_index_char = rus_alph.index(key_char)
            decrypted_index = (text_index - key_index_char) % len(rus_alph)
            decrypted_text.append(rus_alph[decrypted_index])
            key_index += 1
        else:
            decrypted_text.append(char)
    
    return ''.join(decrypted_text)



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

            ciphed_text = vigenere_cipher(text, key)

            with open(file_path, 'a', encoding='utf-8') as file:
                file.write("\n\n=== Зашифрованный текст ===\n")
                file.write(ciphed_text)

            print("Зашифровано.")

        elif choice == "2":

            unciphed_text = vigenere_decipher(text, key)

            with open(file_path, 'a', encoding='utf-8') as file:
                file.write("\n\n=== Расшифрованный текст ===\n")
                file.write(unciphed_text)

            print("Расшифровано.")



if __name__ == "__main__":
    main()