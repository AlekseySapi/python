# Начну реализацию симулятора гачи Zenless Zone Zero

import random

line = '\n################# ################# #################'

def print_res(user_pools, pools, choice):
	v = ['S', 'poop']
	if pools < 74:
		w = [12, 988]
		for _ in range(int(choice)):
			res = random.choices(v, weights=w, k=2)
			if res == 'S':
				return print("\n  Победа! Вы получили персонажа S-класса!\n")
			return print(f'\n  К сожалению, пока только "poop"...\n\nОсталось {user_pools} круток')
	else:
		w = [25, 75]
		for _ in range(int(choice)):
			res = random.choices(v, weights=w, k=2)
			if res == 'S':
				return print("\n  Победа! Вы получили персонажа S-класса!\n")
			return print(f'\n  К сожалению, пока только "poop"...\n\nОсталось {user_pools} круток')


def main():
	print('\n        === Симулятор гачи Zenless Zone Zero ===')
	user_pools = 90     # Всего круток в наличии
	pools = 0		# Откручено
	while True:
		print(line)
		print(f"\n> Всего круток в наличии: {user_pools}")
		print("\nСколько крутим? (Введите 1 или 10)")
		choice = '0'
		s = ''
		while choice not in ('1', '10'):
			s += '>'
			choice = input(f'{s} ').strip()
			if user_pools - int(choice) < 0: choice = '0'	# Вариант обхода недостаточности круток (последняя десятка)
		user_pools -= int(choice)
		pools += int(choice)
		if pools == 90:
			print("\n  Победа! Вы получили персонажа S-класса!")
			print(f"")
			break
		else:
			print_res(user_pools, pools, choice)
			print(f"")


if __name__ == "__main__":
	main()