# Изучаю работу с файлами


# Контекстный менеджер (with) автоматически закрывает файл после выполнения блока кода
# Это предотвращает утечки ресурсов

with open('example.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    print(text)

# Запись данных в файл
with open('example.txt', 'w', encoding='utf-8') as file:
    file.write("Привет, мир!\n")
    file.write("Это пример записи в файл.")

# Добавление данных в конец файла
with open('example.txt', 'a', encoding='utf-8') as file:
    file.write("\nДобавленная строка.")