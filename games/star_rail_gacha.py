# Симулятор гачи  Honkai: Star Rail  для версии 3.3

import random

line = '\n################# ################# #################'
characters = ['Гиацина', 'Байлу', 'Броня', 'Клара', 'Гепард', 'Химеко', 'Вельт', 'Яньцин']
chances = [51, 7, 7, 7, 7, 7, 7, 7]
v = ['S', 'poop']

def check_win(pools, choice, character):
	for _ in range(int(choice)):
		pools += 1
		if 0 < pools < 75:
			w = [6, 994]
		else:
			w = [20, 80]
		res = random.choices(v, weights=w, k=1)[0]
		if res == 'S' or pools == 90:
			character = random.choices(characters, weights=chances, k=1)[0]
			return True, pools, character
	return False, pools, character


def main():
	print('\n        === Симулятор гачи Star Rail ===')
	user_pools = 90     # Всего круток в наличии
	pools = 0			# Откручено
	character = ''
	while True:
		print(line)
		print(f"\n> Всего круток в наличии: {user_pools}\n> Откручено: {pools}")
		print("\nСколько крутим? (Введите 1 или 10)")
		choice = '0'
		s = ''
		while choice not in ('1', '10'):
			s += '>'
			choice = input(f'{s} ').strip()
			if choice.isdigit():
				if pools + int(choice) > 90: choice = '0'	# Вариант обхода недостаточности круток (последняя десятка)
		user_pools -= int(choice)

		win, pools, character = check_win(pools, choice, character)
		if win:
			print(f"\n  Поздравляем!!! Вы получили персонажа  << {character} >>    (на {pools} крутке)\n")
			input()
			break
		else:
			print(f'\n  К сожалению, пока только "poop"...\n\nОсталось {user_pools} круток')


if __name__ == "__main__":
	main()