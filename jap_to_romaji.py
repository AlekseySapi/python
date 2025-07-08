# Конвертация Кандзи, Хираганы и Катаканы в Ромадзи

line = '\n################# ################# #################'


def main():
    print('\n    === Топ символов японской каны по частоте ===')
    while True:
        print(line)
        file_path = 'w.txt'
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        romaji_text = jap_to_romaji(text)

        with open(file_path, 'a', encoding='utf-8') as file:
            file.write("\n\n\n=== Ромадзи ===\n")
            file.write(romaji_text)

        print("\n\n\n  ✅ Конвертация в ромадзи завершена.\n")
        input()


if __name__ == "__main__":
	main()