import pyperclip

line = '\n################# ################# #################'

def text_shuffle(text):
	chars = []
	temp = []
	i = 1
	for char in text:
		if i % 2 == 0:
			temp.append(char)
		else:
			chars.append(char)
		i += 1
	for char in temp:
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