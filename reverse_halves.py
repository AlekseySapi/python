import os

line = '\n======= ======= ======='


def reverse_halves_in_text(text):
    def reverse_halves(s):
        n = len(s)  # Длина строки
        mid = n // 2  # Середина строки

        if n % 2 == 0:
            # Чётное количество символов
            left_half = s[:mid]
            right_half = s[mid:]
            return right_half + left_half
        else:
            # Нечётное количество символов
            left_half = s[:mid]
            middle = s[mid]
            right_half = s[mid+1:]
            return right_half + middle + left_half

    # Обрабатываем текст по строкам
    lines = text.splitlines()  # Разделяем текст на строки
    result_lines = [reverse_halves(line) for line in lines]  # Обрабатываем каждую строку
    return "\n".join(result_lines)  # Соединяем обратно в текст с переводами строк


def main():
    print(line)
    while True:
        file_path = input("# Введите путь к файлу:\n> ").strip()
        if not os.path.exists(file_path):
            print("Файл не найден.")
        else:
            break

    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    reversed_halves = reverse_halves_in_text(text)


    with open(file_path, 'a', encoding='utf-8') as file:
                file.write("\n\n=== Перемешанный текст ===\n")
                file.write(reversed_halves)

    print("Текст перемешан.")



if __name__ == "__main__":
    main()