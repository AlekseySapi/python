

line = '\n######## ######## ########'


def is_prime(n):
    i = 3
    mid = (n - 2) // 4
    for _ in range(mid):
        if n % i == 0:
            return False
        i += 2
    return True


def main():
    while True:
        print(line)
        num = int(input("# Введите число:\n> "))

        if is_prime(num):
            print(f"  Число {num} ->  Простое")
        else:
            print(f"  Число {num} ->  Составное")



if __name__ == "__main__":
    main()