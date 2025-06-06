import random

line = '\n======= ======= ======='
n = 4

def new_num():
    digits = list(range(10))
    random.shuffle(digits)
    return ''.join(str(digit) for digit in digits[:n])

def check_num(user_num, num):
    b = 0
    c = 0
    for i in range(n):
        if user_num[i] == num[i]:
            b += 1
        elif user_num[i] in num:
            c += 1
    return b, c


def main():
    print('\nИгра "Быки и коровы"\n\nНеобходимо угадать четырёхзначное число\n')
    print("(Цифры числа не повторяются)\n")
    print("[ Б - это быки, К - коровы ]")
    print("Быки - количество угаданных цифр на верных позициях,\nКоровы - угаданные цифры, но стоящие не на своих местах\n")
    print("\nВведите ->  pass  <- чтобы было загадано новое число\n")
    while True:
        num = new_num()
        print(line)
        print(" <  Число загадано!  >\n")
        
        win = False
        step = 0
        while not win:
            step += 1
            print(f"== {step} шаг ==")
            user_num = ''
            s = ''
            while not ((len(set(user_num)) == 4) and (len(user_num) == 4)):
                s += '>'
                try:
                    user_num = input(f"{s} ")
                    if user_num == 'pass':
                        win = True
                        print(f"\nБыло загадано -> {num}\n")
                        break
                    check = int(user_num)
                except ValueError:
                    continue
                
            if not win:
                b, c = check_num(user_num, num)
                print(f"[ {b}Б, {c}К ]\n")

                if b == 4:
                    print("Вы угадали!\n")
                    win = True


if __name__ == "__main__":
    main()