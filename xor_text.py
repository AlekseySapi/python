import os

line = '\n======= ======= ======='


def xor(text, key):
    i = 0
    res = []
    for char in text:
       char_code = ord(char)
       key_code = ord(key[i % len(key)])
       xored_code = char_code ^ key_code
       res.append(chr(xored_code))
       i += 1
    return "".join(res)


def main():
    while True:
        print(line)
        file_path = input("# Введите путь к файлу:\n> ").strip()
        if not os.path.exists(file_path):
            print("Файл не найден.")
        else:
            break

    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        
    # key = input("key = ")
    key = '1234'

    xored_text = xor(text, key)

    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(f"\n\n=== XOR с ключём {key} ===\n")
        file.write(xored_text)

    print("Результат записан в файл.\n")


if __name__ == "__main__":
    main()