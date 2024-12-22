# Программа для вывода кодов символов в тексте

while True:
    print("\n=== === ===")
    text = "ABC def,\tghi!?\nxyz..."

    for char in text:
        char_code = ord(char)
        print(f"'{char}' - {char_code}")
    
    input()