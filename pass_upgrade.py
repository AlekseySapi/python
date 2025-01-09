

line = '\n####### ####### #######'

alphs = [
	'h5l7XHAQk9LuctyreUn6NOpKwVJEixDaZ0SgBT4Im28qo1MvYzj3WPsfRFbdGC',
	'yfZr4jCdoVSIQ1G6J0zPD9HbRNaklp7gqLFx5Kv8Unth2AcuseOMmXTWwiE3BY',
	'9fuAepxBtgk4DGO7Z1cIrP0y2L6nbFqasmiV8K3SQdUhjNzYTEvlWHRXoCwJ5M',
	'MT1ahwx9mukICDvV8l5ZopBnSqfj3YPKRWeNQdrGb64OcLHA2EgistXyU0F7zJ',
	'ZnagoqmjfKHcPEIL3A0YDGt1si9OdS5pUvC4R7wXBQJrTMb8NkhlFyWxez62uV',
	'WQ8zXv7x1gA9IoUKRDV4iMklfPcyBar3S52OnbmtGZHEehjC6TJpuFqYds0NLw',
	'DK8EuMBmIO27W9lRayf3thAJvkFNwdSiHL0eocPxb4UCGrZnXqjV6YzpT5sQg1',
	'tax7Te3Co5XiPjUsdVhgmzAyBQGHuOfr1Rv4wYSqMkFNnc8EJ6WplZDbL20IK9',
	'IzyRlLWOdfivUhbAYPk0KSn8uwep6Bs52T7jVqg4HQJNaxMCXoGZ9D3E1mFctr',
	'4Pn8NxlAaUECbZpXzq1YVIJ7cRkwSyT5WBLvHDfrsMOjidm9e30goK2G6uhFQt'
]

nums = [
	'6274308195',
	'4563017928',
	'6145087239',
	'5216749083',
	'0492375681',
	'2938064715',
	'0714859326',
	'7650214983',
	'3902578164',
	'3942518067'
]


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
		new_char = get_char(shift, alphabet, i)
		res_char = caesar(new_char, shift, alphabet)
		while res_char in word_chars:
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

	result_word = part2 + part1 + part4 + part3
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
			index_to_replace = non_digit_indices[(i + shift) % len(non_digit_indices)]
			word_chars[index_to_replace] = nums[(i + shift) % len(nums)]
	return ''.join(word_chars)



def main():
	print(line)
	while True:
		key = ''
		while key == '':
			key = input("Введите старый пароль\n  или секретное слово:\n> ")

		key = translate(key)
		rev_key = reverse_halves(key)
		
		# pass_len = int(input("\nВведите желаемую длину пароля\n(рекомендуется 15-20 симв.)\n> "))
		pass_len = 20
		
		seed_str = input("seed: ")
		if seed_str == '':
			seed = 42
		else:
			seed = 0
			for char in seed_str:
				seed += ord(char)
			
		shift = (seed % 61) + 1
		index = seed % 10

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

		
		print(f"\nВаш пароль:\n> {result_pass}\n")
		print(line)




if __name__ == "__main__":
    main()