# Случайная последовательность

import random

line = '\n############### ############### ###############'


def main():
    print('\n   === Случайная последовательность ===')
    while True:
        print(line)
        print("\nВведите seed для рандома:")
        s = '>'
        notNum = True
        while notNum:
            try:
                user_num = int(input(f'{s} ').strip())
                notNum = False
            except:
                s += '>'
        random.seed(user_num)
        print()

        print(" Результат:")
        first_num = random.randint(0, 9)
        sequence = []
        sequence.append(first_num)
        num = first_num
        for _ in range(9):
            num += random.randint(1, 9)
            sequence.append(num)
        print(f" >>  {sequence}  <<\n")

        input()


if __name__ == "__main__":
	main()