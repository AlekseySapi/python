import os
import random

line = '\n======= ======= ======='


def shuffle(text):
    chars_list = list(text)
    random.shuffle(chars_list)
    return ''.join(chars_list)


def main():
    print(line)
    while True:
        file_path = input("# Введите путь к файлу:\n> ").strip()
        if not os.path.exists(file_path):
            print("Файл не найден.")
        else:
            break

    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()


    with open(file_path, 'a', encoding='utf-8') as file:
        file.write("\n\n\n=== Перемешанный текст ===\n")
        for i in range (10):
            file.write(f"\n{i} > {shuffle(text)}")
                    
    print("Текст перемешан.")



if __name__ == "__main__":
    main()