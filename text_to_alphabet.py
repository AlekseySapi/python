import os


def get_alphabet(text):
    unique_chars = {}
    for char in text:
       unique_chars[char] = None
    sorted_chars = sorted(unique_chars.keys())
    return "".join(sorted_chars)
    
    
def remove_spaces(text):
    return text.replace(" ", "").replace("\n", "")


def main():
    while True:
        file_path = input("# Введите путь к файлу:\n> ").strip()
        if not os.path.exists(file_path):
            print("Файл не найден.")
        else:
            break

    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    alphabet = get_alphabet(remove_spaces(text))

    with open(file_path, 'a', encoding='utf-8') as file:
        file.write("\n\n=== Алфавит этого текста ===\n")
        file.write(f'"{alphabet}"')
        file.write(f"\n\n> {len(alphabet)}")

    print("Алфавит составлен.")


if __name__ == "__main__":
    main()