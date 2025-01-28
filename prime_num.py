import math

line = '\n######## ######## ########'


def is_prime(n):
    if n == 1 or n == 2:
        return True
    if n % 2 == 0:
        return False
    
    i = 3
    sqrt = math.isqrt(n)  # Округление корня в меньшую сторону
    # print(f'Корень = {sqrt}')
    while i <= sqrt:
        # print(i)
        if n % i == 0:
            return False
        i += 2
    return True


def main():
    while True:
        print(line)
        while True:
            num = int(input("# Введите число:\n> "))
            if num < 1:
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