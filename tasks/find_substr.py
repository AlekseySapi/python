def find_substring(haystack, needle):
    """
    Поиск первого вхождения подстроки в строку.
    
    :param haystack: строка, где нужно искать
    :param needle: подстрока, которую ищем
    :return: индекс первого вхождения или -1
    """
    # TODO: Реализовать логику поиска
    # pass
    if needle == "":
        return 0
    
    n, m = len(haystack), len(needle)
    
    for i in range(n - m + 1):  # Идём по строке с учётом длины подстроки
        if haystack[i:i + m] == needle:  # Сравниваем срез строки с подстрокой
            return i
    
    return -1  # Если ничего не нашли, возвращаем -1
                

# Примеры вызовов:
print(find_substring("hello", "ll"))  # 2
print(find_substring("aaaaa", "bba"))  # -1
print(find_substring("", ""))  # 0
print(find_substring("abc", ""))  # 0
print(find_substring("", "a"))  # -1