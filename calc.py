# Классический калькулятор

def sum(a, b):
    return a + b

def diff(a, b):
    return a - b

def multi(a, b):
    return a * b

def divide(a, b):
    return a / b


while True:
    while True:
        user_input = input("Введите первое число: ")
        try:
            n1 = float(user_input)  # Пробуем преобразовать в число
            break  # Выход из цикла, если ввод корректный
        except ValueError:
            print("Ошибка: Нужно вводить только числа. Попробуйте снова.")

    while True:
        op = input("Введите действие (+ - * или /): ")
        match op:
            case '+':
                break
            case '-':
                break
            case '*':
                break
            case '/':
                break
            case _:
                print("Ошибка: Введите одно из 4 действий. Попробуйте снова.")
    
    while True:
        user_input = input("Введите второе число: ")
        try:
            n2 = float(user_input)  # Пробуем преобразовать в число
            break  # Выход из цикла, если ввод корректный
        except ValueError:
            print("Ошибка: Нужно вводить только числа. Попробуйте снова.")
            

    match op:
        case '+':
            print(f"Сумма чисел: {n1} + {n2} = {sum(n1, n2)}\n=== === ===")
        case '-':
            print(f"Разность чисел: {n1} - {n2} = {diff(n1, n2)}\n=== === ===")
        case '*':
            print(f"Произведение чисел: {n1} * {n2} = {multi(n1, n2)}\n=== === ===")
        case '/':
            if n2 == 0:
                print("Ошибка: На ноль делить нельзя!\n=== === ===")
            else:
                print(f"Частное чисел: {n1} / {n2} = {divide(n1, n2)}\n=== === ===")
        case _:
            print("Ошибка..\n=== === ===")