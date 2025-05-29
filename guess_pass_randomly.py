# Программа рандомного перебора пароля

import random

line = '\n############### ############### ###############'
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'


def main():
    print('\n     === Рандомный перебор пароля ===\n\n     (только латинские буквы и цифры)')
    while True:
        print(line)
        print("\nВведите пароль:")
        s = ''
        while True:
            s += '>'
            check = False
            user_pass = input(f'{s} ').strip()
            for char in user_pass:
                if char not in alphabet:
                    check = True
            if check:
                continue
            else:
                break
        pass_len = len(str(user_pass))
        total_steps = len(alphabet) ** pass_len
        perc_1 = int(total_steps / 100)
        perc_10 = int(total_steps / 10)
        print()

        steps = 1
        notWin = True
        used_pass_list = []
        p = 0
        while notWin:
            while True:
                rand_pass = ''
                rand_chars = []
                for _ in range(pass_len):
                    rand_char = random.choice(alphabet)
                    rand_chars.append(rand_char)
                rand_pass = ''.join(rand_chars)
                if rand_pass in used_pass_list:
                    continue
                else:
                    used_pass_list.append(rand_pass)
                    break
            if pass_len > 1:
                if (steps % perc_1) == 0:
                    p += 1
                    print(f".. {p}%")
            else:
                if (steps % perc_10) == 0:
                    p += 10
                    print(f".. {p}%")
            if rand_pass == user_pass:
                notWin = False
            else:
                steps += 1

        print(f"\nПароль ->  {rand_pass}")
        print(f"\nПопыток использовано:  {steps} из {total_steps}  ({p}%)\n")


        input()


if __name__ == "__main__":
	main()