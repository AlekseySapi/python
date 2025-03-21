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

def get_choices(num, operation):
    choices = [num]
    while len(choices) < 4:
        if operation == '/':
            v = random.choice([1, 2, 3])
            if v == 1:
                rand_num = num + (random.randint(1, 999) / 100)
                rand_num = round(rand_num, 2)
            elif v == 2:
                rand_num = num + (random.randint(1, 499) / 100)
                rand_num = round(rand_num, 2)
            else:
                rand_num = num + (random.randint(1, 9) / 100)
                rand_num = round(rand_num, 2)
        else:
            v = random.choice([1, 2, 3])
            if v == 1:
                rand_num = num + random.randint(1, 99)
            elif v == 2:
                rand_num = num + random.randint(1, 49)
            else:
                rand_num = num + random.randint(1, 2)
        if rand_num not in choices:
            choices.append(rand_num)
    random.shuffle(choices)
    return choices
        

def main():
    print('\nТренировка арифметики')
    print('\nВыберите действие: 1: [+]  2: [-]  3: [*]  4: [/]')
    operation_choice = ''
    while operation_choice not in ('1', '2', '3', '4'):
        operation_choice = input('> ').strip()

    operation_mapping = {'1': '+', '2': '-', '3': '*', '4': '/'}
    operation = operation_mapping[operation_choice]
    
    digits1, digits2 = 1, 1
    correct_answers = 0
    
    while True:
        num1 = get_random_number(digits1)
        num2 = get_random_number(digits2)
        if operation in ('*', '/'):
            while num1 == 1:
                num1 = get_random_number(digits2)
            while num2 == 1:
                num2 = get_random_number(digits2)
        
        correct_result = get_operation_result(num1, num2, operation)
        print(line)
        print(f'   {num1} {operation} {num2} =')
        choices = get_choices(correct_result, operation)
        print(f'\n  1: {choices[0]}   2: {choices[1]}   3: {choices[2]}   4: {choices[3]}')
        
        while True:
            user_answer = ''
            while user_answer not in ('1', '2', '3', '4'):
                user_answer = input('> ').strip()

            choices_mapping = {'1': choices[0], '2': choices[1], '3': choices[2], '4': choices[3]}
            choice = choices_mapping[user_answer]
            if choice == correct_result:
                print(' ✅ Верно!')
                correct_answers += 1
                break
            else:
                print(' ❌ Неверно, попробуйте ещё раз.\n')
                
        if correct_answers % 3 == 0:
            if digits1 == digits2:
                digits1 += 1
            else:
                digits2 += 1

if __name__ == "__main__":
    main()