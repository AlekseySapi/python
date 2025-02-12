import os

line = '\n####### ####### ####### ####### #######'


def xor_file(input_file, output_file, key):
    # Читаем файл побайтово
    with open(input_file, 'rb') as infile:
        data = infile.read()

    # Применяем XOR на каждый байт (ключ  -->  1-255)
    encrypted_data = bytes([b ^ key for b in data])

    # Сохраняем результат
    with open(output_file, 'wb') as outfile:
        outfile.write(encrypted_data)


def main():
    while True:
        print(line)
        while True:
            file = input("# Введите имя файла:\n> ")
            if not os.path.isfile(file):
                print("Файл не найден.\n")
            else:
                break
        
        filename, ext = os.path.splitext(file)

        choice = input("  1 - Зашифровать, 2 - Расшифровать:\n> ")
        if choice in ('1', '2'):
            key = 0
            while not (0 < key < 256):
                try:
                    key = int(input("Введите ключ (1-255): "))
                except ValueError:
                    continue

        if choice == '1':
            output_file = f"{filename}_crypted{ext}"
            xor_file(file, output_file, key)
            print("\nЗашифровано.")
        else:
            output_file = f"{filename}_decrypted{ext}"
            xor_file(file, output_file, key)
            print("\nРасшифровано.")


if __name__ == "__main__":
    main()