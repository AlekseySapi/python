import random

line = '\n================ ================ ================'

def get_random_number(digits):
    ch = random.choices([1, 2], [7, 3], k=1)[0]	# 70% - вероятность выбора 1
    if ch == 1:
        return random.randint(2, 10**digits - 1)
    else:
        return random.randint(2, 9)

def generate_expression(digits):
    operations = ['+', '-', '*', '/']
    w = [55, 25, 15, 5]
    op1, op2, op3 = random.choices(operations, weights=w, k=3)

    num1, num2, num3, num4 = get_random_number(digits), get_random_number(digits), get_random_number(digits), get_random_number(digits)

    expr = f"{num1} {op1} {num2} {op2} {num3} {op3} {num4}"
    correct_result = round(eval(expr), 2)

    return expr, correct_result

def main():
    print('\nТренировка арифметики')
    print('\n(при делении  ->  округляем до сотых)')

    digits = 1
    correct_answers = 0

    while True:
        expr, correct_result = generate_expression(digits)
        print(line)

        while True:
            user_answer = input(f'   {expr} = ').replace(',', '.')

            try:
                if float(user_answer) == correct_result:
                    print('✅ Верно!')
                    correct_answers += 1
                    break
                else:
                    print('❌ Неверно, попробуйте ещё раз.\n')
                    correct_answers -= 1
            except ValueError:
                print('⚠️  Введите число!\n')

        if (correct_answers > 0) and (correct_answers % 3 == 0):
            digits += 1
            print(f'\n🔥 Предел генерации чисел повышен до {10**digits - 1}!')

if __name__ == "__main__":
    main()