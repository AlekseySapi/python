import os
from collections import Counter

line = '\n======= ======= ======='

eng_top_1 = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'H', 'R', 'D', 'L', 'U', 'C', 'M', 'F']
eng_top_2 = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'H', 'R', 'D', 'L', 'U', 'W', 'C', 'M']
eng_top_3 = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'U', 'G', 'Y', 'W']
rus_top_1 = ['О', 'Е', 'А', 'И', 'Н', 'Т', 'С', 'Р', 'В', 'Л', 'К', 'М', 'Д', 'П', 'У']
rus_top_2 = ['О', 'А', 'Е', 'И', 'Н', 'Т', 'Л', 'С', 'Р', 'В', 'М', 'К', 'Д', 'П', 'У']
rus_top_3 = ['О', 'А', 'Е', 'И', 'Н', 'Т', 'Л', 'Р', 'С', 'В', 'К', 'М', 'Д', 'П', 'У']
rus_top_4 = ['О', 'А', 'Е', 'Т', 'И', 'Н', 'К', 'Р', 'С', 'Д', 'Л', 'В', 'П', 'У', 'М']

top_lists = [eng_top_1, eng_top_2, rus_top_1, rus_top_2, rus_top_3, rus_top_4]


def replace_chars_by_frequency(text, mapping):
    replaced_text = []
    for char in text:
        replaced_text.append(mapping.get(char.upper(), char))
    return ''.join(replaced_text)



def main():
    print(line)
    while True:
        file_path = input("Введите путь к файлу:\n> ").strip()
        if not os.path.exists(file_path):
            print("Файл не найден.")
        else:
            break

    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()


    # Подсчитываем частоту каждой буквы
    chars_counts = Counter(char.upper() for char in text if char.strip())

    # Получаем топ самых частых букв
    n = 15
    top_chars = chars_counts.most_common(n)


    with open(file_path, 'a', encoding='utf-8') as file:
        file.write("\n\n\n===== РЕЗУЛЬТАТЫ ЗАМЕН =====\n")
        
        for i, top in enumerate(top_lists, start=1):
            # Создаем словарь для текущего топа
            mapping = {char: top[i] for i, (char, _) in enumerate(top_chars) if i < len(top)}
            
            # Преобразуем текст с текущей заменой
            replaced_text = replace_chars_by_frequency(text, mapping)
            
            # Пишем результат в файл с заголовком
            file.write(f"\n===== Вариант {i} =====\n")
            file.write(f"Топ исходного текста:\n {[char for char, _ in top_chars]}\n")
            file.write(f"Меняем на эти буквы:\n {top}\n\n")
            file.write(replaced_text)
            file.write("\n\n")
        
        print("Результат добавлен в файл.")
        print(line)


if __name__ == "__main__":
    main()