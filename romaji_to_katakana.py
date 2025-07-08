# Конвертация Ромадзи в Катакану

line = '\n################# ################# #################'


def main():
    print('\n    === Топ символов японской каны по частоте ===')
    while True:
        print(line)
        file_path = 'w.txt'
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        katakana_text = romaji_to_katakana(text)

        with open(file_path, 'a', encoding='utf-8') as file:
            file.write("\n\n\n=== Катакана ===\n")
            file.write(katakana_text)

        print("\n\n\n  ✅ Конвертация в катакану завершена.\n")
        input()


if __name__ == "__main__":
	main()