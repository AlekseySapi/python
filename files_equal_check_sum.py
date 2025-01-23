# Проверка двух файлов на идентичность по их суммам

import os

line = "\n##### ##### ##### ##### #####"


def file_sum(data):
    return sum((num + (i % 10)) * i for i, num in enumerate(data, start=1))


def main():
    while True:
        print(line)
        while True:
            file1 = input("# Введите путь первого файла:\n> ").strip()
            if not os.path.exists(file1):
                print("Файл не найден.\n")
            else:
                break
        with open(file1, 'rb') as infile:
            data1 = infile.read()

        print()
        while True:
            file2 = input("# Введите путь второго файла:\n> ").strip()
            if not os.path.exists(file2):
                print("Файл не найден.\n")
            else:
                break
        with open(file2, 'rb') as infile:
            data2 = infile.read()

        print()
        sum1 = file_sum(data1)
        sum2 = file_sum(data2)
        print(f'Сумма файла 1 = {sum1}')
        print(f'Сумма файла 2 = {sum2}')

        print()
        if sum1 == sum2:
            print("\n>> Файлы одинаковые\n")
        else:
            print("\n>> Файлы отличаются\n")



if __name__ == "__main__":
    main()