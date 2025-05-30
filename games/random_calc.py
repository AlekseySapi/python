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
        num = random.randint(1, user_num * 2)
        if op == 0:
            res = user_num + num
            print(f" {user_num} + {num} =  {res}")
        elif op == 1:
            res = user_num - num
            print(f" {user_num} - {num} =  {res}")
        elif op == 2:
            res = user_num * num
            print(f" {user_num} * {num} =  {res}")
        print()

        input()


if __name__ == "__main__":
	main()