# Симулятор гачи Zenless Zone Zero для версии 1.7

import random

line = '\n################# ################# #################'
characters = ['Hugo Vlad', 'Nekomata', 'Koleda', 'Grace', 'Rina', 'Lycaon', 'Soldier 11']
chances = [52, 8, 8, 8, 8, 8, 8]
v = ['S', 'poop']

def check_win(pools, choice, character):
	for _ in range(int(choice)):
		if 0 <= pools < 29:
			w = [10, 990]
		elif 29 <= pools < 74:
			w = [7, 993]
		else:
			w = [25, 75]
		res = random.choices(v, weights=w, k=1)[0]
		if res == 'S' or pools == 90:
			character = random.choices(characters, weights=chances, k=1)[0]
			return True, pools, character
		pools += 1
	return False, pools, character


def main():
	print('\n        === Симулятор гачи Zenless Zone Zero ===')
	user_pools = 90     # Всего круток в наличии
	pools = 0		# Откручено
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
			if user_pools - int(choice) < 0: choice = '0'	# Вариант обхода недостаточности круток (последняя десятка)
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