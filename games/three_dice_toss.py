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




if __name__ == "__main__":
	main()