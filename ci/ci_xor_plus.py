# Вариант шифрования через XOR с доп паролем

import os

line = "\n##### ##### ##### ##### #####"

# Сдвиги символов
ltr_shift = 220
arab_shift = 700
lines_shift = 9490
dots_shift = 10300
ch_shift = 15000

current_shift = ltr_shift


def xor(text, key):
    res = []
    for i, char in enumerate(text):
        char_code = ord(char)
        key_code = ord(key[i % len(key)]) + current_shift
        res.append(chr(char_code ^ key_code))
    return ''.join(res)

def xor_plus(text):
    key = 'roqKwLxuAsVfN7UFPiM6cz4I1SWajY0EDhbk8y93mtg2BCdlOGe5JQTnpZXRvH'
    res = []
    for i, char in enumerate(text):
        char_code = ord(char)
        key_code = ord(key[i % len(key)])
        res.append(chr(char_code ^ key_code))
    return ''.join(res)


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

            xored_text = xor_plus(xor(text, key))

            with open(file_path, 'a', encoding='utf-8') as file:
                file.write("\n\n=== Зашифрованный текст ===\n")
                file.write(xored_text)

            print("Зашифровано.")

        elif choice == "2":
            
            unxored_text = xor(xor_plus(text), key)

            with open(file_path, 'a', encoding='utf-8') as file:
                file.write("\n\n=== Расшифрованный текст ===\n")
                file.write(unxored_text)

            print("Расшифровано.")



if __name__ == "__main__":
    main()