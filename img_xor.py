from PIL import Image
import numpy as np
import os

line = '\n############### ############### ###############'


def xor_img(input_file, output_file, key):
    # Открываем изображение
    img = Image.open(input_file)
    
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

    # Сохраняем файл в исходном формате
    if img.format == "JPEG":
        result_img.save(output_file, format="JPEG", quality=90, optimize=True)
    elif img.format == "PNG":
        result_img.save(output_file, format="PNG", compress_level=6, optimize=True)
    else:
        result_img.save(output_file, format=img.format)
    
    print(f'\n\n✅ Файл [{output_file}] успешно сохранён.\n')


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
        if ext.lower() not in ('.jpg', '.jpeg', '.png'):
            print("\n⚠️  Ошибка: Неверный формат файла.\n")
            continue
        output_file = f"{filename}_xor{ext}"

        key = 0
        while not (0 < key < 256):
            try:
                key = int(input("\nВведите ключ (1-255): "))
            except ValueError:
                continue

        xor_img(file, output_file, key)


if __name__ == "__main__":
    main()