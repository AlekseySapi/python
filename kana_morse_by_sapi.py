# Morse Code Translator for Japanese Kana (Hiragana + Katakana) – my version
#   The most frequent symbols are assigned the shortest codes
#
# Переводчик кода Морзе для японской Каны (Хирагана + Катакана) - моя версия
#   Самым частотным символам присвоены наиболее короткие коды
#
#
# > AlekseySapi
# > altmind92@gmail.com
# > https://github.com/AlekseySapi
# > https://t.me/sapi_group


line = '\n################# ################# #################'


def hiragana_to_katakana(text):
    table = str.maketrans({
        'あ': 'ア', 'い': 'イ', 'う': 'ウ', 'え': 'エ', 'お': 'オ',
        'か': 'カ', 'き': 'キ', 'く': 'ク', 'け': 'ケ', 'こ': 'コ',
        'さ': 'サ', 'し': 'シ', 'す': 'ス', 'せ': 'セ', 'そ': 'ソ',
        'た': 'タ', 'ち': 'チ', 'つ': 'ツ', 'て': 'テ', 'と': 'ト',
        'な': 'ナ', 'に': 'ニ', 'ぬ': 'ヌ', 'ね': 'ネ', 'の': 'ノ',
        'は': 'ハ', 'ひ': 'ヒ', 'ふ': 'フ', 'へ': 'ヘ', 'ほ': 'ホ',
        'ま': 'マ', 'み': 'ミ', 'む': 'ム', 'め': 'メ', 'も': 'モ',
        'や': 'ヤ', 'ゆ': 'ユ', 'よ': 'ヨ',
        'ら': 'ラ', 'り': 'リ', 'る': 'ル', 'れ': 'レ', 'ろ': 'ロ',
        'わ': 'ワ', 'を': 'ヲ', 'ん': 'ン',
        'が': 'ガ', 'ぎ': 'ギ', 'ぐ': 'グ', 'げ': 'ゲ', 'ご': 'ゴ',
        'ざ': 'ザ', 'じ': 'ジ', 'ず': 'ズ', 'ぜ': 'ゼ', 'ぞ': 'ゾ',
        'だ': 'ダ', 'ぢ': 'ヂ', 'づ': 'ヅ', 'で': 'デ', 'ど': 'ド',
        'ば': 'バ', 'び': 'ビ', 'ぶ': 'ブ', 'べ': 'ベ', 'ぼ': 'ボ',
        'ぱ': 'パ', 'ぴ': 'ピ', 'ぷ': 'プ', 'ぺ': 'ペ', 'ぽ': 'ポ',
        'ぁ': 'ァ', 'ぃ': 'ィ', 'ぅ': 'ゥ', 'ぇ': 'ェ', 'ぉ': 'ォ',
        'ゃ': 'ャ', 'ゅ': 'ュ', 'ょ': 'ョ', 'っ': 'ッ',
        'ゎ': 'ヮ',
        'ゐ': 'ヰ', 'ゑ': 'ヱ',
        'ゔ': 'ヴ',
        'ゕ': 'ヵ', 'ゖ': 'ヶ'
    })
    return text.translate(table)


