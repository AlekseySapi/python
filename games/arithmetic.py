import random

line = '\n================ ================ ================'

def get_random_number(digits):
    return random.randint(10**(digits-1), 10**digits - 1)

def get_operation_result(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return round(num1 / num2, 2)  # Округляем до двух знаков

def main():
    print('\nТренировка арифметики')
    print('\n для возврата к выбору действия, введите ->  q\n')
    while True:
        print('\nВыберите действие: 1: [+]  2: [-]  3: [*]  4: [/]')
        operation_choice = ''
        s = ''
        while operation_choice not in ('1', '2', '3', '4'):
            s += '>'
            operation_choice = input(f'{s} ').strip()

        operation_mapping = {'1': '+', '2': '-', '3': '*', '4': '/'}
        operation = operation_mapping[operation_choice]
        
        digits1, digits2 = 1, 1
        correct_answers = 0

        keep_playing = True
        
        while keep_playing:
            num1 = get_random_number(digits1)
            num2 = get_random_number(digits2)
            if operation in ('*', '/'):
                while num2 == 1:
                    num2 = get_random_number(digits2)
            
            correct_result = get_operation_result(num1, num2, operation)
            print(line)
            
            while True:
                user_answer = input(f'   {num1} {operation} {num2} = ').replace(',', '.')
                if user_answer.lower() == 'q':
                    keep_playing = False
                    print(line)
                    break
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
                if digits1 == digits2:
                    digits1 += 1
                else:
                    digits2 += 1

if __name__ == "__main__":
    main()