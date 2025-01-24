from PIL import Image
import numpy as np
import os

line = '\n####### ####### ####### ####### #######'


def neg_img(image_path, mode):
    # Открываем изображение
    img = Image.open(image_path)
    
    # Преобразуем изображение в массив numpy
    img_array = np.array(img)
    
    key = 255

    if img_array.shape[-1] == 4:  # Если есть альфа-канал
        # Разделяем RGB и альфа-канал
        rgb = img_array[..., :3]  # RGB каналы
        alpha = img_array[..., 3]  # Альфа-канал

        # Применяем инверсию только к RGB
        rgb = key - rgb

        # Собираем обратно массив с альфа-каналом
        img_array = np.dstack((rgb, alpha))
    else:
        # Если альфа-канала нет, работаем с RGB
        img_array = key - img_array

    # Преобразуем обратно в изображение
    result_img = Image.fromarray(img_array.astype('uint8'))

    # Определяем имя выходного файла
    if mode == 'neg':
        output_file = "img_negative" + os.path.splitext(image_path)[1]
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
        choice = input("  1 - Получить негатив, 2 - Оригинал:\n> ")
        if choice == "1":
            while True:
                format = input('jpg / png: ')
                if format == 'jpg':
                    neg_img("img.jpg", 'neg')
                    break
                elif format == 'png':
                    neg_img("img.png", 'neg')
                    break
        elif choice == "2":
            while True:
                format = input('jpg / png: ')
                if format == 'jpg':
                    neg_img("img_negative.jpg", 'unneg')
                    break
                elif format == 'png':
                    neg_img("img_negative.png", 'unneg')
                    break
        print()


if __name__ == "__main__":
    main()