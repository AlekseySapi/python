def two_sum(nums, target):
    # TODO: Определить два числа, которые в сумме дают второе
    # pass
    # Создаем словарь для хранения чисел и их индексов
    seen = {}
    for i, num in enumerate(nums):
        num_2 = target - num
        # Если дополнение уже есть в словаре, возвращаем индексы
        if num_2 in seen:
            return [seen[num_2], i]
        # Иначе добавляем текущее число в словарь
        seen[num] = i

# Примеры:
print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
print(two_sum([3, 2, 4], 6))       # [1, 2]