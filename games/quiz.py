# Начну реализовывать программу-опрос

import random

line = '\n############### ############### ###############'


def main():
    print('\n   === Опрос от Sapi ===')
    while True:
        print(line)
        print("\n>> 2 * 2 =\n")
        print('1 - "4", 2 - "5", 3 - не знаю, 4 - неважно')
        s = '>'
        while True:
            n1 = input(f"{s} ")
            if n1 in ['1', '2', '3', '4']:
                n1 = int(n1)
                break
            else:
                s += '>'
                continue
        print()

        print("\n>> Утро для тебя - это..\n")
        print('1 - Кофе, 2 - Суета, 3 - Медитация, 4 - другое')
        s = '>'
        while True:
            n2 = input(f"{s} ")
            if n2 in ['1', '2', '3', '4']:
                n2 = int(n2)
                break
            else:
                s += '>'
                continue
        print()

        if n1 == 1 and n2 == 1:
            print("\nКлассно! Вы прошли опрос, ответив на все опросы как и я!\n Добро пожаловать в мою группу:")
            print(" >>  https://t.me/sapi_group  <<")
        else:
            print("Опрос пройден!")
        input()


if __name__ == "__main__":
	main()