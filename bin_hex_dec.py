def is_hex(num):
    try:
        int(num, 16)
        return True
    except ValueError:
        return False
        
def is_bin(num):
    try:
        int(num, 2)
        return True
    except ValueError:
        return False


def main():
     
    while True:
        print("===== ===== =====")
        while True:
            choice = input("В какую систему счисления перевести число?\nВведите 2 (b), 16 (h) или 10 (d):\n> ")
            if choice == "2" or choice == "b" or choice == "16" or choice == "h" or choice == "10" or choice == "d":
                break

        if choice == "2" or choice == "b":
            decimal = int(input("Число: "))
            binary = bin(decimal)[2:]
            print(f"  {decimal} -> {binary}\n")
        elif choice == "16" or choice == "h":
            decimal = int(input("Число: "))
            hex_num = hex(decimal)[2:]
            print(f"  {decimal} -> {hex_num.upper()}\n")
        elif choice == "10" or choice == "d":
            num = input("Число: ")
            
            if is_bin(num):
                decimal = int(num, 2)  # 2 указывает на основание, если есть префикс - можно указать 0
            elif is_hex(num):
                decimal = int(num, 16)
            else:
                exit()
            
            print(f"  {num} -> {decimal}\n")


if __name__ == "__main__":
    main()