import random

# Подбрасывание монеты n раз
n = 1000

while True:
    while True:
        user_input = input("Введите y/Y: ")
        if(user_input == "y" or user_input == "Y"):

            flips = [random.choice(['Орёл', 'Решка']) for _ in range(n)]

            # Подсчёт частоты
            heads_count = flips.count('Орёл')
            tails_count = flips.count('Решка')

            print("\n=== Результаты подбрасывания монеты ===")
            print(f"Орёл  - {heads_count} раз(а) ({int((heads_count / n) * 100)}%)")
            print(f"Решка - {tails_count} раз(а) ({int((tails_count / n) * 100)}%)")
            print("=== === === === === === === === === ===\n")