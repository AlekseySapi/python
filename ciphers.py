import os


def detect_language(text):
    # Определение языка текста
    if any('а' <= char <= 'я' or 'А' <= char <= 'Я' for char in text):
        return 'ru'
    elif any('a' <= char <= 'z' or 'A' <= char <= 'Z' for char in text):
        return 'en'
    else:
        return None


# Шифр Цезаря
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


# Шифр Атбаш
def atbash(text, upper_alphabet, lower_alphabet):
    reverse_upper_alphabet = upper_alphabet[::-1]   # Переворачиваем алфавит
    reverse_lower_alphabet = lower_alphabet[::-1]
    
    # Маппинг букв алфавита на их противоположные
    translation = str.maketrans(upper_alphabet + lower_alphabet, reverse_upper_alphabet + reverse_lower_alphabet)
    
    return text.translate(translation)


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
        upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        lower_alphabet = upper_alphabet.lower()
    elif language == 'ru':
        upper_alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        lower_alphabet = upper_alphabet.lower()



    while True:
        choice1 = input("< Выберите шифр >\n1 - шифр Цезаря, 2 - шифр Атбаш: ")
        if choice1 == "1" or choice1 == "2":
            break
    

    if choice1 == "1":

        while True:
            choice2 = input("> 1 - Зашифровать, 2 - Расшифровать: ")
            if choice2 == "1" or choice2 == "2":
                break

        if choice2 == "1":
            while True:
                shift = input(">> Введите число сдвига: ").strip()
                if shift.lstrip('-').isdigit():
                    shift = int(shift)
                    break
        
        if choice2 == "2":
            while True:
                shift = input(">> Какой сдвиг был у шифра: ").strip()
                if shift.lstrip('-').isdigit():
                    shift = int(shift)
                    shift *= -1
                    break


        shift %= len(lower_alphabet)

        encrypted_text = caesar_cipher(original_text, shift, lower_alphabet, upper_alphabet)

        with open(file_path, 'a', encoding='utf-8') as file:
            file.write("\n\n=== === ===\n")
            file.write(encrypted_text)

        print("Результат добавлен в файл.")

    if choice1 == "2":

        encrypted_text = atbash(original_text, upper_alphabet, lower_alphabet)

        with open(file_path, 'a', encoding='utf-8') as file:
            file.write("\n\n=== === ===\n")
            file.write(encrypted_text)

        print("Результат добавлен в файл.")


if __name__ == "__main__":
    main()