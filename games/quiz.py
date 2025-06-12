# Программа-опрос  Sapi Quiz

import random

line = '\n############### ############### ###############'
current_shift = ord('ꀀ')
q = [
    '2 * 2 =\n1 - "2", 2 - "4", 3 - "5", 4 - неважно',
    'Утро для тебя - это..\n1 - Кофе, 2 - Суета, 3 - Медитация, 4 - другое'
    ]
t = 'ꀸꐫꐉꐁꑳꑰꐏꐏꀓꀑꐠꑺꀒꐎꑲꐏꑺꐊꐊꀑꐌꐎꑲꐏꑳꀝꀒꐏꑰꐃꐇꑳꐊꐃꀒꐌꐂꀑꐀꑰꐇꀑꐀꐏꐍꑱꐌꑰꑹꀑꐈꐁꐈꀑꐊꀑꑽꀐꀸꀑꐦꐏꐃꑱꐌꀑꐍꐏꐄꐁꐉꐏꐀꐁꑰꑽꀒꐃꀒꐍꐌꑿꀒꐂꑲꑲꐍꐎꑱꀋꀸꀑꀌꀏꀒꀑꁚꁅꁆꁁꁁꀋꀝꀞꁆꀟꁟꁔꀝꁂꁓꁁꁛꁮꁕꁃꁝꁄꁂꀑꀒꀍꀎ'

def xor(text, key):
    res = []
    for i, char in enumerate(text):
       char_code = ord(char)
       key_code = ord(key[i % len(key)]) + current_shift
       res.append(chr(char_code ^ key_code))
    return "".join(res)


def main():
    print('\n   === Sapi Quiz ===')
    while True:
        answers = ''
        print(line)
        print(f"\n   >>  {q[0]}\n")
        s = '>'
        while True:
            n1 = input(f"{s} ")
            if n1 in ['1', '2', '3', '4']:
                answers += n1
                break
            else:
                s += '>'
                continue
        print()

        print(f"\n  >>  {q[1]}\n")
        s = '>'
        while True:
            n2 = input(f"{s} ")
            if n2 in ['1', '2', '3', '4']:
                answers += n2
                break
            else:
                s += '>'
                continue
        print()

        print("\nОпрос пройден!\n\n")
        print(xor(t, answers))
        print()
        input()


if __name__ == "__main__":
	main()