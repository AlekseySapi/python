import datetime

line = '\n======= ======= ======='


def year_now():
    return datetime.datetime.now().year


def main():
    print(line)

    this_year = year_now()                
    print(f"Сейчас: {this_year} год")


    print()



if __name__ == "__main__":
    main()