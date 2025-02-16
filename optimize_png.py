import os
from PIL import Image
import subprocess

line = '\n####### ####### ####### ####### #######'


def optimize_png_pillow(input_file, output_file):
    with Image.open(input_file) as img:
        img.save(output_file, format="PNG", optimize=True)
    with Image.open(input_file) as img:
        if img.format == "JPEG":
            img = img.convert("RGB")
        elif img.format == "WEBP":
            img = img.convert("RGBA" if "A" in img.mode else "RGB")  # Сохраняем альфа-канал, если есть
        img.save(output_file, format="PNG", optimize=True)

def optimize_png_opti(input_file, output_file, o):
    with Image.open(input_file) as img:
        if img.format == "JPEG":
            img = img.convert("RGB")
        elif img.format == "WEBP":
            img = img.convert("RGBA" if "A" in img.mode else "RGB")
        img.save(output_file, format="PNG")
        input_file = output_file
    subprocess.run(["optipng", o, input_file, "-out", output_file], check=True)


def main():
    print(line)
    print(" < Оптимизация изображения >\n Форматы JPEG и WebP переводятся в PNG\n")
    while True:
        print(line)
        while True:
            file = input("# Введите имя PNG-файла:\n> ")
            if not os.path.isfile(file):
                print("Файл не найден.\n")
            else:
                break

        filename, ext = os.path.splitext(file)
        if ext.lower() not in ('.jpg', '.jpeg', '.png', '.webp'):
            print("\n⚠️  Ошибка: Неверный формат файла.")
            continue

        choice = ''
        while choice not in ('1', '2'):
            choice = input("\n  1 - Pillow, 2 - OptiPNG:\n> ")
        if choice == '1':
            output_file = f"{filename}_pil.png"
            optimize_png_pillow(file, output_file)
        elif choice == '2':
            output_file = f"{filename}_opt.png"
            optimize_png_opti(file, output_file, "-o2")
        print(f"\n✅ Файл оптимизирован и сохранён: {output_file}\n")


if __name__ == "__main__":
    main()