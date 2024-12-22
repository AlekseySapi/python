# XOR

##########
# 0 - 000
# 1 - 001
# 2 - 010
# 3 - 011
# 4 - 100
# 5 - 101
# 6 - 110
# 7 - 111
# 8  - 1000
# 9  - 1001
# 10 - 1010
# 11 - 1011
# 12 - 1100
# 13 - 1101
# 14 - 1110
# 15 - 1111

'''
a = 3   # 011
b = 5   # 101
        # =
        # 110
'''

while True:
    print("=== === ===")
    '''
    a = int(input("a = "))
    b = int(input("b = "))

    res = a ^ b

    print(f"{a} XOR {b} = {res}\n")
    '''

    char = 'W'
    key_K = 'K'
    key_k = 'k'
    key_1 = '1'
    key_5 = '5'
    key_7 = '7'

    # Перевод символов в числовое представление
    char_code = ord(char)
    key_K_code = ord(key_K)
    key_k_code = ord(key_k)
    key_1_code = ord(key_1)
    key_5_code = ord(key_5)
    key_7_code = ord(key_7)

    # Шифровка разными ключами
    encrypted_by_K = char_code ^ key_K_code
    encrypted_by_k = char_code ^ key_k_code
    encrypted_by_1 = char_code ^ key_1_code
    encrypted_by_5 = char_code ^ key_5_code
    encrypted_by_7 = char_code ^ key_7_code


    print(f"Шифровка символа '{char}':")
    print()
    print(f"Ключом {key_K} -> {chr(encrypted_by_K)}\t | {char_code} ^ {key_K_code} -> {encrypted_by_K}")
    print(f"Ключом {key_k} -> {chr(encrypted_by_k)}\t | {char_code} ^ {key_k_code} -> {encrypted_by_k}")
    print()
    print(f"Ключом {key_1} -> {chr(encrypted_by_1)}\t | {char_code} ^ {key_1_code} -> {encrypted_by_1}")
    print(f"Ключом {key_5} -> {chr(encrypted_by_5)}\t | {char_code} ^ {key_5_code} -> {encrypted_by_5}")
    print(f"Ключом {key_7} -> {chr(encrypted_by_7)}\t | {char_code} ^ {key_7_code} -> {encrypted_by_7}")

    input()


# original = res ^ b
# print(f"\nИсходное число после операции XOR с числом b ({b}):\n {res} XOR {b} = {original}")