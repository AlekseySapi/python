import os
from PIL import Image
import numpy as np

line = '\n####### ####### ####### ####### #######'
background_color = (0, 0, 0)
key = 16    # Искажающий ключ для XOR
q = 8       # Качество сжатия


def shakal_jpg(image_path, output_file):
    img = Image.open(image_path)
    # Если есть прозрачность (RGBA или LA), то заменяем её на чёрный фон
    if img.mode in ("RGBA", "LA"):
        background = Image.new("RGB", img.size, background_color)
        img = img.convert("RGBA")  # Обязательно конвертируем перед композитингом
        background.paste(img, mask=img.split()[3])  # Используем альфа-канал как маску
        img = background
    else:
        img = img.convert("RGB")  # Если альфа-канала нет, просто конвертируем
    # Преобразуем изображение в массив numpy
    img_array = np.array(img)

    # XOR
    img_array = img_array ^ key

    # Преобразуем обратно в изображение
    result_img = Image.fromarray(img_array.astype('uint8'))
    result_img.save(output_file, format="JPEG", quality=q, optimize=True)


def main():
    print(line)
    print(' < Для "шакализации" в формат JPEG >\n    < доступны также PNG и WebP >\n')
    while True:
        print(line)
        while True:
            file = input("# Введите имя картинки:\n> ")
            if not os.path.isfile(file):
                print("Файл не найден.\n")
            else:
                break

        filename, ext = os.path.splitext(file)
        if ext.lower() not in ('.jpg', '.jpeg', '.png', '.webp'):
            print("\n⚠️  Ошибка: Неверный формат файла.")
            continue

        output_file = f"{filename}_shkl.jpg"
        shakal_jpg(file, output_file)
        print(f'\n✅ Картинка "зашакалена" и сохранена: {output_file}\n')


if __name__ == "__main__":
    main()