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
    shift *= -1
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

    print("##### ##### ##### #####")
    while True:
        while True:
            word = input("# Зашифрованное слово [len: 3 - 20]:\n> ")
            if len(word) > 2 and len(word) < 21:
                break
        

        language = detect_language(word)
        if not language:
            print("Не удалось определить язык текста.")
            return

        if language == 'en':
            upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            lower_alphabet = upper_alphabet.lower()
        elif language == 'ru':
            upper_alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
            lower_alphabet = upper_alphabet.lower()



        print("\n=== === === === ===\n# Перевод раскладки")
        translated_word = translate_layout(word, language)
        print("> " + translated_word + "\n")

        print("# Шифр Атбаш")
        atbashed_word = atbash(word, upper_alphabet, lower_alphabet)
        print("> " + atbashed_word + "\n")

        print("# Шифр Цезаря")
        for i in range(len(upper_alphabet)-1):
            caesared_word = caesar_cipher(word, i+1, lower_alphabet, upper_alphabet)
            print(f"  {caesared_word} < {i+1}")

        print("\n##### ##### ##### #####")


if __name__ == "__main__":
    main()