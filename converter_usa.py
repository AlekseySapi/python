import os

line = '\n####### ####### ####### ####### #######'


def convert(value, from_unit, to_unit):
    conversion_factors = {
        ("km", "miles"): 0.621371,
        ("miles", "km"): 1.60934,
        ("m", "ft"): 3.28084,
        ("ft", "m"): 0.3048,
        ("cm", "inches"): 0.393701,
        ("inches", "cm"): 2.54,
        ("kg", "lbs"): 2.20462,
        ("lbs", "kg"): 0.453592,
    }
    
    factor = conversion_factors.get((from_unit, to_unit))
    if factor:
        return round(value * factor, 4)
    return None


def main():
    print(line)
    print(" < Конвертер величин >")
    
    while True:
        print(line)
        try:
            value = float(input("# Введите число:\n> "))
        except ValueError:
            print("\n⚠️  Ошибка: Введите корректное число.\n")
            continue

        print("\n  Выберите, из чего переводим:")
        print("  1 - Км в мили    | 2 - Мили в км")
        print("  3 - М в футы     | 4 - Футы в м")
        print("  5 - См в дюймы   | 6 - Дюймы в см")
        print("  7 - Кг в фунты   | 8 - Фунты в кг")

        choice = ''
        while choice not in map(str, range(1, 9)):
            choice = input("\n> ")

        units = {
            '1': ('km', 'miles'),
            '2': ('miles', 'km'),
            '3': ('m', 'ft'),
            '4': ('ft', 'm'),
            '5': ('cm', 'inches'),
            '6': ('inches', 'cm'),
            '7': ('kg', 'lbs'),
            '8': ('lbs', 'kg'),
        }

        from_unit, to_unit = units[choice]
        result = convert(value, from_unit, to_unit)
        
        if result is not None:
            print(f"\n  {value} {from_unit} = {result} {to_unit}\n")
        else:
            print("\n⚠️  Ошибка: Невозможно выполнить конвертацию.\n")


if __name__ == "__main__":
    main()