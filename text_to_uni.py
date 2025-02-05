import os

line = '\n####### ####### ####### ####### #######'


def text_to_uni(text):
	uni_nums = []
	for char in text:
		char_num = str(ord(char))
		while len(char_num) < 6:
			char_num = '0' + char_num
		uni_nums.append(char_num)
	return ' '.join(uni_nums)


def main():
    while True:
        file_path = input("# Введите путь к файлу:\n> ").strip()
        if not os.path.exists(file_path):
            print("Файл не найден.")
        else:
            break
    with open(file_path, 'r', encoding='utf-8') as file:
        original_text = file.read()
    while True:
        print(line)
        while True:
            choice = input("  1 - Перевести текст в Юникод:\n> ")
            if choice == "1":
                text = original_text
                break
                
        if choice == "1":
            with open(file_path, 'a', encoding='utf-8') as file:
                file.write("\n\n\n=== Текст переведённый в Юникод ===\n")
                file.write(text_to_uni(text))
            print("\nПереведено.\n")


if __name__ == "__main__":
    main()