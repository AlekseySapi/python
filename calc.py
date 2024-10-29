# Классический калькулятор

def sum(a, b):
    res = a + b
    if res.is_integer():
        res = int(res)
    return res

def diff(a, b):
    res = a - b
    if res.is_integer():
        res = int(res)
    return res

def multi(a, b):
    res = a * b
    if res.is_integer():
        res = int(res)
    return res

def divide(a, b):
    res = a / b
    if res.is_integer():
        res = int(res)
    return res

def power(a, b):
    res = a ** b
    if res.is_integer():
        res = int(res)
    return res


while True:
    while True:
        user_input = input("Введите первое число: ")
        try:
            n1 = float(user_input)  # Пробуем преобразовать в число
            break  # Выход из цикла, если ввод корректный
        except ValueError:
            print("Ошибка: Нужно вводить только числа. Попробуйте снова.")

    while True:
        op = input("Введите действие (+ - * / или ^ для возведения в степень): ")
        match op:
            case '+':
                break
            case '-':
                break
            case '*':
                break
            case '/':
                break
            case '^':
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


    # Переводим введённые числа в целый формат, если это возможно

    if n1.is_integer():
        n1 = int(n1)

    if n2.is_integer():
        n2 = int(n2)
            

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
        case '^':
            print(f"Возведение в степень: {n1}^{n2} = {power(n1, n2)}\n=== === ===")
        case _:
            print("Ошибка..\n=== === ===")