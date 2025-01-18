import pyperclip

line = "\n######### ######### #########"
current_shift = ord('æ')

def xor(text, n, key):
    res = []
    for i, char in enumerate(text):
        char_code = ord(char)
        key_code = n + ord(key[i % len(key)]) + current_shift
        res.append(chr(char_code ^ key_code))
    return ''.join(res)

def get_alphabet(text):
    unique_chars = {}
    for char in text:
       unique_chars[char] = None
    sorted_chars = sorted(unique_chars.keys(), reverse=True)
    return "".join(sorted_chars)

def replace_words(text, mapping):
    for key, value in mapping.items():
        text = text.replace(key, value)
    return text

def caesar_cipher(text, shift, alphabet):
    result = []
    for char in text:
        if char in alphabet:
            idx = alphabet.index(char)
            new_idx = idx + shift
            result.append(alphabet[new_idx % len(alphabet)])
        else:
            result.append(char)
    return ''.join(result)

def atbash(text, alphabet):
    reverse_alphabet = alphabet[::-1]
    translation = str.maketrans(alphabet, reverse_alphabet)
    return text.translate(translation)

def detect_lang(char):
    if 'а' <= char <= 'я' or 'А' <= char <= 'Я' or char in 'Ёё':
        return 'ru'
    elif 'a' <= char <= 'z' or 'A' <= char <= 'Z':
        return 'en'
    else:
        return None

def translate_layout(text, shift):
	en = 'ixDZKEHnMyJzTvlqNfjemhgcrSVwICXBbYFQUPOautGdApkLRWso'
	ru = 'дДЦКьокСПАзутгШапЬЫщрЩЙТОЛНЕфлйУВчснвемИЧЯРяГМшыцФЗи'
	en_sh = caesar_cipher(en, shift, en)
	shift_n = shift * (-1)
	ru_sh = caesar_cipher(ru, shift_n, ru)
	en_to_ru = str.maketrans(en_sh, ru_sh)
	ru_to_en = str.maketrans(ru_sh, en_sh)
	res = []
	for char in text:
		if detect_lang(char) == 'en':
			res.append(char.translate(en_to_ru))
		elif detect_lang(char) == 'ru':
			res.append(char.translate(ru_to_en))
		else:
			res.append(char)
	return "".join(res)

def reverse_text(text, choice):
    res = text[::-1]
    res = reverse_halves_in_text(res, choice)
    return res

def reverse_halves_in_text(text, choice):
    def reverse_halves(s):
        n = len(s)
        mid = n // 2
        if n % 2 == 0:
            left_half = s[:mid]
            right_half = s[mid:]
            return right_half + left_half
        else:
            left_half = s[:mid]
            middle = s[mid]
            right_half = s[mid+1:]
            return right_half + middle + left_half
    lines = text.splitlines()
    result_lines = [reverse_halves(line) for line in lines]
    return "\n".join(result_lines)


def main():
    while True:
        print(line)
        original_text = ''
        while original_text == '':
            original_text = input("# Введите текст:\n\n")

        while True:
            choice = input("\n  1 - Зашифровать, 2 - Расшифровать:\n> ")
            if choice == "1" or choice == "2":
                text = original_text
                key = input("pass = ")
                if key == '': key = ' '
                key_num = 0
                c = 1
                for char in key:
                    plus = ord(char) * c + ord(char) % (c * 10)
                    key_num += plus
                    c += 1
                n = (ord(key[0]) % 9) + 1
                if ord(key[0]) % 2 != 0:
                    n *= -1
                shift = (key_num + n) % (len(key) * n)

                break


        if choice == "1":
            translated_text = translate_layout(text, shift)
            xored_text = xor(translated_text, n, key)
            alphabet = get_alphabet(xored_text)
            ciphed_text = caesar_cipher(xored_text, shift, alphabet)
            res_text = reverse_text(ciphed_text, choice)

            print(f"\n\n=== Зашифрованный текст ===\n\n{res_text}")
            pyperclip.copy(res_text)
            print("\n\n>> Текст скопирован в буфер обмена.\n")

        elif choice == "2":
            alphabet = get_alphabet(text)
            unciphed_text = caesar_cipher(text, shift*(-1), alphabet)
            unreversed_text = reverse_text(unciphed_text, choice)
            unxored_text = xor(unreversed_text, n, key)
            res_text = translate_layout(unxored_text, shift)

            print(f"\n\n=== Расшифрованный текст ===\n\n{res_text}")
            pyperclip.copy(res_text)
            print("\n\n>> Текст скопирован в буфер обмена.\n")


if __name__ == "__main__":
    main()