kana_morse = {
    'ン': '.',   # N
    'イ': '-',   # I
    'ノ': '..',  # NO
    'ト': '.-',  # TO
    'ニ': '-.',  # NI
    'デ': '--',  # DE
    'テ': '...', # TE
    'カ': '..-', # KA
    'ス': '.-.', # SU
    'ウ': '-..', # U
    'オ': '.--', # O
    'シ': '-.-', # SHI
    'ア': '--.', # A
    'タ': '---', # TA

    'コ': '....',   # KO
    'エ': '...-',   # E
    'ラ': '..-.',   # RA
    'ハ': '.-..',   # HA
    'リ': '-...',   # RI
    'ク': '..--',   # KU

    'ッ': '.-.-',   # Сокуон (っ)

    'ガ': '.--.',   # GA
    'ル': '-..-',   # RU
    'キ': '-.-.',   # KI
    'ミ': '--..',   # MI
    'セ': '.---',   # SE
    'ヤ': '-.--',   # YA
    'メ': '--.-',   # ME
    'ム': '---.',   # MU
    'モ': '----',   # MO

    'マ': '..-.-',  # MA
    'ケ': '..--.',  # KE
    'フ': '.-..-',  # FU
    'ネ': '.-.-.',  # NE
    'レ': '.--..',  # RE
    'ヘ': '-...-',  # HE
    'ソ': '-..-.',  # SO
    'ヨ': '-.-..',  # YO
    'ワ': '.-.--',  # WA
    'ヒ': '.--.-',  # HI
    'ホ': '.---.',  # HO
    'サ': '-..--',  # SA

    'ナ': '-.-.-',  # NA
    'ユ': '-.--.',  # YU
    'チ': '-.---',  # CHI
    'ツ': '--..-',  # TSU
    'ロ': '--.-.',  # RO
    'ヌ': '--.--',  # NU
    'ヲ': '---.-',  # WO


    'ジ': '......', # JI
    'ド': '.....-', # DO
    'バ': '.-....', # BA
    'ブ': '-.....', # BU
    'ボ': '....--', # BO
    'ザ': '...-.-', # ZA
    'ビ': '...--.', # BI
    'ダ': '..-..-', # DA
    'ズ': '..-.-.', # ZU
    'ベ': '..--..', # BE
    'ピ': '.-...-', # PI

    'プ': '.-..-.', # PU
    'グ': '.-.-..', # GU
    'ゴ': '.--...', # GO
    'ギ': '-....-', # GI
    'パ': '-...-.', # PA
    'ポ': '-..-..', # PO
    'ゲ': '-.-...', # GE
    'ペ': '--....', # PE
    'ゼ': '...---', # ZE
    'ゾ': '..-.--', # ZO
    'ヂ': '..---.', # DJI
    'ヅ': '.-..--', # DZU


    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',


    '。': '...-.',  # точка
    '、': '..-..',  # запятая
    'ー': '.-...',  # чоон
    '・': '.-.-.-', # интерпункт
    '〜': '.-.--.', # волнистая черта
    '（': '.--..-', # открывающая круглая скобка
    '）': '.--.-.', # закрывающая круглая скобка
    '？': '.---..', # вопросительный
    '！': '-...--', # восклицательный
    '「': '-..-.-', # открывающая кавычка
    '」': '-..--.', # закрывающая кавычка
    '『': '-.-..-', # открывающая угловая кавычка
    '』': '-.-.-.', # закрывающая угловая кавычка
    '※': '-.--..', # знак сноски
    '…': '--...-',  # многоточие
    '〒': '--..-.', # знак почты
    '〆': '--.-..', # знак сокращения


    'ャ': '....-.', # YA-small
    'ュ': '...-..', # YU-small
    'ョ': '..-...', # YO-small

    'ヴ': '---...', # VU

    'ァ': '..----', # a-small
    'ィ': '.-.---', # i-small
    'ゥ': '.--.--', # u-small
    'ェ': '.---.-', # e-small
    'ォ': '.----.', # o-small
    'ヮ': '-..---', # wa-small
    'ヰ': '-.-.--', # wi
    'ヱ': '-.--.-', # we
    'ヵ': '-.---.', # ka-small
    'ヶ': '--..--'  # ke-small
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
    text = hiragana_to_katakana(text)
    morse_words = []
    words = text.strip().upper().split()
    for word in words:
        morse_letters = []
        for char in word:
            if char in morse_dict:
                morse_letters.append(morse_dict[char])
            else:
                morse_letters.append('')
        morse_words.append(' '.join(morse_letters))
    return ' / '.join(morse_words)


def morse_to_text(morse_code, morse_dict):
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
                decoded_letters.append('?')
        decoded_words.append(''.join(decoded_letters))
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
    print('\n            === Kana Morse Translate ===')
    while True:
        print(line)
        print("\n\n< Choose mode >\n  1 - Morse to Kana; 3 - Morse to bin;\n  2 - Kana to Morse; 4 - bin to Morse:")
        s = '>'
        while True:
            n = input(f"{s} ")
            if n in ['1', '2', '3', '4']:
                ch = n
                break
            else:
                s += '>'
        
        if ch in ['1', '3', '4']:
            v = "code"
        else:
            v = "kana-text"
        print(f"\nInput {v}:")
        text = input("  ")
        if ch == '2':
            result = text_to_morse(text, kana_morse)
            result += '\n\n\nIn binary form:\n  ' + morse_to_bin(result)
        elif ch == '3':
            result = morse_to_bin(text)
        elif ch == '4':
            result = bin_to_morse(text)
        else:
            result = morse_to_text(text, kana_morse)

        print("\n\nResult:")
        print("  " + result)

        print()
        input()


if __name__ == "__main__":
	main()