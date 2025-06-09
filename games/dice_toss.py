# Бросок кубиков

import random
import time

line = '\n############### ############### ###############'


def main():
    print('\n         ===== Бросок кубиков =====')
    while True:
        random.seed(time.time())
        print(line)
        print("\nСколько кубиков бросаем (1, 2, 3, 4 или 5)?")
        s = '>'
        while True:
            n = input(f"{s} ")
            if n in ['1', '2', '3', '4', '5']:
                n = int(n)
                break
            else:
                s += '>'
                continue
        print()

        if n == 1:
            print(f"\nБросок 1 кубика:\n")
        else:
            print(f"\nБросок {n} кубиков:\n")
        die = []
        i = 0
        win = True
        sum = 0
        for _ in range(n):
            die.append(random.randint(1, 6))
            sum += die[i]
            print(f"> {die[i]}")
            if die[i] != 6:
                win = False
            i += 1
        if win:
            print("\nПобеда!!!")
        elif i != 1:
            print(f"\nСумма: {sum}")
        input()


if __name__ == "__main__":
	main()