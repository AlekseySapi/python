# Программа для перевода чисел из десятичных в двоичные и назад

while True:
    print("=== === === === ===")
    while True:
        choice = input("Введите 1 или 2\n  1 -> Из 10 в 2\n  2 -> Из 2 в 10\n> ")
        if choice == "1" or choice == "2":
            break

    if choice == "1":
        decimal = int(input("Число: "))
        binary = bin(decimal)[2:]
        print(f"{decimal} -> {binary}\n")
    elif choice == "2":
        binary = input("Двоичное число: ")
        decimal = int(binary, 2)  # 2 указывает на основание, если есть префикс, можно указать 0
        print(f"  {binary} -> {decimal}\n")