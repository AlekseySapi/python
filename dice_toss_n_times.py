import random

# Подбрасывание кубика n раз
n = 1000


while True:
    user_input = input("Введите y/Y: ")
    if(user_input == "y" or user_input == "Y"):

        rolls = [random.randint(1, 6) for _ in range(n)]

        # Подсчёт частоты выпадения каждой стороны
        roll_counts = {i: rolls.count(i) for i in range(1, 7)}

        print("\n=== Результаты подбрасывания кубика ===")
        for side, count in roll_counts.items():
            print(f"Грань {side}: {count} раз(а) ({int((count / n) * 100)}%)")
        print("=== === === === === === === === === ===\n")