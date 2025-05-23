# Начну реализацию симулятора гачи Zenless Zone Zero

import random

line = '\n################# ################# #################'

def check_win(pools, choice):
	v = ['S', 'poop']
	if pools < 74:
		w = [12, 988]
		for _ in range(int(choice)):
			pools += 1
			if pools == 90:
				return True, pools
			res = random.choices(v, weights=w, k=1)
			if res[0] == 'S':
				return True, pools
		return False, pools
	else:
		w = [25, 75]
		for _ in range(int(choice)):
			pools += 1
			res = random.choices(v, weights=w, k=1)
			if res[0] == 'S':
				return True, pools
		return False, pools


def main():
	print('\n        === Симулятор гачи Zenless Zone Zero ===')
	user_pools = 90     # Всего круток в наличии
	pools = 0		# Откручено
	while True:
		print(line)
		print(f"\n> Всего круток в наличии: {user_pools}\n> Откручено: {pools}")
		print("\nСколько крутим? (Введите 1 или 10)")
		choice = '0'
		s = ''
		while choice not in ('1', '10'):
			s += '>'
			choice = input(f'{s} ').strip()
			if user_pools - int(choice) < 0: choice = '0'	# Вариант обхода недостаточности круток (последняя десятка)
		user_pools -= int(choice)

		win, pools = check_win(pools, choice)
		if win:
			print(f"\n  Победа! Вы получили персонажа S-класса! (на {pools} крутке)\n")
			break
		else:
			print(f'\n  К сожалению, пока только "poop"...\n\nОсталось {user_pools} круток')


if __name__ == "__main__":
	main()