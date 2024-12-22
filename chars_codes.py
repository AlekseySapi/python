# Программа для вывода кодов символов в тексте

while True:
    print("\n=== === ===")
    text = "ABC def,\tghi!?\nxyz..."

    for char in text:
        char_code = ord(char)
        print(f"'{char}' - {char_code}")

    # Перевод кодов пробела, табуляции и новой строки в символы
    space_char_code = 32    # 0b100000
    t_char_code = 9         # 0b1001
    n_char_code = 10        # 0b1010

    print("\n=== === ===")
    print(f"Пробел - '{chr(space_char_code)}'")
    print(f"Табуляция - '{chr(t_char_code)}'")
    print(f"Перенос строки - '{chr(n_char_code)}'")

    
    input()