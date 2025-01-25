# Калькулятор by AlekseySapi
# С фиксированным первым числом для работы только с ним

from decimal import Decimal, InvalidOperation, getcontext


# Точность -> 42 знака после запятой
getcontext().prec = 42


#####################  Самые важные и интересные константы нашей Вселенной  ######################################################
##################################################################################################################################
constants = {
    'c': Decimal('299792458'),       #  м/с  ->  E = m * c^2  [Скорость света]
    'h': Decimal('6.62607015E-34'),      #  *10^(−34)  Дж·с  ->  E = h * ν  < Энергия фотона >  [Постоянная Планка]
    'el': Decimal('1.602176634E-19'),    #  *10^(−19)  Кл  [Заряд электрона]
    'g_const': Decimal('6.67430E-11'),   #  *10^(−11)  м³/(кг·с²)  [Гравитационная постоянная]
    'g': Decimal('9.8'),             #  м/с^2  [Ускорение свободного падения]
    'g_moon': Decimal('1.62'),       #  м/с^2  [Ускорение свободного падения на Луне]
    'g_mars': Decimal('3.86'),       #  м/с^2  [Ускорение свободного падения на Марсе]
    'me': Decimal('9.1093837015E-31'),   #  *10^(−31)  кг  [Модульная масса электрона]
    'e0': Decimal('8.8541878128E-12'),   #  *10^(−12)  Ф/м  ->  уравнения Максвелла  [Электромагнитная постоянная]
    'kB': Decimal('1.380649E-23'),       #  *10^(−23)  Дж/К  [Постоянная Больцмана]
    'nA': Decimal('6.02214076E23'),     #  * 10^23  молекул/моль  [Число Авогадро]
    'cL': Decimal('1.1E-52'),            #  *10^(−52)  м^(−2)  ->  Расширение Вселенной (тёмная энергия)  Λ  [Космологич. постоянная]
    'al': Decimal('0.0072973525643'),    #  [Постоянная тонкой структуры] -> связывает фундаментальные константы (c, h, el)
    'al_rev': Decimal('137.035999177'),  #  Обратное значение
    'al_rev_int': Decimal('137'),        #  В виде целого числа
    'pi': Decimal('3.14159265'),         #  Отношение длины окружности к её диаметру
    'pi42': Decimal('3.141592653589793238462643383279502884197169'),     #  Точность до 42 знака после запятой
    'e': Decimal('2.718281828459'),      #  [Число Эйлера]  ->  Экспоненциальный рост / затухание
    'f': Decimal('1.618'),               #  [Золотое сечение]  с точностью до 3х знаков
    'f20': Decimal('1.61803398874989484820'),    #  Точность - 20 знаков
    'v1': Decimal('7.91'),               #  км/с  [Первая космическая скорость]
    'v2': Decimal('11.186'),             #  км/с  [Вторая космическая скорость]
    'v3': Decimal('16.65'),              #  км/с  [Третья космическая скорость]
    'abs_zero': Decimal('-273.15'),        #  °C  [Абсолютный нуль температуры]
    'c7': Decimal('142857'),             #  Цикл из 6 цифр  при делении  1/7  (+ при умножении на 1-6 оно также идёт по циклу)
    'c13': Decimal('769230'),            #  Цикл при делении  1/13  (076923)
    'c14': Decimal('714285'),            #  Цикл при делении  1/14
    'c17': Decimal('5882352941176470'),  #  Цикл при делении  1/17  (0588235294117647)  16 знаков
    'c19': Decimal('526315789473684210'),    #  Цикл при делении  1/19  (052631578947368421)  18 знаков
    'c137': Decimal('72992700')          #  (00729927)
}
##################################################################################################################################

line = "\n=============== =============== ==============="


def get_constant_or_number(input_value):
    if input_value in constants:
        return constants[input_value]
    try:
        return Decimal(input_value)
    except:
        raise ValueError("!  Введите либо число, либо допустимую константу.\n")

def format_number(n):
    # Убираем .0, если число целое
    return int(n) if n == n.to_integral_value() else n


print("\n +  -  *  /   <--   Арифм. действия")
print(" %   <--   Нахождение процента от числа")
print(" ^            <--   Возведение в степень")
print(" root   <--   Корень (для квадратного, укажите степень -> 2)")
print("\n (i  ->  квадр. корень из -1)")

if __name__ == "__main__":
    print(line)
    while True:
        try:
            # Ввод первого числа
            user_input1 = input("> Введите первое число или константу: ")
            n1 = get_constant_or_number(user_input1)
        except (InvalidOperation, ValueError):
            print("\n!  Ошибка. Попробуйте снова.")
            continue
        break

    while True:
        while True:
            try:
                # Ввод действия
                operation = input(">> Введите действие: ")
                if operation not in ('+', '-', '*', '/', '%', '^', 'root'):
                    raise ValueError("Неверное действие.\n   Используйте  +, -, *, /, %, ^ или root")
                break
            except ValueError as e:
                print(f"\n!  Ошибка: {e}\n")
                continue

        while True:
            try:
                # Ввод второго числа
                if operation == 'root':
                    user_input2 = input("> Введите степень корня: ")
                else:
                    user_input2 = input("> Введите второе число или константу: ")
                n2 = get_constant_or_number(user_input2)


                # Проверка деления на 0
                if operation == '/' and n2 == 0:
                    raise ZeroDivisionError("На 0 делить нельзя.")
                if (operation == '^' or operation == 'root') and n2 <= 0:
                    raise ValueError
                if operation == 'root' and n1 < 0 and n2 > 3 and n2 % 2 == 0:
                    raise ValueError
                break
            except (InvalidOperation, ValueError):
                print("\n!  Ошибка. Попробуйте снова.\n")
                continue
            except ZeroDivisionError as e:
                print(f"\n!  Ошибка: {e}\n")
                continue
                
                
        complex_check = False
        neg_check = False
        # Выполнение операции
        if operation == '+':
            result = n1 + n2
        elif operation == '-':
            result = n1 - n2
        elif operation == '*':
            result = n1 * n2
        elif operation == '/':
            result = n1 / n2
        elif operation == '%':
            result = (n1 * n2) / 100
        elif operation == '^':
            result = n1 ** n2
        elif operation == 'root':
            if n1 < 0 and n2 == 2:
                complex_check = True
                n1 *= -1
            elif n1 < 0 and n2 % 2 != 0:
                neg_check = True
                n1 *= -1
            dec_root = Decimal(1) / Decimal(n2)
            result = n1 ** dec_root
            

        # Форматируем числа и выводим результат
        n1_formatted = format_number(n1)
        n2_formatted = format_number(n2)
        result_formatted = format_number(result)

        if complex_check:
            print(f"\n[  Результат:  -{n1_formatted} {operation} {n2_formatted} = {result_formatted} * i  ]\n\n")
        elif neg_check:
            print(f"\n[  Результат:  -{n1_formatted} {operation} {n2_formatted} = -{result_formatted}  ]\n\n")
        else:
            print(f"\n[  Результат:  {n1_formatted} {operation} {n2_formatted} = {result_formatted}  ]\n\n")

        print(f'> Первое число: {user_input1}')


####  Поле для расчётов  ####
'''







'''
#############################