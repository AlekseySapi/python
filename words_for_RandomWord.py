# Программа для составления списков уникальных слов (-> RandomWord)

import re


def get_words(input_text):

    unique_words = set(re.findall(r'\b\w+\b', input_text.lower()))

    sorted_words = sorted(unique_words)


    w = 10      # Кол-во слов в строке
    formatted_output = ""
    for i in range(0, len(sorted_words), w):
        line = ", ".join([f'"{word}"' for word in sorted_words[i:i+w]])
        formatted_output += line + ",\n"


    return formatted_output.rstrip(",\n")



def main():

    while True:

        file_path = input("Введите путь к текстовому файлу: ")

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
        except FileNotFoundError:
            print("Файл не найден. Проверьте путь и попробуйте снова.")
            continue
        except Exception as e:
            print(f"Произошла ошибка при чтении файла: {e}")
            return



        words = get_words(text)


        try:
            with open(file_path, 'a', encoding='utf-8') as file:  # Открываем файл в режиме "дополнения"
                file.write("\n=== === ===\n")
                file.write(words + "\n")
                print("Слова успешно добавлены в файл.")
                print("\n=== === ===")
        except Exception as e:
            print(f"Произошла ошибка при записи файла: {e}")
            return

        


if __name__ == "__main__":
    main()