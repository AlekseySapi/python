import random

# Подбрасывание монеты n раз
n = 1000
flips = [random.choice(['Орёл', 'Решка']) for _ in range(n)]

# Подсчёт частоты
heads_count = flips.count('Орёл')
tails_count = flips.count('Решка')


print(f"Орёл - {heads_count}")
print(f"Решка - {tails_count}")