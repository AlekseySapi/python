import os
# import pyperclip

line = '\n####### ####### #######'


def main():
    while True:
        print(line)
        file_path = input("# Введите путь к файлу:\n> ").strip()
        if not os.path.exists(file_path):
            print("Файл не найден.")
        else:
            break

    chars = []
    char = 'ꀀ'  # Первый символ
    char_ord = ord(char)
    n = 1160  # Количество символов
    i = 0
    for c in range(char_ord, char_ord + n):
        chars.append(chr(c))
        chars.append(' ')
        i += 1
        if (i % 20) == 0:
            chars.append('\n')

    chars_str = ''.join(chars)


    with open(file_path, 'a', encoding='utf-8') as file:
        file.write("\n\n\n========= ======= ======= ======= =========\n")
        file.write(f"{chars_str}")

    print("Символы записаны в файл.")

    # pyperclip.copy(chars_str)
    # print("\n>> Символы скопированы в буфер обмена.\n")

    print(line)


if __name__ == "__main__":
    main()