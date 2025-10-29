line = '\n############ ############ ############ ############ ############'

ABC = "#ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ZYX = "#ZYXWVUTSRQPONMLKJIHGFEDCBA"
ABC_RU = "#АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
ZYX_RU = "#ЯЮЭЬЫЪЩШЧЦХФУТСРПОНМЛКЙИЗЖЁЕДГВБА"
nums = "0123456789"
symb = " ,.!?:'\""


def a1z26(text, alph, choice_ci):
	text = text.upper()
	res = []
	if choice_ci == '1':
		i = 0
		while(i < len(text)):
			if (i+1) < len(text):
				if (text[i] in nums) and (text[i+1] in nums):
					n = int(text[i])*10 + int(text[i+1])
					if 1 <= n <= 26:
						res.append(alph[n])
						i = i + 1	# Попробовать записи шифра в виде двухразрядных чисел (без разделителей) -> 220126070922
					else:
						res.append(alph[0])
						i = i + 1
				elif text[i] in nums:
					res.append(alph[int(text[i])])
				elif text[i] in symb:
					res.append(text[i])
				elif text[i] == '-':
					i = i + 1
					continue
				else: res.append(alph[0])
			else:
				if text[i] in nums:
					res.append(alph[int(text[i])])
				elif text[i] in symb:
					res.append(text[i])
				elif text[i] == '-':
					i = i + 1
					continue
				else: res.append(alph[0])
			i = i + 1
		t = "\n\n Расшифрованный текст:"
	else:
		for char in text:
			if char in alph:
				res.append(str(alph.index(char)).zfill(2))
			else:
				res.append(char)
		t = "\n\n Зашифрованный текст:"
	print(t)
	print(f"> {''.join(res)}")


def main():
	while True:
		print('\n                 ===== Шифр A1Z26 =====')
		print('\n   (можно указывать как в виде "1-5-26", так и "010526")')
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
				text = input("\n Введите цифровой шифр:\n> ")
			else:
				text = input("\n Введите текст:\n> ")

			a1z26(text, alph, choice_ci)
			input()



if __name__ == "__main__":
    main()