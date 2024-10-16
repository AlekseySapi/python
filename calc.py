# Классический калькулятор

def sum(a, b):
    return a + b

def diff(a, b):
    return a - b

def multi(a, b):
    return a * b

def divide(a, b):
    return a / b


while 1:
    n1 = float(input("Введите первое число: "))
    op = ''
    while op != '+' and op != '-' and op != '*' and op != '/':
        print("Введите действие")
        op = input("(+ - * или /): ")
    n2 = float(input("Введите первое число: "))

    match op:
        case '+':
            print(f"Сумма чисел: {n1} + {n2} = {sum(n1, n2)}\n=== === ===")
        case '-':
            print(f"Разность чисел: {n1} - {n2} = {diff(n1, n2)}\n=== === ===")
        case '*':
            print(f"Произведение чисел: {n1} * {n2} = {multi(n1, n2)}\n=== === ===")
        case '/':
            if n2 == 0:
                print("На ноль делить нельзя!\n=== === ===")
            else:
                print(f"Частное чисел: {n1} / {n2} = {divide(n1, n2)}\n=== === ===")
        case _:
            print("Ошибка..\n=== === ===")