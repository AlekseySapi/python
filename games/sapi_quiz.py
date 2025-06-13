# Программа-опрос  Sapi Quiz

import random

line = '\n################# ################# #################'

# Алфавит - 158 символов
alphabet = '!#$&()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~ЁАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюяё№'           
current_shift = ord('ꀀ')
q = [
    '2 * 2 =\n1 - "2", 2 - "4", 3 - "5", 4 - неважно',
    'Утро для тебя - это..\n1 - Кофе, 2 - Суета, 3 - Медитация, 4 - другое'
    ]
t = 'ꐩꐌꐅꑰꑸꐅꐊꀙꀔꐦꑳꀙꐍꑱꐋꑹꐉꐌꀓꐈꐋꑸꐎꑵꀝꀕꐇꑵꐂꐆꑱꐏꐇꀑꐄꐈꀔꐊꑵꐁꀘꐋꐌꐎꑵꐏꑳꑿꀓꐌꐄꐂꀐꐌꀑꑺꀘꀽꀐꐧꐍꐆꑵꐏꀙꐇꐊꐎꐄꐏꐆꐋꐂꑳꑹꀑꐀꀔꐏꐈꑺꀘꐃꑴꑲꐊꐆꑴꀊꀹꀓꀉꀋꀑꀙꁐꁀꁌꁄꁇꀂꀖꀝꁅꀛꁜꁗꀛꁀꁗꁄꁑꁯꁓꁃꁚꁌꁇꀐꀓꀏꀋ'

def xor(text, key):
    res = []
    for i, char in enumerate(text):
       char_code = ord(char)
       key_code = ord(key[i % len(key)]) + current_shift
       res.append(chr(char_code ^ key_code))
    return "".join(res)

def get_key(key):
    key = int(key)
    key *= key * 37
    key = key ** 7
    return str(key)[::-1]


def main():
    print('\n                  === Sapi Quiz ===')
    while True:
        answers = ''
        print(line)
        i = 0
        for _ in range(len(q)):
            print(f"\n   >>  {q[i]}\n")
            i += 1
            s = '>'
            while True:
                n = input(f"{s} ")
                if n in ['1', '2', '3', '4']:
                    answers += n
                    break
                else:
                    s += '>'
                    continue
            print()

        key = get_key(answers)

        print("\nОпрос пройден!\n\n")
        print(xor(t, key))
        print()
        input()


if __name__ == "__main__":
	main()