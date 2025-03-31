import pyperclip

line = '\n################# ################# #################'

def translate(text):
	rus = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
	eng = 'ABVGDEËŽZIJKLMNOPRSTUFHCČWŜƂYƄƎÜÄabvgdeëžzijklmnoprstufhcčwŝƃyƅƏüä'
	
	rus_to_eng = str.maketrans(rus, eng)
	eng_to_rus = str.maketrans(eng, rus)
	
	res = []
	for char in text:
		if char in rus:
			res.append(char.translate(rus_to_eng))
		elif char in eng:
			res.append(char.translate(eng_to_rus))
		else:
			res.append(char)
	return "".join(res)

def main():
    print('\n        === Транслит ===')
    print('\nВведите текст для перевода между RU - EN')
    while True:
        text = input('\n> ')
        result = translate(text)


        print(f'\n\n> {result}')

        pyperclip.copy(result)

        print("\n ✅ Текст скопирован\n")
        print(line)

if __name__ == "__main__":
    main()