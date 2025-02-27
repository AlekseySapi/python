import os
from PIL import Image

line = '\n####### ####### ####### ####### #######'
background_color = (0, 0, 0)    # Чёрный фон
q = 90  # Оптимальное качество


def optimize_jpg(input_file, output_file, q):
    with Image.open(input_file) as img:
        # Если есть прозрачность (RGBA или LA), то заменяем её на чёрный фон
        if img.mode in ("RGBA", "LA"):
            background = Image.new("RGB", img.size, background_color)
            img = img.convert("RGBA")  # Обязательно конвертируем перед композитингом
            background.paste(img, mask=img.split()[3])  # Используем альфа-канал как маску
            img = background
        else:
            img = img.convert("RGB")  # Если альфа-канала нет, просто конвертируем

        img.save(output_file, "JPEG", quality=q, optimize=True)

def optimize_jpg_to_720p(input_file, output_file, q):
    with Image.open(input_file) as img:
        # Если есть прозрачность (RGBA или LA), то заменяем её на чёрный фон
        if img.mode in ("RGBA", "LA"):
            background = Image.new("RGB", img.size, background_color)
            img = img.convert("RGBA")  # Обязательно конвертируем перед композитингом
            background.paste(img, mask=img.split()[3])  # Используем альфа-канал как маску
            img = background
        else:
            img = img.convert("RGB")  # Если альфа-канала нет, просто конвертируем
        dim = (1280, 720)
        img = img.resize(dim)

        img.save(output_file, "JPEG", quality=q, optimize=True)


def main():
    print(line)
    print(" < Оптимизация изображения >\n Форматы PNG и WebP переводятся в JPEG\n")
    while True:
        print(line)
        while True:
            file = input("# Введите имя файла:\n> ")
            if not os.path.isfile(file):
                print("Файл не найден.\n")
            else:
                break

        filename, ext = os.path.splitext(file)
        if ext.lower() not in ('.jpg', '.jpeg', '.png', '.webp'):
            print("\n⚠️  Ошибка: Неверный формат файла.")
            continue
        output_file = f"{filename}_pil.jpg"
        
        choice = ''
        while choice not in ('1', '2'):
            choice = input("\n  1 - Pillow, 2 - Pillow + >> 720p\n> ")
        if choice.lower() == '1':
            optimize_jpg(file, output_file, q)
        else:
            optimize_jpg_to_720p(file, output_file, q)
        
        print(f"\n✅ Файл оптимизирован и сохранён: {output_file}\n")


if __name__ == "__main__":
    main()