import random

line = '\n================ ================ ================'

def get_random_number(digits):
    num = 0
    while num == 0:
        num = random.randint(-10**digits + 1, 10**digits - 1)
    return num

def get_random_divisible_number(digits):
    num2 = random.randint(2, 10)
    num1 = num2 * random.randint(1, 10**digits // num2)
    return num1, num2

def generate_expression(digits):
    operations = ['+', '-', '*', '/']
    op1, op2 = random.choices(operations, k=2)
    
    if op1 == '/':
        num1, num2 = get_random_divisible_number(digits)
    else:
        num1, num2 = get_random_number(digits), get_random_number(digits)
    
    if op2 == '/':
        num2, num3 = get_random_divisible_number(digits)
    else:
        num3 = get_random_number(digits)

    expr = f"{num1} {op1} {num2} {op2} {num3}"
    correct_result = eval(expr)
    
    return expr, correct_result

def main():
    print('\nТренировка арифметики')
    
    digits = 1
    correct_answers = 0
    
    while True:
        expr, correct_result = generate_expression(digits)
        print(line)
        
        while True:
            user_answer = input(f'   {expr} = ')
            
            try:
                if float(user_answer) == correct_result:
                    print('✅ Верно!')
                    correct_answers += 1
                    break
                else:
                    print('❌ Неверно, попробуйте ещё раз.\n')
            except ValueError:
                print('⚠️  Введите число!\n')
                
        if correct_answers % 3 == 0:
            digits += 1
            print(f'\n🔥 Уровень повышен! Теперь числа до {10**digits - 1}!')

if __name__ == "__main__":
    main()