def celsius_to_fahrenheit(celsius: float) -> float:
    """
    Конвертирует температуру из градусов Цельсия в Фаренгейты.

    :param celsius: Температура в градусах Цельсия
    :return: Температура в Фаренгейтах
    """
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """
    Конвертирует температуру из Фаренгейтов в градусы Цельсия.

    :param fahrenheit: Температура в Фаренгейтах
    :return: Температура в градусах Цельсия
    """
    return (fahrenheit - 32) * 5 / 9


def main():
    """
    Основная функция программы для выбора типа конвертации и вывода результата.
    """
    print("Конвертер температуры 🌡️\n")
    print("1: Цельсий в Фаренгейт")
    print("2: Фаренгейт в Цельсий\n")
    
    choice = input("Выберите тип конвертации (1 или 2): ").strip()
    
    if choice == "1":
        try:
            celsius = float(input("\nВведите температуру в Цельсиях: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"\n{celsius}°C соответствует {fahrenheit:.2f}°F\n")
        except ValueError:
            print("Ошибка ввода: Введите корректное числовое значение.\n")
    
    elif choice == "2":
        try:
            fahrenheit = float(input("\nВведите температуру в Фаренгейтах: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"\n{fahrenheit}°F соответствует {celsius:.2f}°C\n")
        except ValueError:
            print("Ошибка ввода: Введите корректное числовое значение.\n")
    
    else:
        print("Ошибка: Введите 1 или 2 для выбора режима.\n")


if __name__ == "__main__":
    main()