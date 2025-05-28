# Программа рандомного подбора числовой последовательности

import random

line = '\n############### ############### ###############'


def main():
    print('\n  === Подбор числовой последовательности ===')
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
        num_len = len(str(user_num))

        print("\nПопытки:\n")

        step = 1
        notWin = True
        while notWin:
            rand_num_str = ''
            rand_num_list = []
            first_num = True
            for _ in range(num_len):
                if first_num and num_len > 1:
                    rand_num = random.randint(1, 9)
                else:
                    rand_num = random.randint(0, 9)
                first_num = False
                rand_num_list.append(str(rand_num))
            rand_num_str = ''.join(rand_num_list)
            print(f"> {rand_num_str}")
            if rand_num_str == str(user_num):
                notWin = False
            else:
                step += 1

        print(f"\nВсего попыток ->  {step}\n")


        input()


if __name__ == "__main__":
	main()