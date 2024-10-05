print("Привет, мир!")

user_name = input("... Постой, а как тебя зовут? ")
print(f"Привет, {user_name}!")

user_age = int(input("Подскажи, сколько тебе лет: "))

if user_age < 13:
    print("Ты пока ещё ребёнок")
elif user_age >= 13 and user_age < 18:
    print("Ты подросток")
elif user_age >= 18 and user_age < 65:
    print("Ты взрослый человек")
else:
    print("Ты пожилой")