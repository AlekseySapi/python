# Проверка двух файлов на идентичность побайтово

import os

line = "\n##### ##### ##### ##### #####"


def are_files_equal(file1, file2):
    with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
        while True:
            chunk1 = f1.read(4096)  # Читаем кусками по 4КБ
            chunk2 = f2.read(4096)
            if chunk1 != chunk2:
                return False  # Содержимое отличается
            if not chunk1:  # Дошли до конца обоих файлов
                return True


def main():
    while True:
        print(line)
        while True:
            file1 = input("# Введите путь первого файла:\n> ").strip()
            if not os.path.exists(file1):
                print("Файл не найден.\n")
            else:
                break

        print()
        while True:
            file2 = input("# Введите путь второго файла:\n> ").strip()
            if not os.path.exists(file2):
                print("Файл не найден.\n")
            else:
                break

        print()
        if are_files_equal(file1, file2):
            print("\n>> Файлы одинаковые\n")
        else:
            print("\n>> Файлы отличаются\n")



if __name__ == "__main__":
    main()