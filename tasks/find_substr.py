def find_substring(haystack, needle):
    """
    Поиск первого вхождения подстроки в строку.
    
    :param haystack: строка, где нужно искать
    :param needle: подстрока, которую ищем
    :return: индекс первого вхождения или -1
    """
    # TODO: Реализовать логику поиска
    pass

# Примеры вызовов:
print(find_substring("hello", "ll"))  # 2
print(find_substring("aaaaa", "bba"))  # -1
print(find_substring("", ""))  # 0
print(find_substring("abc", ""))  # 0
print(find_substring("", "a"))  # -1