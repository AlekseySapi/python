# Калькулятор степеней by AlekseySapi


line = "\n========================================"
p = 21	# Показатель степени


while True:
    print(line)
    try:
        n = int(input(f"> Введите число: "))
        if n < 2: continue
    except:
        continue
        
    nums = []
    for i in range(p):
        nums.append(n ** i)
        	
    print()
    for i in range(0, len(nums), 3):
    	print(' '.join(map(str, nums[i:i+3])))

     



####  Поле для расчётов  ####
'''







'''
#############################