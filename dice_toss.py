import random

# Подбрасывание кубика n раз
n = 1000
rolls = [random.randint(1, 6) for _ in range(n)]

# Подсчёт частоты выпадения каждой стороны
roll_counts = {i: rolls.count(i) for i in range(1, 7)}


print(roll_counts)