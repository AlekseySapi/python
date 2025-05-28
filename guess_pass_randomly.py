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

        print("\nПопытки:\n")

        steps = 1
        notWin = True
        used_pass_list = []
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
            print(f"> {rand_pass}")
            if rand_pass == user_pass:
                notWin = False
            else:
                steps += 1

        total_steps = len(alphabet) ** pass_len
        percent = int((steps / total_steps) * 100)
        print(f"\nПароль ->  {rand_pass}")
        print(f"\nПопыток использовано:  {steps} из {total_steps}  ({percent}%)\n")


        input()


if __name__ == "__main__":
	main()