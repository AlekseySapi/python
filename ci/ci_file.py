import os

line = '\n####### ####### ####### ####### #######'


def xor_file(input_file, output_file, key):
    # Читаем файл побайтово
    with open(input_file, 'rb') as infile:
        data = infile.read()

    key_bytes = key.encode()  # Преобразование строкового ключа в байты
    print(list(key_bytes))
    key_length = len(key_bytes)

    # XOR на каждый байт файла циклично по байтам ключа
    encrypted_data = bytes([data[i] ^ key_bytes[i % key_length] for i in range(len(data))])

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
            key = input("key = ") or ' '

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