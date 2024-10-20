# Программа, которая отправляет GET-запрос к GitHub API и выводит статус ответа


import requests


response = requests.get('https://api.github.com')
if response.status_code == 200:
    print("Успешное соединение с GitHub API!")
else:
    print(f"Ошибка: статус код {response.status_code}")