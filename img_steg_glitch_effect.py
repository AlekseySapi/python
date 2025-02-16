import os
import random
from PIL import Image

line = '\n####### ####### ####### ####### #######'
alphabet = '0123456789ABCDEFGHIJKL!#%&*+АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
#           0123456789ABCDEFGHIJKL!#%&*+АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя


def distort_image(input_file, output_file):
    img = Image.open(input_file)
    pixels = img.load()
    width, height = img.size

    num_symbols = width * height
    random_text = ''.join(random.choice(alphabet) for _ in range(num_symbols))
    binary_text = ''.join(format(byte, '08b') for byte in random_text.encode('utf-8'))

    max_length = width * height * 3
    binary_text = binary_text[:max_length]

    data_index = 0
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y] if img.mode == 'RGB' else pixels[x, y][:3]  # Извлекаем только RGB каналы

            # Кодируем текст в LSB каналов
            if data_index < len(binary_text):
                r = (r & 0b11011111) | (int(binary_text[data_index]) << 5)
                data_index += 1
            if data_index < len(binary_text):
                g = (g & 0b11011111) | (int(binary_text[data_index]) << 5)
                data_index += 1
            if data_index < len(binary_text):
                b = (b & 0b11011111) | (int(binary_text[data_index]) << 5)
                data_index += 1

            # Возвращаем в пиксель
            if img.mode == 'RGBA':
                a = pixels[x, y][3]  # Если есть альфа, оставляем её без изменений
                pixels[x, y] = (r, g, b, a)
            else:
                pixels[x, y] = (r, g, b)  # Для RGB
    
    img.save(output_file)
    print(f"\n✅ Изображение искажено и сохранено: {output_file}\n")


def main():
    while True:
        print(line)
        file = input("# Введите имя файла:\n> ")
        if not os.path.isfile(file):
            print("Файл не найден.\n")
            continue
        
        filename, ext = os.path.splitext(file)
        output_file = f"{filename}_steg{ext}"
        distort_image(file, output_file)


if __name__ == "__main__":
    main()