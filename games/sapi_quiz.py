# Программа-опрос  Sapi Quiz

import random

line = '\n################# ################# #################'

# Алфавит - 158 символов
alphabet = '!#$&()*+,-./ 0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}~ЁАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюяё№'           
current_shift = ord('ꀀ')
q = [
    '"2 * 2 = "\n1 - "2"; 2 - "4"; 3 - "5"; 4 - Неважно',
    'Утро для тебя - это..\n1 - Кофе; 2 - Суета; 3 - Медитация; 4 - Другое',
    'У тебя преобладают черты сангвиника и/или флегматика?\n1 - Да; 2 - Я больше холерик; 3 - Я больше меланхолик; 4 - Не знаю',
    'Какое учение тебе ближе?\n1 - Христианство; 2 - Ислам; 3 - Буддизм; 4 - Другое',
    'Бог есть?\n1 - Да; 2 - Нет; 3 - Точно это неизвестно; 4 - Сомневаюсь',
    'Тебе бы хотелось жить вечно?\n1 - Да, конечно; 2 - Точно нет; 3 - Не думаю о таком; 4 - Даже не знаю..'
    ]
t = 'ꁋꑹꀧꑡꑡꑯꀢꀀꀔꑐꀙꀌꀓꀒꀔꁾꁩꁧꀁ씫ꑥꑦꑾꀈꁼꁭꁰꁡꁤꀐꁮꁠꀽꀪꀥꀜꀡꀑꀦꑬꑰꑤꑧꑢꑤꀡꀉꀜꀸꑒꀨꁴꀦꑧꀃꀀꑄꀍꐲꑨꐙꑿꑺꁹꀙꁭꁫꁯꁸꁬꁭꁮꀪꀂꀃꀬꀇꀭꀚꀎꑪꑾꑿꑫꑦꀇꑶꀖꑽꀚꀽꑈꀶꀿꀤꀯꀒꁻꐵꀃꑨꑯꀀꀀ셰ꁙꁘꁗꁋꁱꀇꀀꑜꀀꑒꑍꀇꀏꑾꑗꑽꀝꑟꐺꑊꐻꁗꁄꀈꀻꁖꁯꁠꐟꀞꀚꁵꁶ'

def xor(text, key):
    res = []
    for i, char in enumerate(text):
       char_code = ord(char)
       key_code = ord(key[i % len(key)]) + current_shift
       res.append(chr(char_code ^ key_code))
    return "".join(res)

def caesar_plus_shift(text, shift, alph):
    result = []
    i = 0
    for char in text:
        if char in alph:
            idx = alph.index(char)
            new_idx = idx + shift + i
            i += 1 + shift % 9
            result.append(alph[new_idx % len(alph)])
        else:
            result.append(char)
    return ''.join(result)

def vigenere(text, key, alph, mode):
    result = []
    key_index = 0
    for char in text:
        if char not in alph:
            result.append(char)
            continue
        char_index = alph.index(char)
        key_char = key[key_index % len(key)]
        key_shift = alph.index(key_char)
        # print(f"key_shift: {key_shift}")
        if mode == 'ci':
            new_index = (char_index + key_shift) % len(alph)
        else:
            new_index = (char_index - key_shift) % len(alph)
        result.append(alph[new_index])
        key_index += 1
    return ''.join(result)

def get_key(key, shift):
    key = int(key)
    key *= key * 37
    key = str(key ** 7)[::-1]
    # print(f"\nnum_key:\n{key}\n")
    key = caesar_plus_shift(key, shift, alphabet)
    return key


def main():
    print('\n                  === Sapi Quiz ===')
    while True:
        answers = ''
        print(line)
        i = 0
        for _ in range(len(q)):
            print(f"\n   >> {i+1}.  {q[i]}\n")
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

        shift = 1 + int(answers) % 99
        # print(f"\nshift: {shift}\n")

        key = get_key(answers, shift)
        # print(f"\nkey:\n{key}\n")

        print("\nОпрос пройден!\n\n(..но открылось ли секретное сообщение...?)\n\n")

        # viged_t = vigenere(t, key, alphabet, 'ci')
        # print(f"\nviged_t:\n{viged_t}\n")
        # res = xor(viged_t, key)
        unxored_t = xor(t, key)
        # print(f"\nunxored_t:\n{unxored_t}\n")
        res = vigenere(unxored_t, key, alphabet, 'unci')
        print()
        print(res)

        print()
        input()


if __name__ == "__main__":
	main()