line = '\n############ ############ ############ ############ ############'

ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ZYX = "ZYXWVUTSRQPONMLKJIHGFEDCBA"
ABC_RU = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
ZYX_RU = "ЯЮЭЬЫЪЩШЧЦХФУТСРПОНМЛКЙИЗЖЁЕДГВБА"


def vigenere(text, key, alph, choice_ci):
	result = []
	key_index = 0
	t = ""
	for char in text:
		if char in alph:
			char_index = alph.index(char)
			key_char = key[key_index % len(key)]
			key_shift = alph.index(key_char)
			if choice_ci == '1':
				new_index = (char_index - key_shift) % len(alph)	# Расшифровка
				t = "\n\n Расшифрованный текст:"
			else:
				new_index = (char_index + key_shift) % len(alph)	# Шифрование
				t = "\n\n Зашифрованный текст:"
			result.append(alph[new_index])
			key_index += 1
		else:
			result.append(char)
			continue
	print(t)
	print(f"> {''.join(result)}")

def clear_key(key, alph):
	res = []
	for ch in key:
		if ch in alph:
			res.append(ch)
	return ''.join(res)


def main():
	while True:
		print('\n      ===== Шифр Виженера =====')
		while True:
			print(line)

			print('  1 - Расшифровать,\n  2 - Зашифровать:')
			choice_ci = ''
			s = ''
			while choice_ci not in ('1', '2'):
				s += '>'
				choice_ci = input(f'{s} ').strip()

			print('\n  1 - Обычный EN алфавит (ABC..),  2 - Перевёрнутый (ZYX..):')
			print('  3 - Обычный RU алфавит (АБВ..),  4 - Перевёрнутый (ЯЮЭ..):')
			choice_alph = ''
			s = ''
			while choice_alph not in ('1', '2', '3', '4'):
				s += '>'
				choice_alph = input(f'{s} ').strip()
			if choice_alph == '1':
				alph = ABC
			elif choice_alph == '2':
				alph = ZYX
			elif choice_alph == '3':
				alph = ABC_RU
			else:
				alph = ZYX_RU

			if choice_ci == '1':
				text = input("\n Введите шифр:\n> ").upper()
			else:
				text = input("\n Введите текст:\n> ").upper()
			
			key = ""
			while key == "":
				key = input("\n Введите ключ:\n> ").upper()
				key = clear_key(key, alph)
				print(f" [key = {key}]")

			vigenere(text, key, alph, choice_ci)
			input()



if __name__ == "__main__":
    main()