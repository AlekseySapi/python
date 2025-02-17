# Конвертер валют по курсу на 17.02.2025

line = '\n############### ############### ###############'


def convert(rub, choice):
        """Конвертация рублей в выбранную валюту."""
        if choice == '1':
            usd = str(round(rub / 102.376, 2))
            return usd + ' USD'
        elif choice == '2':
            eur = str(round(rub / 105.807, 2))
            return eur + ' EUR'
        elif choice == '3':
            jpy = str(round(rub / 0.637, 2))
            return jpy + ' JPY'

'''

    17.02.2025
1 доллар США (USD) = 102,3762 рубля
1 евро (EUR) = 105,8072 рубля
100 японских иен (JPY) = 63,7144 рубля


'''


def main():
    print(line)
    print(" <  Перевод валют (по данным на 17.02.2025)  >\n")
    while True:
        print(line)
        try:
            rub = round(float(input("# Введите сумму в рублях:\n> ")), 2)
        except:
            continue

        choice = ''
        while choice not in ('1', '2', '3'):
            choice = input("\n# Выберите валюту (1 - USD, 2 - EUR, 3 - JPY):\n> ")

        print(f'\n{rub} RUB = {convert(rub, choice)}')


if __name__ == "__main__":
    main()