import random

line = '\n============= ============= ============='

def new_number():
    return random.randint(1, 100)

def main():
    print('\nИгра "Угадай число"  (от 1 до 100)')
    print('\nВведите ->  pass  <- чтобы начать заново')
    
    while True:
        number = new_number()
        print(line)
        print('       <  Новое число загадано!  >\n')
        
        win = False
        step = 0
        
        while not win:
            step += 1
            print(f'== {step} шаг ==')
            user_num = ''
            s = ''
            
            while not (user_num.isdigit() and 1 <= int(user_num) <= 100):
                s += '>'
                user_num = input(f'{s} ')
                if user_num == 'pass':
                    win = True
                    print(f'\nБыло загадано -> {number}\n')
                    break
            
            if not win:
                user_num = int(user_num)
                
                if user_num < number:
                    print(' Загаданное число больше [>]\n')
                elif user_num > number:
                    print(' Загаданное число меньше [<]\n')
                else:
                    print('\n ✅ Вы угадали!\n')
                    win = True

if __name__ == "__main__":
    main()