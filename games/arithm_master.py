import random

line = '\n================ ================ ================'

def get_random_number(digits):
    ch = random.choices([1, 2], [7, 3], k=1)[0]	# 70% - вероятность выбора 1
    if ch == 1:
        return random.randint(2, 10**digits - 1)
    else:
        return random.randint(2, 9)

def generate_expression(digits, op_choice):
    if op_choice == '1':
        operations = ['+', '-', '*', '/']
        w = [55, 25, 15, 5]
    else:
        operations = ['+', '-', '*']
        w = [55, 25, 20]
    op1, op2, op3 = random.choices(operations, weights=w, k=3)

    num1, num2, num3, num4 = get_random_number(digits), get_random_number(digits), get_random_number(digits), get_random_number(digits)

    expr = f"{num1} {op1} {num2} {op2} {num3} {op3} {num4}"
    correct_result = round(eval(expr), 2)

    return expr, correct_result

def main():
    print('\nТренировка арифметики')
    print('\n(при делении  ->  округляем до сотых)')
    print('\n\n Чтобы начать заново, введите ->  q\n')
    print(' Для получения ответа, введите ->  pass\n')
    while True:
        print(line)
        print('  1 - Добавить операции деления, 2 - Без них')
        op_choice = ''
        s = ''
        while op_choice not in ('1', '2'):
            s += '>'
            op_choice = input(f'{s} ').strip()
        digits = 1
        correct_answers = 0
        keep_playing = True
        while keep_playing:
            expr, correct_result = generate_expression(digits, op_choice)
            print(line)

            while True:
                user_answer = input(f'   {expr} = ').replace(',', '.')
                if user_answer.lower() == 'q':
                    keep_playing = False
                    print()
                    break
                if user_answer.lower() == 'pass':
                    print(f'\n Ответ: {correct_result}\n')
                    correct_answers -= 1
                    break

                try:
                    if float(user_answer) == correct_result:
                        print('✅ Верно!')
                        correct_answers += 1
                        # print(f'\n correct_answers = {correct_answers}\n')
                        break
                    else:
                        print('❌ Неверно, попробуйте ещё раз.\n')
                        correct_answers -= 1
                        # print(f'( correct_answers = {correct_answers} )\n')
                except ValueError:
                    print('⚠️  Введите число!\n')

            if (correct_answers > 0) and (correct_answers % 3 == 0):
                digits += 1
                correct_answers = 0
                print(f'\n🔥 Предел генерации чисел повышен до {10**digits - 1}!')

if __name__ == "__main__":
    main()