line = '\n########### ########### ########### ########### ###########'

ABC = "#ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ZYX = "#ZYXWVUTSRQPONMLKJIHGFEDCBA"
nums = "0123456789"
symb = " ,.!?:'\""


def main():
	while True:
		print('\n             ===== Шифр A1Z26 =====')
		print('\n(можно указывать как в виде "1-5-26", так и "010526")')
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

			text = input("\n Введите цифровой шифр:\n> ")
			res = []
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


			unci_str = ''.join(res)

			print("\n\n Расшифрованный текст:")
			print(f"> {unci_str}")
			input()



if __name__ == "__main__":
    main()