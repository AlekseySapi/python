import random
import time


while True:
	print('\n===================== ===================== =====================\n')
	n = 0
	while True:
		try:
			n = int(input(f'Введите кол-во раундов: '))
			if 10 <= n <= 100_000_000:
				break
			print()
		except:
			print()
			continue
	change = ''
	while change.lower() not in ['y', 'n']:
		change = input('\nМенять выбор? (y/n)\n> ')
	prc_10 = round(n / 10)
	print('\n...')
	wins = 0
	i = 0
	p = 1
	random.seed(time.time())
	for _ in range(n):
		i += 1
		if i % prc_10 == 0:
			print(f'{p * 10}%')
			p += 1
		nums = [0, 1, 0]
		random.shuffle(nums)
		a = nums[0]
		b = nums[1]
		c = nums[2]
		# print(nums)
	
		choices = [0, 1, 2]
		choice = random.choice(choices)
		# print(choice)
		if change.lower() == 'y':
			if choice == 0 and b == 0:
				choice = 2
			if choice == 0 and c == 0:
				choice = 1
			if choice == 1 and a == 0:
				choice = 2
			if choice == 1 and c == 0:
				choice = 0
			if choice == 2 and a == 0:
				choice = 1
			if choice == 2 and b == 0:
				choice = 0
			
		if nums[choice]:
			wins += 1
	
	print(f'\n\n  Проведено {n:,} раундов...  -->  {wins} побед!  [{(wins * 100) // n}%]\n')