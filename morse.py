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
    'А': '.-',    'Б': '-...',  'В': '.--',   'Г': '--.',   'Д': '-..',
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


def clean_morse(morse_code):
    table = str.maketrans({
        '*': '.',
        '°': '.',
        '·': '.',   # U+00B7 (точка по центру)
        '•': '.',	# U+2022 (жирная точка)
        '●': '.',   # (U+25CF) - чёрный кружок
        '⬤': '.',   # (U+2B24) - чёрный большой кружок
        '◦': '.',   # U+25E6 (белый кружок)
        '0': '.',
        'o': '.',
        'O': '.',
        'e': '.',

        '_': '-',    # нижнее подчёркивание
        '–': '-',    # U+2013 (длинное тире)
        '—': '-',    # U+2014 (em dash)
        '−': '-',    # U+2212 (минус)
        '=': '-',

        '/': ' ',	# слэш
        '\\': ' ',	# обратный слэш
        '|': ' '
    })
    return morse_code.translate(table)


def text_to_morse(text, morse_dict):
    # Результат для всех слов
    morse_words = []
    
    # Разбиваем по словам по пробелам в тексте
    words = text.strip().upper().replace('Ё', 'Е').split()
    
    for word in words:
        morse_letters = []
        for char in word:
            if char in morse_dict:
                morse_letters.append(morse_dict[char])
            else:
                morse_letters.append('')  # если символа нет в словаре - пропускаем
        # Соединяем буквы одним пробелом
        morse_words.append(' '.join(morse_letters))
    return ' / '.join(morse_words)


def morse_to_text(morse_code, morse_dict):
    # Создаем обратный словарь: код Морзе -> символ
    reverse_morse = {v: k for k, v in morse_dict.items()}
    
    morse_code = clean_morse(morse_code)
    
    words = morse_code.strip().split('   ')
    decoded_words = []
    
    for word in words:
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
    
    
def morse_to_bin(morse_code):
    morse_code = clean_morse(morse_code)
    table = str.maketrans({
        '.': '10',
        '-': '1110',
        ' ': '00'
    })
    return morse_code.translate(table)[:-1]
	
	
def bin_to_morse(bin_code):
	bin_code += '0'
	morse_code = bin_code.replace('1110', '-').replace('10', '.').replace('000000', ' / ').replace('00', ' ').replace('0', '')
	return morse_code
	

def main():
    print('\n               === Morse Translate ===')
    while True:
        print(line)
        print("\n\n< Выберите режим >\n  1 - Morse to en; 3 - Morse to ru; 5 - Morse to bin;\n  2 - en to Morse; 4 - ru to Morse; 6 - bin to Morse:")
        s = '>'
        while True:
            n = input(f"{s} ")
            if n in ['1', '2', '3', '4', '5', '6']:
                ch = n
                break
        if ch in ['3', '4']:
            current_dict = morse_ru
        else:
            current_dict = morse_en
        
        if ch in ['1', '3', '5', '6']:
            v = "код"
        else:
            v = "текст"
        print(f"\nВведите {v}:")
        text = input("  ")
        if ch in ['2', '4']:
            result = text_to_morse(text, current_dict)
            result += '\n\n\nВ бинарном виде:\n  ' + morse_to_bin(result)
        elif ch == '5':
            result = morse_to_bin(text)
        elif ch == '6':
            result = bin_to_morse(text)
        else:
            result = morse_to_text(text, current_dict)

        print("\n\nРезультат:")
        print("  " + result)

        print()
        input()


if __name__ == "__main__":
	main()