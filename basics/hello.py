print("Привет, мир!")

user_name = input("... Постой, а как тебя зовут? ")
print(f"Привет, {user_name}!")


while True:
    user_input = input("Введите сколько вам лет (или напишите 'stop', чтобы выйти): ")

    if user_input.lower() == 'stop':
        print("Программа завершена.")
        break

    user_age = int(user_input)


if user_age < 13:
    print("Ты пока ещё ребёнок")
elif user_age >= 13 and user_age < 18:
    print("Ты подросток")
elif user_age >= 18 and user_age < 65:
    print("Ты взрослый человек")
elif user_age >= 65:
    print("Ты пожилой")
else:
    print("?")