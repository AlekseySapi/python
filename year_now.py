from datetime import date

line = '\n========= ========= ========= ========= ========='


today = date.today()
this_year = today.year
month = today.month
day = today.day


def main():
    print(line)
    print(" ===== Год в разных системах летосчисления =====")

    print(f"\n << Сейчас >>")
    print(f"<< {this_year} год >>")

    ch_year = this_year + 2697
    print(f"\nКитай: {ch_year} год")

    jap1_year = this_year - 2019
    jap2_year = this_year + 660
    print(f"\nЯпония: {jap1_year} год  < или >  {jap2_year} год")

    budd_year = this_year + 543
    print(f"\nБуддийский: {budd_year} год")

    crt_heb_year = this_year + 3760
    print(f"\nОт Сотворения мира (иуд.): {crt_heb_year} год")

    if month < 9:
        crt_byz_year = this_year + 5509 - 1
    else:
        crt_byz_year = this_year + 5509
    print(f"От Сотворения мира (визант.): {crt_byz_year} год")


    print(line)



if __name__ == "__main__":
    main()