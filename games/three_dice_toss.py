# Подбрасывание трёх кубиков

import random
import time

line = '\n############### ############### ###############'


def main():
    print('\n      === Подбрасывание трёх кубиков ===')
    while True:
        random.seed(time.time())
        print(line)
        print("\nБросаем кубики? (y/Y):")
        s = ''
        answer = ''
        while True:
            if answer not in ['y', 'Y']:
                s += '>'
                answer = input(f'{s} ').strip()
            else:
                break
        print()

        die_1 = random.randint(1, 6)
        die_2 = random.randint(1, 6)
        die_3 = random.randint(1, 6)

        print(f" Первый кубик:  {die_1}\n Второй кубик:  {die_2}\n Третий кубик:  {die_3}")

        if die_1 == 1 and die_2 == 1 and die_3 == 1:
            print("\n Мдаа..) Увы...")
        elif die_1 == 6 and die_2 == 6 and die_3 == 6:
            print("\n Победа!!!")
        print()


if __name__ == "__main__":
	main()