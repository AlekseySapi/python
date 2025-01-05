import os
import random

line = '\n======= ======= ======='


def clear_text(text):
    return text.replace(" ", "").replace(",", "").replace(".", "").replace("\n", "")


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

    cleared_text = clear_text(text)


    with open(file_path, 'a', encoding='utf-8') as file:
        file.write('\n\n')
        file.write(cleared_text)
                    
    print("Текст очищен.")



if __name__ == "__main__":
    main()