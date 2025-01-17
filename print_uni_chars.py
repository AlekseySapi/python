import pyperclip

print()
chars = []
char = 'ꀀ'  # Первый символ
char_ord = ord(char)
n = 1160  # Количество символов
i = 0
for c in range(char_ord, char_ord + n):
    chars.append(chr(c))
    chars.append(' ')
    i += 1
    if (i % 20) == 0:
        chars.append('\n')

chars_str = ''.join(chars)

print(chars_str)

pyperclip.copy(chars_str)
print("\n>> Символы скопированы в буфер обмена.\n")

print()
input()