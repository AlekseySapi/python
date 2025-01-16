import pyperclip

line = '\n####### ####### #######'

alphs = [
	'q5JW1KRFhGUmHz8Ng9T4bLlOrYaPV7AIQScuMoEw2BsC3nZt6ykfvxpX0edDji',
	'Ljm0NfcSsh9oq5pU6IMGHDPukneFVCRiZrW3JadE7Y2y8zwlxOgBbT4A1XKvtQ',
	'YeSQqZrvN15Fgcj9tIGAzlBE3wHLOTuM02dWnsJ4py6K7mXihfkPU8baVoDxRC',
	'8LMQVxo9fKSlgsXOPAH6kCmIy7nRBqU254dhYG0baDZzErwNv3WtFuijTJpe1c',
	'1UzF7f8OeDnptoS4QuWgERYN2x9GJM03rCqIjcBybw6VT5ZsaHdKXmlkvhiAPL',
	'eXB9GixmbFPsuoYCntJ803AVz6Il2EHgvrZL4d1kK5qSwQUfNajycTMORh7WDp',
	'65nv0cZJqRtX9UgPTkBjfaxGS4LCluhDdNo3YOiMe8rswpFHy2mEbVAKzQI71W',
	'CnPFlk5B1sOcX64jLA8xGMVpWStaKqrzU3DId0uoemTy7wifgvhQHZNJE29RYb',
	'QfxLil8kEITnRm7WwUt3jZKbS9zGqeocgy21Vhu50rHDNPCAvYp4sFO6aBMJdX',
	'6dTHkleU0fYmNFABVGQcjy5qsRbhKorDExPICngu317X984azvJtLpwOZi2MWS'
]

nums = [
	'4108796253',
	'0785219436',
	'6158493207',
	'0749156283',
	'4638905172',
	'5180479623',
	'1670293845',
	'3468209571',
	'3028951647',
	'9251870463'
]

all_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'


def translate(text):
	rus = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
	eng = 'ABVGD30XZIJKLMNOPRSTUFHCQW64Y5789abvgd30xzijklmnoprstufhcqw64y5789'
	
	rus_to_eng = str.maketrans(rus, eng)
	
	res = []
	for char in text:
		if char in rus:
			res.append(char.translate(rus_to_eng))
		else:
			res.append(char)
	return "".join(res)


def caesar(text, shift, alphabet):
	result = []
	i = 1
	for char in text:
		if char in alphabet:
			idx = alphabet.index(char)
			new_idx = idx + shift + i
			result.append(alphabet[new_idx % len(alphabet)])
		else:
			result.append(char)
		i += 1
	return ''.join(result)


def get_char(shift, alphabet, i):
	new_i = shift + i * 2
	new_char = alphabet[new_i % len(alphabet)]
	return new_char


def add_chars(word, shift, alphabet, l):
	word_chars = list(word)
	i = 1
	for _ in range(l):
		if i % 21 == 0:
			shift += i
		new_char = get_char(shift, alphabet, i)
		res_char = caesar(new_char, shift, alphabet)
		if res_char in word_chars:
			res_char = caesar(res_char, i, alphabet)
			i += 1
		word_chars.append(res_char)
		i += 1
	return ''.join(word_chars)


def reverse_halves(word):
	mid = len(word) // 2
	first_half = word[:mid]
	second_half = word[mid:]

	mid1 = len(first_half) // 2
	mid2 = len(second_half) // 2

	part1 = first_half[:mid1]
	part2 = first_half[mid1:]
	part3 = second_half[:mid2]
	part4 = second_half[mid2:]

	result_word = part2 + part4 + part1 + part3
	return result_word


def clean(word, shift, alphabet):
	word_chars = list(word)
	for i in range(len(word_chars) - 1):
		if word_chars[i] == word_chars[i + 1]:
			word_chars[i + 1] = get_char(shift, alphabet, i)
	return ''.join(word_chars)


def nums_check(word, shift, nums):
	digit_count = sum(1 for char in word if char.isdigit())
	if digit_count == 0:
		shortage = 5
	else:
		shortage = len(word) / digit_count
	desire = 4
	word_chars = list(word)
	if shortage > desire:
		non_digit_indices = [i for i, char in enumerate(word_chars) if not char.isdigit()]
		needed_nums = (len(word) // desire) - digit_count
		for i in range(needed_nums):
			index_to_replace = non_digit_indices[(i * shift + i) % len(non_digit_indices)]
			word_chars[index_to_replace] = nums[(i + shift) % len(nums)]
	return ''.join(word_chars)


def check_and_remove(text):
	word_chars = list(text)
	result = []
	for char in word_chars:
		if char in all_chars:
			result.append(char)
	return ''.join(result)



def main():
	print(line)
	while True:
		key = ''
		while key == '':
			key = input("Введите старый пароль\n   или секретное слово:\n> ")

		key_chars = list(key)
		chars_num = 0
		i = 3
		for char in key_chars:
			chars_num += ord(char) * i * 10 + i 
			i += 1
		
		key = translate(key)
		key = check_and_remove(key)

		if key == '':
			shift = (chars_num % 61) + 1
			index = (chars_num // 10) % 10
			chars_num_str = str(chars_num)
			ch_nums = list(chars_num_str)
			res = []
			i = 1
			for _ in ch_nums:
				res.append(get_char(shift, alphs[index], i))
				i += 1
			key = ''.join(res)

		rev_key = reverse_halves(key)
		
		# pass_len = int(input("\nВведите желаемую длину пароля\n(рекомендуется 15-25 симв.)\n> "))
		pass_len = 15

		seed_str = input("seed: ")
		if seed_str == '':
			shift = (chars_num % 61) + 1
			index = (chars_num % 9) + 1
		else:
			seed = 0
			i = 3
			for char in seed_str:
				seed += ord(char) * i * 10 + i
				i += 1
			shift = ((chars_num + seed) % 61) + 1
			index = ((chars_num + seed) // 10) % 10

		caesar_key = caesar(rev_key, shift, alphs[index])
		
		if len(caesar_key) < pass_len:
			l = pass_len - len(caesar_key)
			res_key = add_chars(caesar_key, shift, alphs[index], l)
		elif len(caesar_key) > pass_len:
			res_key = caesar_key[:pass_len]
		else:
			res_key = caesar_key
		
		clean_key = clean(res_key, shift, alphs[index])
		nums_checked_key = nums_check(clean_key, shift, nums[index])
		result_pass = reverse_halves(nums_checked_key)

		pyperclip.copy(result_pass)

		print("\n>> Пароль скопирован\n>>   в буфер обмена\n")
		print(line)


if __name__ == "__main__":
    main()