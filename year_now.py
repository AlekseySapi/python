import datetime

line = '\n======= ======= ======= ======= ======='


def year_now():
    return datetime.datetime.now().year


def main():
    print(line)
    print(" === Год в разных календарях мира ===")

    this_year = year_now()
    print(f"\n << Сейчас >>")
    print(f"<< {this_year} год >>")

    ch_year = this_year + 2697
    print(f"\nКитай: {ch_year} год")

    jap1_year = this_year - 2019
    jap2_year = this_year + 660
    print(f"\nЯпония: {jap1_year} год  < или >  {jap2_year} год")

    budd_year = this_year + 543
    print(f"\nБуддийский: {budd_year} год")


    print()



if __name__ == "__main__":
    main()