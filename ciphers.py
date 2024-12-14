import os


def detect_language(text):
    # Определение языка текста
    if any('а' <= char <= 'я' or 'А' <= char <= 'Я' for char in text):
        return 'ru'
    elif any('a' <= char <= 'z' or 'A' <= char <= 'Z' for char in text):
        return 'en'
    elif any('α' <= char <= 'ω' or 'Α' <= char <= 'Ω' for char in text):
        return 'greek'
    elif any('א' <= char <= 'ת' for char in text):
        return 'hebr'
    elif any('𐤀' <= char <= '𐤕' for char in text):
        return 'phnx'
    elif any('أ' <= char <= 'غ' for char in text):
        return 'arab'
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
def translate_layout(text, current_layout):    
    if current_layout == 'en':
        return ''.join(key_mapping_en.get(char, char) for char in text)
    elif current_layout == 'ru':
        return ''.join(key_mapping_ru.get(char, char) for char in text)


# Шифр Цезаря
def caesar_cipher(text, shift, language, alphabet):
    if language != 'hebr' or language != 'phnx' or language != 'arab':
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
    else:
        result = []
        for char in text:
            if char in alphabet:
                idx = alphabet.index(char)
                new_idx = idx + shift
                result.append(alphabet[new_idx % len(alphabet)])
            else:
                result.append(char)  # Пропуск символов, не входящих в алфавит
    return ''.join(result)


# Шифр Атбаш
def atbash(text, language, alphabet):
    if language == 'hebr' or language == 'phnx' or language == 'arab':
        # Переворачиваем алфавит
        reverse_alphabet = alphabet[::-1]

        # Маппинг букв алфавита на их противоположные
        translation = str.maketrans(alphabet, reverse_alphabet)
    else:
        lower_alphabet = alphabet.lower()

        # Переворачиваем алфавит
        reverse_alphabet = alphabet[::-1]
        reverse_lower_alphabet = lower_alphabet[::-1]
    
        # Маппинг букв алфавита на их противоположные
        translation = str.maketrans(alphabet + lower_alphabet, reverse_alphabet + reverse_lower_alphabet)
    
    return text.translate(translation)


def main():
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
        print("Не удалось определить язык текста.")
        return
    
    print(f"Язык определён как -> [{language}]")

    if language == 'ru':
        alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    elif language == 'en':
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    elif language == 'greek':
        alphabet = 'ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ'
    elif language == 'hebr':
        alphabet = 'אבגדהוזחטיכלמנסעפצקרשת'
    elif language == 'phnx':
        alphabet = '𐤀𐤁𐤂𐤃𐤄𐤅𐤆𐤇𐤈𐤉𐤊𐤋𐤌𐤍𐤎𐤏𐤐𐤑𐤒𐤓𐤔𐤕'
    elif language == 'arab':
        alphabet = 'أبجدﻩوزحطيكلمنسعفصقرشتثخذضظغ'
        


    while True:

        if language in {'ru', 'en'}:

            while True:
                choice1 = input("# Выберите шифр\n 0 - Перевод раскладки, 1 - шифр Цезаря, 2 - шифр Атбаш (Q/q - выход): ")
                if choice1 == "q" or choice1 == "Q":
                    exit()
                elif choice1 == "0" or choice1 == "1" or choice1 == "2":
                    break

        else:

            while True:
                choice1 = input("# Выберите шифр\n 1 - шифр Цезаря, 2 - шифр Атбаш (Q/q - выход): ")
                if choice1 == "q" or choice1 == "Q":
                    exit()
                elif choice1 == "1" or choice1 == "2":
                    break
        

        if choice1 == "0":

            translated_text = translate_layout(original_text, language)

            with open(file_path, 'a', encoding='utf-8') as file:
                file.write("\n\n=== === ===\n")
                file.write(translated_text)

            print("Результат добавлен в файл.\n")


        if choice1 == "1":

            while True:
                choice2 = input("> 1 - Зашифровать, 2 - Расшифровать: ")
                if choice2 == "1" or choice2 == "2":
                    break

            if choice2 == "1":
                while True:
                    shift = input(">> Насколько нужно сдвинуть? ").strip()
                    if shift.lstrip('-').isdigit():
                        shift = int(shift)
                        break
            
            if choice2 == "2":
                while True:
                    shift = input(">> Какой сдвиг был у шифра? ").strip()
                    if shift.lstrip('-').isdigit():
                        shift = int(shift)
                        shift *= -1
                        break


            shift %= len(alphabet)

            encrypted_text = caesar_cipher(original_text, shift, language, alphabet)

            with open(file_path, 'a', encoding='utf-8') as file:
                file.write("\n\n=== === ===\n")
                file.write(encrypted_text)

            print("Результат добавлен в файл.\n")


        if choice1 == "2":

            encrypted_text = atbash(original_text, language, alphabet)

            with open(file_path, 'a', encoding='utf-8') as file:
                file.write("\n\n=== === ===\n")
                file.write(encrypted_text)

            print("Результат добавлен в файл.\n")


if __name__ == "__main__":
    main()