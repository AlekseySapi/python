# Переводчик кода Морзе

line = '\n################# ################# #################'

'''
Радиожаргоны:

GM, GA, GE, GN (от good morning, good afternoon, good evening, good night), ЗДР — приветствие;
CQ (вероятно, от seek you) — общий вызов;
DE (далее позывной) — это такой-то (от такого-то);
GB (от good bye), ДСВ — до свидания;
K (от key — ключ, работать ключом) — передавайте, перехожу на приём;
PSE (от please) — пожалуйста;
QRZ? — кто меня вызывает?;
QRS — передавайте медленнее;
QRQ — передавайте быстрее;
R (от roger that) — вас понял;
TKS, TNX (от thanks), СПБ, БЛГ — спасибо;
73 — наилучшие пожелания

'''

morse_en = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',     'F': '..-.',
    'G': '--.',   'H': '....',  'I': '..',    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',   'P': '.--.',  'Q': '--.-',  'R': '.-.',
    'S': '...',   'T': '-',     'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-',  ',': '--..--', '?': '..--..', "'": '.----.',
    '!': '-.-.--',  '/': '-..-.',  '(': '-.--.',  ')': '-.--.-',
    '&': '.-...',   ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.',   '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.'
}

morse_ru = {
    'А': '.-',    'Б': '-...',  'В': '.--',   'Г': '--.',   'Д': '-..',   'Ё': '.',
    'Е': '.',     'Ж': '...-',  'З': '--..',  'И': '..',    'Й': '.---',  'К': '-.-',
    'Л': '.-..',  'М': '--',    'Н': '-.',    'О': '---',   'П': '.--.',  'Р': '.-.',
    'С': '...',   'Т': '-',     'У': '..-',   'Ф': '..-.',  'Х': '....',  'Ц': '-.-.',
    'Ч': '---.',  'Ш': '----',  'Щ': '--.-',  'Ъ': '--.--', 'Ы': '-.--',  'Ь': '-..-',
    'Э': '..-..', 'Ю': '..--',  'Я': '.-.-',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-',  ',': '--..--', '?': '..--..', "'": '.----.',
    '!': '-.-.--',  '/': '-..-.',  '(': '-.--.',  ')': '-.--.-',
    '&': '.-...',   ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.',   '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.'
}


def text_to_morse(text, morse_dict):
    # Результат для всех слов
    morse_words = []
    
    # Разбиваем по словам по пробелам в тексте
    words = text.strip().upper().split()
    
    for word in words:
        morse_letters = []
        for char in word:
            if char in morse_dict:
                morse_letters.append(morse_dict[char])
            else:
                morse_letters.append('')  # если символа нет в словаре - пропускаем
        # Соединяем буквы одним пробелом
        morse_words.append(' '.join(morse_letters))
    
    # Соединяем слова тремя пробелами
    return '   '.join(morse_words)


def morse_to_text(morse_code, morse_dict):
    # Создаем обратный словарь: код Морзе -> символ
    reverse_morse = {v: k for k, v in morse_dict.items()}
    
    # Сплит по 3 пробелам — делим на слова
    words = morse_code.strip().split('   ')
    decoded_words = []
    
    for word in words:
        # Сплит по одному пробелу — делим на буквы
        letters = word.strip().split(' ')
        decoded_letters = []
        for letter_code in letters:
            if letter_code in reverse_morse:
                decoded_letters.append(reverse_morse[letter_code])
            else:
                decoded_letters.append('?')  # неизвестный код
        decoded_words.append(''.join(decoded_letters))
    
    # Собираем слова через пробел
    return ' '.join(decoded_words)


def main():
    print('\n               === Morse Translate ===')
    while True:
        print(line)
        print("\n\n< Выберите режим >\n  1 - Morse to en; 2 - Morse to ru;\n  3 - en to Morse; 4 - ru to Morse:")
        s = '>'
        while True:
            n = input(f"{s} ")
            if n in ['1', '2', '3', '4']:
                ch = n
                break
        if ch in ['2', '4']:
            current_dict = morse_ru
        else:
            current_dict = morse_en
        
        print("\nВведите код/текст:")
        text = input("  ")
        if ch in ['3', '4']:
            result = text_to_morse(text, current_dict)
        else:
            text = text.replace('/', ' ')
            result = morse_to_text(text, current_dict)

        print("\nРезультат:")
        print("  " + result)

        print()
        input()


if __name__ == "__main__":
	main()