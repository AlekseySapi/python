from PIL import Image
import numpy as np
import os

line = '\n####### ####### ####### ####### #######'


def xor_img(image_path, key, mode):
    # Открываем изображение
    img = Image.open(image_path)
    
    # Преобразуем изображение в массив numpy
    img_array = np.array(img)

    if img_array.shape[-1] == 4:  # Если есть альфа-канал
        # Разделяем RGB и альфа-канал
        rgb = img_array[..., :3]  # RGB каналы
        alpha = img_array[..., 3]  # Альфа-канал

        # Применяем XOR только к RGB
        encrypted_rgb = rgb ^ key

        # Собираем обратно массив с альфа-каналом
        img_array = np.dstack((encrypted_rgb, alpha))
    else:
        # Если альфа-канала нет, работаем с RGB
        img_array = img_array ^ key

    # Преобразуем обратно в изображение
    result_img = Image.fromarray(img_array.astype('uint8'))

    # Определяем имя выходного файла
    if mode == 'xor':
        output_file = "img_xored" + os.path.splitext(image_path)[1]
    else:
        output_file = "img_original" + os.path.splitext(image_path)[1]

    # Сохраняем файл в исходном формате
    if img.format == "JPEG":
        result_img.save(output_file, format="JPEG", quality=95, optimize=True)
    elif img.format == "PNG":
        result_img.save(output_file, format="PNG", compress_level=6, optimize=True)
    else:
        result_img.save(output_file, format=img.format)
    
    print(f'\nФайл [{output_file}] сохранён успешно.')


def main():
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
            while True:
                format = input('jpg / png: ')
                if format == 'jpg':
                    xor_img("img.jpg", key, 'xor')
                    break
                elif format == 'png':
                    xor_img("img.png", key, 'xor')
                    break
        elif choice == "2":
            while True:
                format = input('jpg / png: ')
                if format == 'jpg':
                    xor_img("img_xored.jpg", key, 'unxor')
                    break
                elif format == 'png':
                    xor_img("img_xored.png", key, 'unxor')
                    break
        print()


if __name__ == "__main__":
    main()