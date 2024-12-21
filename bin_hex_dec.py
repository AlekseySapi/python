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

line = "===== ===== ===== ===== ===== ===== ====="
line2 = "===== ===== =====\n  [db / hb] -> 2,\n  [bh / dh] -> 16,\n  [bd / hd] -> 10:"


def main():
    
    print(line)
    print("В какую систему счисления перевести число?")
    print("Введите db, hb, bh, dh, bd или hd:")
    print("  db: 10 -> 2\n  hb: 16 -> 2\n  bh: 2 -> 16\n  dh: 10 -> 16\n  bd: 2 -> 10\n  hd: 16 -> 10")

    while True:
        while True:
            choice = input("> ")
            if choice == "db" or choice == "hb" or choice == "bh" or choice == "dh" or choice == "bd" or choice == "hd":
                break

        if choice == "db":
            decimal = int(input("Число: "))
            binary = bin(decimal)[2:]
            print(f"  {decimal} (d) -> {binary} (b)\n")
            print(line2)
        elif choice == "hb":
            num = input("Число: ")
            if is_hex(num):
                decimal = int(num, 16)
            binary = bin(decimal)[2:]
            print(f"  {num} (h) -> {binary} (b)\n")
            print(line2)
        elif choice == "bh":
            num = input("Число: ")
            if is_bin(num):
                decimal = int(num, 2)
            hex_num = hex(decimal)[2:]
            print(f"  {num} (b) -> {hex_num.upper()} (h)\n")
            print(line2)
        elif choice == "dh":
            decimal = int(input("Число: "))
            hex_num = hex(decimal)[2:]
            print(f"  {decimal} (d) -> {hex_num.upper()} (h)\n")
            print(line2)
        elif choice == "bd":
            num = input("Число: ")
            if is_bin(num):
                decimal = int(num, 2)  # 2 указывает на основание, если есть префикс - можно указать 0
                print(f"  {num} (b) -> {decimal} (d)\n")
            else:
                exit()
            print(line2)
        elif choice == "hd":
            num = input("Число: ")
            if is_hex(num):
                decimal = int(num, 16)
                print(f"  {num} (h) -> {decimal} (d)\n")
            else:
                exit()
            print(line2)


if __name__ == "__main__":
    main()