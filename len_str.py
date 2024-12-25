

en = '`1234567890-=qwertyuiop[]asdfghjkl;\'zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?'
ru = 'ё1234567890-=йцукенгшщзхъфывапролджэячсмитьбю.Ё!"№;%:?*()_+ЙЦУКЕНГШЩЗХЪ/ФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,'

str = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
str2 = '^*/%+)[=}@(`;],&{#'

def main():
    
    print(f"en - {len(en)}")
    print(f"ru - {len(ru)}")
    print("===")
    print(f"str - {len(str)}")
    print(f"str2 - {len(str2)}")


if __name__ == "__main__":
    main()