# Шифр Виженера v3
# Словарь - весь Unicode

# import os
import pyperclip

line = "\n##### ##### ##### ##### #####"
max_len = 200000

def vigenere_cipher(text, key, mode):
    result = []
    key_index = 0
    for char in text:
        if char == '\n':
            result.append(char)
            continue
        char_index = ord(char)
        key_char = key[key_index % len(key)]
        key_shift = ord(key_char)
        if mode == "encrypt":
            new_index = (char_index + key_shift) % max_len
        else:
            new_index = (char_index - key_shift) % max_len
        result.append(chr(new_index))
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