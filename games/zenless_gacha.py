# Симулятор гачи Zenless Zone Zero для версии 1.7

import random

line = '\n################# ################# #################'

def check_win(pools, choice, character):
	v = ['S', 'poop']
	if pools < 74:
		w = [12, 988]
		for _ in range(int(choice)):
			pools += 1
			if pools == 90:
				return True, pools
			res = random.choices(v, weights=w, k=1)
			if res[0] == 'S':
				char_choice = ['Hugo', 'Nekomata', 'Koleda', 'Grace', 'Rina', 'Lycaon', 'Soldier 11']
				chances = [52, 8, 8, 8, 8, 8, 8]
				character = random.choices(char_choice, weights=chances, k=1)[0]
				return True, pools, character
		return False, pools, character
	else:
		w = [25, 75]
		for _ in range(int(choice)):
			pools += 1
			res = random.choices(v, weights=w, k=1)
			if res[0] == 'S':
				char_choice = ['Hugo', 'Nekomata', 'Koleda', 'Grace', 'Rina', 'Lycaon', 'Soldier 11']
				chances = [52, 8, 8, 8, 8, 8, 8]
				character = random.choices(char_choice, weights=chances, k=1)[0]
				return True, pools, character
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
			break
		else:
			print(f'\n  К сожалению, пока только "poop"...\n\nОсталось {user_pools} круток')


if __name__ == "__main__":
	main()