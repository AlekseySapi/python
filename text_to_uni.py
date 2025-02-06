import os

line = '\n####### ####### ####### ####### ####### ####### #######'


def text_to_uni(text):
	uni_nums = []
	for char in text:
		char_num = str(ord(char))
		while len(char_num) < 6:
			char_num = '0' + char_num
		uni_nums.append(char_num)
	return ' '.join(uni_nums)

def replace(text):
	res_text = text.replace('00000', 'a')
	res_text = res_text.replace('000010', 'n')  # Новая строка
	res_text = res_text.replace('000032', 's')  # Пробел
	res_text = res_text.replace('00004', 'b')
	res_text = res_text.replace('00005', 'c')
	res_text = res_text.replace('00006', 'd')
	res_text = res_text.replace('00007', 'f')
	res_text = res_text.replace('00008', 'g')
	res_text = res_text.replace('00009', 'h')
	res_text = res_text.replace('0000', 'o')
	res_text = res_text.replace('0001', 'j')
	res_text = res_text.replace('000', 'e')
	res_text = res_text.replace('0018', 'k')
	res_text = res_text.replace('00107', 'x')
	res_text = res_text.replace('00108', 'y')
	res_text = res_text.replace('00109', 'z')
	res_text = res_text.replace('0010', 'p')
	res_text = res_text.replace('0011', 'r')
	res_text = res_text.replace('00', 'i')
	res_text = res_text.replace('127', 'u')
	res_text = res_text.replace('128', 'v')
	res_text = res_text.replace('129', 'w')
	return res_text

def remove(text):
	res_text = text.replace(' ', '')
	return res_text

def with_sp_and_nl(text):
    res_text = remove(text)
    res_text = res_text.replace('000032', '000032 ')
    res_text = res_text.replace('000010', '000010\n')
    res_text = res_text.replace('s', 's ')
    res_text = res_text.replace('n', 'n\n')
    return res_text


def main():
    print(line)
    while True:
        file_path = input("# Введите путь к файлу:\n> ").strip()
        if not os.path.exists(file_path):
            print("Файл не найден.\n")
        else:
            break
    with open(file_path, 'r', encoding='utf-8') as file:
        original_text = file.read()
    while True:
        print(line)
        while True:
            choice = input("  1 - Перевести текст в Юникод, 2 - С доп. сжатием:\n> ")
            if choice == "1" or choice == "2":
                text = original_text
                break
        while True:
            sp_choice = input("   0 - Без пробелов, 1 - С пробелами,\n   2 - С разделением слов и строк:\n>> ")
            if sp_choice == "0" or sp_choice == "1" or sp_choice == "2":
                break
                
        if choice == "1":
            res_text = text_to_uni(text)
            if sp_choice == "2":
                res_text = with_sp_and_nl(res_text)
            elif sp_choice == "0":
                res_text = remove(res_text)
            with open(file_path, 'a', encoding='utf-8') as file:
                file.write("\n\n\n=== Текст переведённый в Юникод ===\n")
                file.write(res_text)
            print("\nПереведено.\n")
        
        elif choice == "2":
            res_text = text_to_uni(text)
            res_text = replace(res_text)
            if sp_choice == "2":
                res_text = with_sp_and_nl(res_text)
            elif sp_choice == "0":
                res_text = remove(res_text)
            with open(file_path, 'a', encoding='utf-8') as file:
                file.write("\n\n\n=== Текст переведённый в Юникод ===\n")
                file.write(res_text)
            print("\nПереведено.\n")


if __name__ == "__main__":
    main()