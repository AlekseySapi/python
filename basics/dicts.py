# Словарь - это неупорядоченная изменяемая коллекция пар "ключ-значение".
# Ключи должны быть уникальными и неизменяемыми типами данных.

# Пустой словарь
my_dict = {}

# Словарь с элементами
person = {
    "Имя": "Алексей",
    "Возраст": 30,
    "Город": "Токио"
}

print(person["Имя"])

person["email"] = "altmind92@gmail.com"

del person["Возраст"]


print(person.keys())
print(person.values())

print()
print(person)


person["Возраст"] = 31
print("После обновления возраста:", person)

del person["Город"]
print("После удаления города:", person)

# Вывод текущих ключей и значений
print("Ключи:", person.keys())
print("Значения:", person.values())

print(".............................")
# Перебор и вывод пар "ключ-значение"
print("== Информация обо мне ==")
for key, value in person.items():
    print(f"{key}: {value}")

    