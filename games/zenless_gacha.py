# Начну реализацию симулятора гачи Zenless Zone Zero

import random

line = '\n################# ################# #################'

def print_res(pools, choice):
	v = ['S', 'poop']
	if pools < 74:
		w = [12, 988]
		for _ in range(int(choice)):
			res = random.choices(v, weights=w, k=2)
			if res == 'S':
				return print("\n  Победа! Вы получили персонажа S-класса!")
			return print('\n  К сожалению, пока только "poop"...')
	else:
		w = [250, 750]
		if pools == 98:
			return print("\n  Победа! Вы получили персонажа S-класса!")
		for _ in range(int(choice)):
			res = random.choices(v, weights=w, k=2)
			if res == 'S':
				return print("\n  Победа! Вы получили персонажа S-класса!")
			return print('\n  К сожалению, пока только "poop"...')


def main():
	print('\n        === Симулятор гачи Zenless Zone Zero ===')
	pools = 90     # Всего круток в наличии
	while True:
		print(line)
		print(f"\n> Всего круток в наличии: {pools}")
		print("\nСколько крутим? (Введите 1 или 10)")
		choice = '0'
		s = ''
		while choice not in ('1', '10'):
			s += '>'
			choice = input(f'{s} ').strip()
			if pools - int(choice) < 0: choice = '0'	# Вариант обхода недостаточности круток (последняя десятка)
		pools -= int(choice)

		print_res(pools, choice)

		print(f"\n\nОсталось {pools} круток")

if __name__ == "__main__":
	main()