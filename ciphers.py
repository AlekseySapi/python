import os


def detect_language(text):
    # Определение языка текста
    if any('а' <= char <= 'я' or 'А' <= char <= 'Я' for char in text):
        return 'ru'
    elif any('a' <= char <= 'z' or 'A' <= char <= 'Z' for char in text):
        return 'en'
    else:
        return None
    

# Словарь соответствий раскладок
key_mapping_en = {
    'q': 'й', 'w': 'ц', 'e': 'у', 'r': 'к', 't': 'е', 'y': 'н', 'u': 'г', 'i': 'ш', 'o': 'щ', 'p': 'з', '[': 'х', ']': 'ъ',
    'a': 'ф', 's': 'ы', 'd': 'в', 'f': 'а', 'g': 'п', 'h': 'р', 'j': 'о', 'k': 'л', 'l': 'д', ';': 'ж', '\'': 'э',
    'z': 'я', 'x': 'ч', 'c': 'с', 'v': 'м', 'b': 'и', 'n': 'т', 'm': 'ь', ',': 'б', '.': 'ю', '/': '.', '`': 'ё',
    'Q': 'Й', 'W': 'Ц', 'E': 'У', 'R': 'К', 'T': 'Е', 'Y': 'Н', 'U': 'Г', 'I': 'Ш', 'O': 'Щ', 'P': 'З', '{': 'Х', '}': 'Ъ',
    'A': 'Ф', 'S': 'Ы', 'D': 'В', 'F': 'А', 'G': 'П', 'H': 'Р', 'J': 'О', 'K': 'Л', 'L': 'Д', ':': 'Ж', '"': 'Э',
    'Z': 'Я', 'X': 'Ч', 'C': 'С', 'V': 'М', 'B': 'И', 'N': 'Т', 'M': 'Ь', '<': 'Б', '>': 'Ю', '?': ',', '~': 'Ё',
    '#': '№', '$': ';', '^': ':', '&': '?', '@': '"', '|': '/'
}
key_mapping_ru = {
    'й': 'q', 'ц': 'w', 'у': 'e', 'к': 'r', 'е': 't', 'н': 'y', 'г': 'u', 'ш': 'i', 'щ': 'o', 'з': 'p', 'х': '[', 'ъ': ']',
    'ф': 'a', 'ы': 's', 'в': 'd', 'а': 'f', 'п': 'g', 'р': 'h', 'о': 'j', 'л': 'k', 'д': 'l', 'ж': ';', 'э': '\'',
    'я': 'z', 'ч': 'x', 'с': 'c', 'м': 'v', 'и': 'b', 'т': 'n', 'ь': 'm', 'б': ',', 'ю': '.', '.': '/', 'ё': '`',
    'Й': 'Q', 'Ц': 'W', 'У': 'E', 'К': 'R', 'Е': 'T', 'Н': 'Y', 'Г': 'U', 'Ш': 'I', 'Щ': 'O', 'З': 'P', 'Х': '{', 'Ъ': '}',
    'Ф': 'A', 'Ы': 'S', 'В': 'D', 'А': 'F', 'П': 'G', 'Р': 'H', 'О': 'J', 'Л': 'K', 'Д': 'L', 'Ж': ':', 'Э': '"',
    'Я': 'Z', 'Ч': 'X', 'С': 'C', 'М': 'V', 'И': 'B', 'Т': 'N', 'Ь': 'M', 'Б': '<', 'Ю': '>', ',': '?', 'Ё': '~',
    '№': '#', ';': '$', ':': '^', '?': '&', '"': '@', '/': '|'
}

# Перевод текста между раскладками
def translate_layout(text: str, current_layout: str) -> str:
    if current_layout not in {'ru', 'en'}:
        raise ValueError("Некорректная раскладка.")
    
    if current_layout == 'en':
        return ''.join(key_mapping_en.get(char, char) for char in text)
    elif current_layout == 'ru':
        return ''.join(key_mapping_ru.get(char, char) for char in text)


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
        choice1 = input("< Выберите шифр >\n0 - Перевод раскладки, 1 - шифр Цезаря, 2 - шифр Атбаш: ")
        if choice1 == "0" or choice1 == "1" or choice1 == "2":
            break
    

    if choice1 == "0":

        translated_text = translate_layout(original_text, language)

        with open(file_path, 'a', encoding='utf-8') as file:
            file.write("\n\n=== === ===\n")
            file.write(translated_text)

        print("Результат добавлен в файл.")


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