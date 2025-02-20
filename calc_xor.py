# Калькулятор XOR  by AlekseySapi


line = "\n========================================"
z = 24


while True:
    print(line)
    try:
        n1 = int(input("\n> Введите первое число: "))
    except:
        print()
        continue
        
    while True:
        try:
            n2 = int(input("\n> Введите второе число: "))
        except:
            continue
        
        print("\n")
        print("    L   L   L   L   L   L")	
        print(f"    {bin(n1)[2:].zfill(z)}  [{n1}]")
        print(f"    {bin(n2)[2:].zfill(z)}  [{n2}]")
        print(f"    =")
        print(f"    {bin(n1 ^ n2)[2:].zfill(z)}  [{n1 ^ n2}]")
            
        print(f"\n\n    n1 XOR n2 = {n1 ^ n2}  \n")
        break
        



####  Поле для расчётов  ####
'''







'''
#############################