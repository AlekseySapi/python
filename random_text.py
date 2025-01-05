import os
import random

line = '\n======= ======= ======='

eng = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
rus = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'


def random_text(n, alphabet):
    res = []
    for i in range(n):
        res.append(random.choice(alphabet))
    return ''.join(res)


def insert_spaces(text):
    result = []
    char_count = 0
    line_count = 0
    short_line_count = 0
    is_space = False
    is_short_nl = False
    is_nl = False
    min_s_len = 15
    max_s_len = 35
    min_check = 19
    min_len = 35
    max_len = 55


    for char in text:
        result.append(char)
        char_count += 1
        line_count += 1
        short_line_count += 1
        
        if not is_space:
            is_space = True
            rand_space = random.randint(1, 16)
            if rand_space == 1:
                rand_space = random.randint(1, 6)
                if rand_space == 1:
                    rand_space = random.randint(1, 6)
        		
        if not is_short_nl:
            is_short_nl = True
            rand_short_nl = random.randint(min_s_len, max_s_len)
            if rand_short_nl < min_check:
                rand_short_nl = random.randint(min_s_len, max_s_len)
        if not is_nl:
            is_nl = True
            rand_nl = random.randint(min_len, max_len)

        # Случайное добавление пробела
        if char_count == rand_space and is_space:
            result.append(" ")
            char_count = 0
            is_space = False

        # Случайное добавление переноса строки
        if short_line_count == rand_short_nl and is_short_nl:
            result.append(",\n")
            short_line_count = max_len
            line_count = 0
            is_nl = False
        if line_count == rand_nl and is_nl:
            result.append(".\n")
            short_line_count = 0
            line_count = 0
            is_short_nl = False

    return "".join(result)


def main():
    print(line)
    while True:
        file_path = input("# Введите путь к файлу:\n> ").strip()
        if not os.path.exists(file_path):
            print("Файл не найден.")
        else:
            break

    
    lang = int(input("\nКакой алфавит использовать для текста?\n  1 - ENG, 2 - RUS:\n> "))

    if lang == 2:
        alphabet = rus
    else:
        alphabet = eng


    n = int(input("\nКол-во символов в тексте:\n> "))

    text = random_text(n, alphabet)
    text = insert_spaces(text)


    with open(file_path, 'a', encoding='utf-8') as file:
        file.write('\n\n')
        file.write(text)
                    
    print("Текст создан.")



if __name__ == "__main__":
    main()