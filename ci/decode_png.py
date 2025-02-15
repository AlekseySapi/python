import os
from PIL import Image

line = '\n################# ################# ################# #################'
line2 = '\n################# ################# #################'
stop_symb = '00000000'  # Стоп-символ


def decode_text_from_png(input_file, text_file, choice):
    img = Image.open(input_file)
    pixels = img.load()

    width, height = img.size
    binary_text = ""

    if choice == '1':
        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y] if img.mode == 'RGB' else pixels[x, y][:3]
                binary_text += str(r & 1) + str(g & 1) + str(b & 1)
    elif choice == '2':
        for y in range(height):
            for x in range(width - 1, -1, -1):
                r, g, b = pixels[x, y] if img.mode == 'RGB' else pixels[x, y][:3]
                binary_text += str(r & 1) + str(g & 1) + str(b & 1)
    elif choice == '3':
        for y in range(height - 1, -1, -1):
            for x in range(width):
                r, g, b = pixels[x, y] if img.mode == 'RGB' else pixels[x, y][:3]
                binary_text += str(r & 1) + str(g & 1) + str(b & 1)
    elif choice == '4':
        for y in range(height - 1, -1, -1):
            for x in range(width - 1, -1, -1):
                r, g, b = pixels[x, y] if img.mode == 'RGB' else pixels[x, y][:3]
                binary_text += str(r & 1) + str(g & 1) + str(b & 1)
    elif choice == '5':
        for x in range(width):  
            for y in range(height):
                r, g, b = pixels[x, y] if img.mode == 'RGB' else pixels[x, y][:3]
                binary_text += str(r & 1) + str(g & 1) + str(b & 1)
    elif choice == '6':
        for x in range(width):  
            for y in range(height - 1, -1, -1):
                r, g, b = pixels[x, y] if img.mode == 'RGB' else pixels[x, y][:3]
                binary_text += str(r & 1) + str(g & 1) + str(b & 1)
    elif choice == '7':
        for x in range(width - 1, -1, -1):  
            for y in range(height):
                r, g, b = pixels[x, y] if img.mode == 'RGB' else pixels[x, y][:3]
                binary_text += str(r & 1) + str(g & 1) + str(b & 1)
    elif choice == '8':
        for x in range(width - 1, -1, -1):  
            for y in range(height - 1, -1, -1):
                r, g, b = pixels[x, y] if img.mode == 'RGB' else pixels[x, y][:3]
                binary_text += str(r & 1) + str(g & 1) + str(b & 1)

    byte_array = []
    for i in range(0, len(binary_text), 8):
        byte = binary_text[i:i+8]
        if byte == stop_symb:   # Стоп-символ
            break
        byte_array.append(int(byte, 2))

    try:
        secret_text = bytes(byte_array).decode('utf-8')  # Декодируем обратно в строку
        with open(text_file, 'a', encoding='utf-8') as file:
            # file.write("\n\n\n======= ======= =======\n")
            file.write(secret_text)
        print("\n🔍 Текст найден и записан в файл!\n")
        print(line2)
    except UnicodeDecodeError:
        print("\n⚠️  Текст не найден.\n")


def main():
    print(line)
    print(" < 8 вариантов обхода пикселей изображения >\n\n [1] ➡️  ⬇️    | [2] ⬅️  ⬇️    | [3] ➡️  ⬆️    | [4] ⬅️  ⬆️    - по строкам\n [5] ⬇️  ➡️    | [6] ⬆️  ➡️    | [7] ⬇️  ⬅️    | [8] ⬆️  ⬅️    - по столбцам\n")
    while True:
        print(line2)
        while True:
            file = input("# Введите имя PNG-файла:\n> ")
            if not os.path.isfile(file):
                print("Файл не найден.\n")
            else:
                break

        filename, ext = os.path.splitext(file)
        if ext.lower() != ".png":
            print("\n⚠️  Ошибка: Поддерживаются только PNG-файлы.")
            continue
        
        print()
        while True:
            text_file = input("# Введите имя файла для результата:\n> ")
            if not os.path.isfile(text_file):
                with open(text_file, 'w') as f:
                    pass
                break
            else:
                break

        while True:
            choice = ''
            while choice not in ('q', '1', '2', '3', '4', '5', '6', '7', '8'):
                choice = input("\n  < Обход >  [ q - Читать новый файл ]\n  1 - ➡️  ⬇️    2 - ⬅️  ⬇️    3 - ➡️  ⬆️    4 - ⬅️  ⬆️\n  5 - ⬇️  ➡️    6 - ⬆️  ➡️    7 - ⬇️  ⬅️    8 - ⬆️  ⬅️\n> ")
            if choice == 'q':
                print()
                break
            decode_text_from_png(file, text_file, choice)


if __name__ == "__main__":
    main()