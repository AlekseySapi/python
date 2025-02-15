import os
from PIL import Image

line = '\n####### ####### ####### ####### #######'
stop_symb = '00000000'


def encode_text_in_png(input_file, output_file, secret_text):
    binary_text = ''.join(format(byte, '08b') for byte in secret_text.encode('utf-8')) + stop_symb  # Стоп-символ

    img = Image.open(input_file)
    pixels = img.load()
    width, height = img.size
    data_index = 0

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y] if img.mode == 'RGB' else pixels[x, y][:3]  # Извлекаем только RGB каналы

            # Кодируем текст в LSB каналов
            if data_index < len(binary_text):
                r = (r & 0b11111110) | int(binary_text[data_index])  # Кодируем бит в LSB
                data_index += 1
            if data_index < len(binary_text):
                g = (g & 0b11111110) | int(binary_text[data_index])
                data_index += 1
            if data_index < len(binary_text):
                b = (b & 0b11111110) | int(binary_text[data_index])
                data_index += 1

            # Возвращаем в пиксель
            if img.mode == 'RGBA':
                a = pixels[x, y][3]  # Если есть альфа, оставляем её без изменений
                pixels[x, y] = (r, g, b, a)
            else:
                pixels[x, y] = (r, g, b)  # Для RGB

            if data_index >= len(binary_text):
                break
        if data_index >= len(binary_text):
            break

    img.save(output_file)
    print("\n✅ Информация скрыта в файле:", output_file)
    print()


def decode_text_from_png(input_file):
    img = Image.open(input_file)
    pixels = img.load()

    width, height = img.size
    binary_text = ''

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y] if img.mode == 'RGB' else pixels[x, y][:3]  # Извлекаем только RGB каналы

            # Извлекаем данные из младших битов
            binary_text += str(r & 1)  # Читаем младший бит красного канала
            binary_text += str(g & 1)  # Читаем младший бит зелёного канала
            binary_text += str(b & 1)  # Читаем младший бит синего канала

    byte_array = []
    for i in range(0, len(binary_text), 8):
        byte = binary_text[i:i+8]
        if byte == stop_symb:  # Стоп-символ
            break
        byte_array.append(int(byte, 2))

    try:
        secret_text = bytes(byte_array).decode('utf-8')  # Декодируем обратно в строку
        print(f"\n🔍 Сообщение найдено:\n\n  {secret_text}")
    except UnicodeDecodeError:
        print("\n⚠️  Сообщение не найдено.")


def main():
    while True:
        print(line)
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

        choice = ''
        while choice not in ('1', '2'):
            choice = input("\n  1 - Спрятать текст, 2 - Извлечь текст:\n> ")

        if choice == '1':
            text = input("\nВведите скрытое сообщение:\n> ")
            output_file = f"{filename}_hidden.png"
            encode_text_in_png(file, output_file, text)
        else:
            decode_text_from_png(file)


if __name__ == "__main__":
    main()