# Шифр Виженера

# import os
import pyperclip

line = "\n##### ##### ##### ##### #####"

eng_alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
eng_alph_lower = "abcdefghijklmnopqrstuvwxyz"
rus_alph = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
rus_alph_lower = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
symb = ' !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~№'
#	     !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~№
num = '0123456789'


def vigenere_cipher(text, key, mode):
    result = []
    key_index = 0
    for char in text:
        if char in eng_alph:
            alphabet = eng_alph
        elif char in eng_alph_lower:
            alphabet = eng_alph_lower
        elif char in rus_alph:
            alphabet = rus_alph
        elif char in rus_alph_lower:
            alphabet = rus_alph_lower
        elif char in symb:
            alphabet = symb
        elif char in num:
            alphabet = num
        else:
            result.append(char)
            continue
        char_index = alphabet.index(char)
        key_char = key[key_index % len(key)]
        if key_char in eng_alph:
            key_alphabet = eng_alph
        elif key_char in eng_alph_lower:
            key_alphabet = eng_alph_lower
        elif key_char in rus_alph:
            key_alphabet = rus_alph
        elif key_char in rus_alph_lower:
            key_alphabet = rus_alph_lower
        elif key_char in symb:
            key_alphabet = symb
        elif key_char in num:
            key_alphabet = num
        key_shift = key_alphabet.index(key_char)
        if mode == "encrypt":
            new_index = (char_index + key_shift) % len(alphabet)
        else:
            new_index = (char_index - key_shift) % len(alphabet)
        result.append(alphabet[new_index])
        key_index += 1
    return ''.join(result)


def main():
    while True:
        print(line)
        text = input("# Введите текст:\n> ")
        '''
        file_path = input("# Введите путь к файлу:\n> ").strip()
        if not os.path.exists(file_path):
            print("Файл не найден.")
        else:
            break

    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        '''

        while True:
            choice = input("\n  1 - Зашифровать, 2 - Расшифровать:\n> ")
            if choice == "1" or choice == "2":
                key = input("\npass = ")
                break

        if choice == "1":
            ciphed_text = vigenere_cipher(text, key, 'encrypt')
            print(f"\nШифр Виженера:\n> {ciphed_text}")
            
            pyperclip.copy(ciphed_text)
            print("\n>> Текст скопирован в буфер обмена.\n")
            
            '''
            with open(file_path, 'a', encoding='utf-8') as file:
                file.write("\n\n\n=== Зашифрованный текст ===\n")
                file.write(ciphed_text)

            print("\nЗашифровано.\n")
            '''

        elif choice == "2":
            unciphed_text = vigenere_cipher(text, key, 'decrypt')
            print(f"\nШифр Виженера:\n> {unciphed_text}")
            
            pyperclip.copy(unciphed_text)
            print("\n>> Текст скопирован в буфер обмена.\n")
            
            '''
            with open(file_path, 'a', encoding='utf-8') as file:
                file.write("\n\n\n=== Расшифрованный текст ===\n")
                file.write(unciphed_text)

            print("\nРасшифровано.\n")
            '''


if __name__ == "__main__":
    main()