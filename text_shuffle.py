import pyperclip

line = '\n################# ################# #################'

def text_shuffle(text):
	chars = []
	temp1 = []
	temp2 = []
	i = 2
	for char in text:
		if i % 2 == 0:
			temp1.append(char)
		elif i % 3 == 0:
			temp2.append(char)
		else:
			chars.append(char)
		i += 1
	for char in temp1:
		chars.append(char)
	for char in temp2:
		chars.append(char)
	return ''.join(chars)

def main():
	print('\n        === Перемешивание текста ===')
	print('\nВведите текст')
	while True:
		text = input('\n> ')
		result = text_shuffle(text)


		print(f'\n\n> {result}')

		pyperclip.copy(result)

		print("\n ✅ Текст скопирован\n")
		print(line)

if __name__ == "__main__":
	main()