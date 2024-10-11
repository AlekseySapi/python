# Список с моими любимыми фильмами

favorite_movies = ["Расплата", "Прибытие", "Чудо на Гудзоне"]
print("Исходный список:", favorite_movies)

# Добавление нового фильма
favorite_movies.append("Хранители")
print("После добавления:", favorite_movies)

# Вставка фильма на вторую позицию
favorite_movies.insert(1, "Области тьмы")
print("После вставки:", favorite_movies)

# Удаление фильма
favorite_movies.remove("Чудо на Гудзоне")
print("После удаления:", favorite_movies)


# Длина списка
print("Количество фильмов:", len(favorite_movies))


# Перебор и вывод фильмов
print("Список любимых фильмов:")
for movie in favorite_movies:
    print("-", movie)