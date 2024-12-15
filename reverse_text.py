import os

def reverse_text(text):
    res = text[::-1]
    return res

def main():
    while True:
        file_path = input("# Введите путь к файлу:\n> ").strip()
        if not os.path.exists(file_path):
            print("Файл не найден.")
        else:
            break

    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    reversed_text = reverse_text(text)

    with open(file_path, 'a', encoding='utf-8') as file:
        file.write("\n\n=== Перевёрнутый текст ===\n")
        file.write(reversed_text)

    print("Текст перевёрнут.")


if __name__ == "__main__":
    main()