import random
import time

line = '\n======= ======= ======='

seed_value = int(time.time() * 1000)  # сид в милисекундах
random.seed(seed_value)


def main():
    while True:
        print(line)
        n = 0
        while not (1 <= n <= 10):
            try:
                n = int(input("Кол-во цифр (1-10): "))
            except ValueError:
                continue
        if n == 1:
            rand_num = random.randint(0, 9)
        else:
            digits = list(range(10))
            first_digit = random.choice(digits[1:]) # Выбираем первой цифрой не ноль
            digits.remove(first_digit)  # Удаляем её из набора

            random.shuffle(digits)  # Перемешиваем оставшиеся цифры

            digits = [first_digit] + digits
            
            rand_num = ''.join(str(digit) for digit in digits[:n])  # Берём первые n цифр и склеиваем их в строку

        print()
        print(f'> {rand_num}')



if __name__ == "__main__":
    main()