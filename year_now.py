import datetime

line = '\n======= ======= ======= ======= ======='


def year_now():
    return datetime.datetime.now().year


def main():
    print(line)
    print(" === Год в разных календарях мира ===")

    this_year = year_now()
    print(f"\n<< {this_year} год >>")

    ch_year = this_year + 2697
    print(f"\nКитай: {ch_year} год")


    print()



if __name__ == "__main__":
    main()