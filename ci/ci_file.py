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
    '''
    file = 'img.jpg'
    encrypted_file = 'img_crypted.jpg'
    decrypted_file = 'img_decrypted.jpg'
    '''
    
    file = 'img.png'
    encrypted_file = 'img_crypted.png'
    decrypted_file = 'img_decrypted.png'
    
    '''
    file = 'track.mp3'
    encrypted_file = 'track_crypted.mp3'
    decrypted_file = 'track_decrypted.mp3'
    '''
    '''
    file = 'text.txt'
    encrypted_file = 'text_crypted.txt'
    decrypted_file = 'text_decrypted.txt'
    '''
    while True:
        print(line)
        choice = input("  1 - Зашифровать, 2 - Расшифровать:\n> ")
        if choice == "1" or choice == "2":
            key = 0
            while not (0 < key < 256):
                try:
                    key = int(input("Введите ключ (1-255): "))
                except ValueError:
                    continue

        if choice == "1":
            xor_file(file, encrypted_file, key)
            print("\nЗашифровано.")

        elif choice == "2":
            xor_file(encrypted_file, decrypted_file, key)
            print("\nРасшифровано.")


if __name__ == "__main__":
    main()