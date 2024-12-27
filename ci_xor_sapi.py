import os
import random

line = "\n##### ##### ##### ##### #####"

# Сдвиги символов
shift = 220
arab_shift = 700
lines_shift = 9490
dots_shift = 10300
ch_shift = 15000
symb_shift = 40950


def xor(text, key):
    res = []
    for i, char in enumerate(text):
        char_code = ord(char)
        key_code = ord(key[i % len(key)]) + symb_shift
        res.append(chr(char_code ^ key_code))
    return ''.join(res)


def add_spaces(text):
    length = len(text)
    
    # Пропорции
    num_spaces = max(1, length // 8)  # Пробелы: примерно 1 на каждые 8 символов
    num_newlines = max(1, length // 50)  # Переносы строк: примерно 1 на каждые 50 символов

    # Преобразуем текст в список для вставки символов
    text_list = list(text)

    # Вставляем пробелы
    for _ in range(num_spaces):
        position = random.randint(0, len(text_list))
        text_list.insert(position, ' ')

    # Вставляем переносы строк
    for _ in range(num_newlines):
        position = random.randint(0, len(text_list))
        text_list.insert(position, '\n')

    return ''.join(text_list)


def remove_spaces(text):
    return text.replace(" ", "").replace("\n", "")


# Переворот текста
def reverse_text(text):
    res = text[::-1]
    res = reverse_halves_in_text(res)
    return res

def reverse_halves_in_text(text):
    def reverse_halves(s):
        n = len(s)  # Длина строки
        mid = n // 2  # Середина строки

        if n % 2 == 0:
            left_half = s[:mid]
            right_half = s[mid:]
            return right_half + left_half
        else:
            left_half = s[:mid]
            middle = s[mid]
            right_half = s[mid+1:]
            return right_half + middle + left_half

    lines = text.splitlines()  # Разделяем текст на строки
    result_lines = [reverse_halves(line) for line in lines]  # Обрабатываем каждую строку
    return "\n".join(result_lines)



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

            xored_text = xor(text, key)
            reversed_text = reverse_text(xored_text)

            with open(file_path, 'a', encoding='utf-8') as file:
                file.write("\n\n=== Зашифрованный текст ===\n")
                file.write(add_spaces(reversed_text))

            print("Зашифровано.")

        elif choice == "2":

            text = remove_spaces(text)
            unreversed_text = reverse_text(text)
            unxored_text = xor(unreversed_text, key)

            with open(file_path, 'a', encoding='utf-8') as file:
                file.write("\n\n=== Расшифрованный текст ===\n")
                file.write(unxored_text)

            print("Расшифровано.")



if __name__ == "__main__":
    main()