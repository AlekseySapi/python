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

    char_A = 'A'
    char_Z = 'Z'
    char_a = 'a'
    char_z = 'z'
    key_K = 'K'
    key_k = 'k'

    # Перевод символов в числовое представление
    char_A_code = ord(char_A)
    char_Z_code = ord(char_Z)
    char_a_code = ord(char_a)
    char_z_code = ord(char_z)
    key_K_code = ord(key_K)
    key_k_code = ord(key_k)

    print(f"Код символа {char_A} - {char_A_code}")
    print(f"Код символа {char_Z} - {char_Z_code}")
    print(f"Код символа {char_a} - {char_a_code}")
    print(f"Код символа {char_z} - {char_z_code}")
    print()
    print(f"Код символа {key_K} - {key_K_code}")
    print(f"Код символа {key_k} - {key_k_code}")

    input()


# original = res ^ b
# print(f"\nИсходное число после операции XOR с числом b ({b}):\n {res} XOR {b} = {original}")