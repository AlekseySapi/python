def my_bin_xor(str1, str2):
    # Сравнивает строки, дополняя короткую строку нулями в начале
    max_len = max(len(str1), len(str2))
    str1 = str1.zfill(max_len)  # Дополняет нулями слева до max_len
    str2 = str2.zfill(max_len)

    result = ""
    for i in range(max_len):
        if str1[i] == '1' and str2[i] == '0':
            result += '1'
        elif str1[i] == '0' and str2[i] == '1':
            result += '1'
        else:
            result += '0'
    return result
    
    
def incr_bin_str(binary_string):
    # Увеличивает двоичную строку на единицу побитово
    try:
        n = len(binary_string)
        carry = 1
        result = ""
        for i in range(n - 1, -1, -1):
            bit = int(binary_string[i])
            sum_bit = bit + carry
            result = str(sum_bit % 2) + result
            carry = sum_bit // 2
        if carry:
            result = "1" + result
        return result
    except (ValueError, IndexError):
        return "Ошибка: Некорректный формат двоичного числа."



def main():
     
    while True:
        print("===== ===== =====")
        num = input("Двоичное число (первое) = ")
        n = int(input(" Кол-во чисел: "))
        key = input("Двоичный ключ = ")
        
        print()
        
        for i in range(n):
            xor = my_bin_xor(num, key)
            d_n = int(num, 2)
            d_k = int(key, 2)
            d_xor = int(xor, 2)
            print(f"{num} *XOR* {key} = {xor}\t| {d_n} xor {d_k} = {d_xor}")
            num = incr_bin_str(num)

        print()



if __name__ == "__main__":
    main()