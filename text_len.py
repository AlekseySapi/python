import os
import random

line = '\n======= ======= ======='


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


    print(f"\nДлина текста:\n> {len(text)}\n")


if __name__ == "__main__":
    main()