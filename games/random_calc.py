# Калькулятор, производящий рандомные вычисления

import random
import time

line = '\n############### ############### ###############'


def main():
    print('\n         === Рандомный калькулятор ===')
    print('\n Введите число и получите случайный результат!\n')
    while True:
        random.seed(time.time())
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
        print()

        op = random.randint(0, 2)
        n = user_num + random.randint(0, 999)
        if n < 0: n *= -1
        num = random.randint(1, n)
        if op == 0:
            res = user_num + num
        elif op == 1:
            res = user_num - num
        elif op == 2:
            res = user_num * num
        if res < 0: res *= -1
        print(f" >>  {res}  <<\n")

        input()


if __name__ == "__main__":
	main()