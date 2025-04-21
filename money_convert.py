# Конвертер валют по курсу на 17.02.2025

line = '\n############### ############### ###############'
usd_c = 80.76
eur_c = 93.67
jpy_c = 0.57


def convert_to_curr(rub, choice):
        """Конвертация рублей в выбранную валюту."""
        if choice == '1':
            usd = str(round(rub / usd_c, 2))
            return usd + ' USD'
        elif choice == '2':
            eur = str(round(rub / eur_c, 2))
            return eur + ' EUR'
        elif choice == '3':
            jpy = str(round(rub / jpy_c, 2))
            return jpy + ' JPY'
        
def convert_to_rub(curr, choice):
        """Конвертация валюты в рубли."""
        if choice == '1':
            return str(round(curr * usd_c, 2))
        elif choice == '2':
            return str(round(curr * eur_c, 2))
        elif choice == '3':
            return str(round(curr * jpy_c, 2))

'''

    17.02.2025
1 доллар США (USD) = 102,3762 рубля
1 евро (EUR) = 105,8072 рубля
100 японских иен (JPY) = 63,7144 рубля


    21.04.2025
1 доллар США (USD) = 80,76 рублей
1 евро (EUR) = 93,67 рубля
100 японских иен (JPY) = 57 рублей


'''


def main():
    print(line)
    print(" <  Перевод валют (по данным на 21.04.2025)  >\n")
    while True:
        print(line)

        choice1 = ''
        while choice1 not in ('1', '2'):
            choice1 = input("\n  1 - Из рублей, 2 - В рубли:\n> ")

        if choice1 == '1':
            try:
                rub = round(float(input("\n# Введите сумму в рублях:\n> ")), 2)
            except:
                continue

            choice2 = ''
            while choice2 not in ('1', '2', '3'):
                choice2 = input("\n# Выберите валюту (1 - USD, 2 - EUR, 3 - JPY):\n> ")

            print(f'\n{rub} RUB = {convert_to_curr(rub, choice2)}')
        else:
            choice_curr = ''
            while choice_curr not in ('1', '2', '3'):
                choice_curr = input("\n# Выберите валюту (1 - USD, 2 - EUR, 3 - JPY):\n> ")
            try:
                curr = round(float(input("\n# Введите сумму:\n> ")), 2)
            except:
                continue
            
            if choice_curr == '1':
                print(f'\n{curr} USD = {convert_to_rub(curr, choice_curr)} RUB')
            elif choice_curr == '2':
                print(f'\n{curr} EUR = {convert_to_rub(curr, choice_curr)} RUB')
            elif choice_curr == '3':
                print(f'\n{curr} JPY = {convert_to_rub(curr, choice_curr)} RUB')


if __name__ == "__main__":
    main()