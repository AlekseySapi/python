# Начну реализацию симулятора гачи Zenless Zone Zero

line = '\n################# ################# #################'


def main():
	print('\n        === Симулятор гачи Zenless Zone Zero ===')
	pools = 100     # Всего круток в наличии
	while True:
		print(line)
		print(f"\n> Всего круток в наличии: {pools}")
		print("\nСколько крутим? (Введите 1 или 10)")
		choice = '0'
		s = ''
		while choice not in ('1', '10'):
			s += '>'
			choice = input(f'{s} ').strip()
		pools -= int(choice)
		print(f"\nОсталось {pools} круток")

if __name__ == "__main__":
	main()