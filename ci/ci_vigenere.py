line = '\n########## ########## ##########'

ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ZYX = "ZYXWVUTSRQPONMLKJIHGFEDCBA"

def vigenere(text, key, alph):
	result = []
	key_index = 0
	for char in text:
		if char in alph:
			char_index = alph.index(char)
			key_char = key[key_index % len(key)]
			key_shift = alph.index(key_char)
			new_index = (char_index - key_shift) % len(alph)	# Для шифрования, минус заменить на плюс
			result.append(alph[new_index])
			key_index += 1
		else:
			result.append(char)
			continue
	return ''.join(result)

def clear_key(key):
	res = []
	for ch in key:
		if ch in ABC:
			res.append(ch)
	return ''.join(res)


def main():
	while True:
		print('\n  ===== Шифр Виженера =====')
		while True:
			print(line)

			print('  1 - Обычный алфавит (ABC..),\n  2 - Перевёрнутый (ZYX..):')
			choice = ''
			s = ''
			while choice not in ('1', '2'):
				s += '>'
				choice = input(f'{s} ').strip()
			if choice == '1':
				alph = ABC
			else:
				alph = ZYX

			text = input("\n Введите шифр:\n> ").upper()
			key = input("\n Введите ключ:\n> ").upper()
			key = clear_key(key)

			print("\n\n Расшифрованный текст:")
			print(f"> {vigenere(text, key, alph)}")
			input()



if __name__ == "__main__":
    main()