# Программа рандомного подбора числовой последовательности

import random

line = '\n################# ################# #################'


def main():
    print('\n     === Подбор числовой последовательности ===')
    while True:
        print(line)
        print("\nВведите число:")
        s = '>'
        notNum = True
        while notNum:
            try:
                user_num = int(input(f'{s} ').strip())
                notNum = False
            except:
                s += '>'
        if user_num < 0: user_num *= -1


        input()


if __name__ == "__main__":
	main()