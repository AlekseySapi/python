import math

line = '\n######## ######## ########'


def is_prime(n):
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    sqrt = math.isqrt(n)  # Округление корня в меньшую сторону
    # print(f'Корень = {sqrt}')
    while i <= sqrt:
        # print(i)
        if n % i == 0 or n % (i + 2) == 0:  # Рассматриваем по паре чисел в областях, кратных 6+-1
            return False
        i += 6
    return True


def main():
    while True:
        print(line)
        while True:
            try:
                num = int(input("# Введите число:\n> "))
            except:
                print()
                continue
            if num < 2:
                print()
                continue
            else:
                break

        if is_prime(num):
            print(f"  Число {num} ->  Простое")
        else:
            print(f"  Число {num} ->  Составное")



if __name__ == "__main__":
    main()