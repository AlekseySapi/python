# Программа-опрос  Sapi Quiz

import random

line = '\n############### ############### ###############'
q = ["2 * 2 =", "Утро для тебя - это.."]


def main():
    print('\n   === Sapi Quiz ===')
    while True:
        answers = ''
        print(line)
        print(f"\n>> {q[0]}\n")
        print('1 - "4", 2 - "5", 3 - не знаю, 4 - неважно')
        s = '>'
        while True:
            n1 = input(f"{s} ")
            if n1 in ['1', '2', '3', '4']:
                answers += n1
                break
            else:
                s += '>'
                continue
        print()

        print(f"\n>> {q[1]}\n")
        print('1 - Кофе, 2 - Суета, 3 - Медитация, 4 - другое')
        s = '>'
        while True:
            n2 = input(f"{s} ")
            if n2 in ['1', '2', '3', '4']:
                answers += n2
                break
            else:
                s += '>'
                continue
        print()

        if answers == '11':
            print("\nКлассно! Вы прошли опрос, ответив на все опросы как и я!\n Добро пожаловать в мою группу:")
            print(" >>  https://t.me/sapi_group  <<")
        else:
            print("Опрос пройден!")
        input()


if __name__ == "__main__":
	main()