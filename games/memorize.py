import random
import tkinter as tk
from tkinter import messagebox

line = '\n======= ======= ======='

def generate_number(digits):
    return ''.join(str(random.randint(0, 9)) for _ in range(digits))

def show_number(number):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Запомните число", f"{number}\n\nЗакройте это окно и введите число в консоли.")

def main():
    print('\nТренировка памяти')
    digits = 3
    correct_answers = 0
    
    while True:
        number = generate_number(digits)
        show_number(number)
        print(line)
        print(f'Введите число:')
        
        while True:
            user_input = input('> ').strip()
            if user_input == number:
                print(' ✅ Верно!')
                correct_answers += 1
                break
            else:
                print(' ❌ Неверно, попробуйте ещё раз.')
        
        if correct_answers % 2 == 0:
            digits += 1
            print(f'\n 📈 Новый уровень! Теперь {digits} цифр.')

if __name__ == "__main__":
    main()