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
    num_len = len(str(num))
    k = 1
    i = 0
    for _ in range(num_len):
        i += 1
        if i % 4 == 0:
            k *= 10
    while len(choices) < 4:
        if operation == '/':
            v = random.choice([1, 2, 3])
            if v == 1:
                if num % 10 >= 2:
                    rand_num = num - (random.randint(1, 199) / 100)
                    rand_num = round(rand_num, 2)
                elif num % 10 >= 1:
                    rand_num = num - (random.randint(1, 99) / 100)
                    rand_num = round(rand_num, 2)
                else:
                    rand_num = num + (random.randint(1, 199) / 100)
                    rand_num = round(rand_num, 2)
            elif v == 2:
                if num % 10 >= 2:
                    rand_num = num - (random.randint(1, 199) / 100)
                    rand_num = round(rand_num, 2)
                elif num % 10 >= 1:
                    rand_num = num - (random.randint(1, 99) / 100)
                    rand_num = round(rand_num, 2)
                else:
                    rand_num = num + (random.randint(1, 49) / 100)
                    rand_num = round(rand_num, 2)
            else:
                if num % 10 >= 2:
                    rand_num = num - (random.randint(1, 199) / 100)
                    rand_num = round(rand_num, 2)
                elif num % 10 >= 1:
                    rand_num = num - (random.randint(1, 99) / 100)
                    rand_num = round(rand_num, 2)
                else:
                    rand_num = num + (random.randint(1, 9) / 100)
                    rand_num = round(rand_num, 2)
        else:
            if (num % 10 * k) > (9 * k):
                rand_num = num - random.randint(1, 9 * k)
            else:
                rand_num = num + random.randint(1, 9 * k)
            while rand_num % 10 != num % 10:
                v = random.choice([1, 2, 3])
                if v == 1:
                    rand_num = num + random.randint(1, 49 * k)
                elif v == 2:
                    rand_num = num + random.randint(1, 9 * k)
                else:
                    if (num % 100 * k) > (19 * k):
                        rand_num = num - random.randint(1, 9 * k)
                    elif (num % 10 * k) > (9 * k):
                        rand_num = num - random.randint(1, 5 * k)
                    else:
                        rand_num = num + random.randint(1, 9 * k)
        if rand_num not in choices:
            choices.append(rand_num)
    random.shuffle(choices)
    return choices
        

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
                s = ''
                while user_answer.lower() not in ('1', '2', '3', '4', 'q'):
                    s += '>'
                    user_answer = input(f'{s} ').strip()
                
                if user_answer.lower() == 'q':
                    keep_playing = False
                    print(line)
                    break

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