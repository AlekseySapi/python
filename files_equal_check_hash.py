# Сравнение двух файлов по хэш-сумме

import os
import hashlib

line = "\n##### ##### ##### ##### #####"


def file_checksum(file_path):
    hash_obj = hashlib.sha256()  # SHA-256 лучше, чем MD5 и SHA-1
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):  # Читаем файл кусками
            hash_obj.update(chunk)
    return hash_obj.hexdigest()

def are_files_equal(file1, file2):
    return file_checksum(file1) == file_checksum(file2)


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
        sum1 = file_checksum(file1)
        sum2 = file_checksum(file2)
        print(f'Сумма файла 1 = {sum1}')
        print(f'Сумма файла 2 = {sum2}')

        print()
        if are_files_equal(file1, file2):
            print("\n>> Файлы одинаковые\n")
        else:
            print("\n>> Файлы отличаются\n")



if __name__ == "__main__":
    main()