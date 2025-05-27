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

        print("\nПопытки:\n")

        step = 1
        notWin = True
        while notWin:
            rand_num_str = ''
            num_len = len(str(user_num))
            for _ in range(num_len):
                rand_num = random.randint(0, 9)
                rand_num_str += str(rand_num)
            print(f"> {rand_num_str}")
            if rand_num_str == str(user_num):
                notWin = False
            else:
                step += 1

        print(f"\nВсего попыток ->  {step}\n")


        input()


if __name__ == "__main__":
	main()