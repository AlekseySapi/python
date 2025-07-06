# Счётчик всех символов японской каны в тексте (суммарно Хирагана и Катакана) и составление топа по их частоте

from collections import Counter
import pandas as pd

line = '\n################# ################# #################'


def get_char_frequency(text):
    text = text.replace('\n', '')  # удаляем все переводы строк
    counts = Counter(text)
    total = sum(counts.values())
    df = pd.DataFrame(
        counts.items(),
        columns=['Символ', 'Кол-во']
    )
    df['Частота (%)'] = (df['Кол-во'] / total * 100).round(2)
    df = df.sort_values(by='Кол-во', ascending=False).reset_index(drop=True)
    df.index += 1
    pd.set_option('display.max_rows', None)  # показать все строки без сокращений
    return df


def hiragana_to_katakana(text):
    table = str.maketrans({
        'あ': 'ア', 'い': 'イ', 'う': 'ウ', 'え': 'エ', 'お': 'オ',
        'か': 'カ', 'き': 'キ', 'く': 'ク', 'け': 'ケ', 'こ': 'コ',
        'さ': 'サ', 'し': 'シ', 'す': 'ス', 'せ': 'セ', 'そ': 'ソ',
        'た': 'タ', 'ち': 'チ', 'つ': 'ツ', 'て': 'テ', 'と': 'ト',
        'な': 'ナ', 'に': 'ニ', 'ぬ': 'ヌ', 'ね': 'ネ', 'の': 'ノ',
        'は': 'ハ', 'ひ': 'ヒ', 'ふ': 'フ', 'へ': 'ヘ', 'ほ': 'ホ',
        'ま': 'マ', 'み': 'ミ', 'む': 'ム', 'め': 'メ', 'も': 'モ',
        'や': 'ヤ', 'ゆ': 'ユ', 'よ': 'ヨ',
        'ら': 'ラ', 'り': 'リ', 'る': 'ル', 'れ': 'レ', 'ろ': 'ロ',
        'わ': 'ワ', 'を': 'ヲ', 'ん': 'ン',
        'が': 'ガ', 'ぎ': 'ギ', 'ぐ': 'グ', 'げ': 'ゲ', 'ご': 'ゴ',
        'ざ': 'ザ', 'じ': 'ジ', 'ず': 'ズ', 'ぜ': 'ゼ', 'ぞ': 'ゾ',
        'だ': 'ダ', 'ぢ': 'ヂ', 'づ': 'ヅ', 'で': 'デ', 'ど': 'ド',
        'ば': 'バ', 'び': 'ビ', 'ぶ': 'ブ', 'べ': 'ベ', 'ぼ': 'ボ',
        'ぱ': 'パ', 'ぴ': 'ピ', 'ぷ': 'プ', 'ぺ': 'ペ', 'ぽ': 'ポ',
        'ぁ': 'ァ', 'ぃ': 'ィ', 'ぅ': 'ゥ', 'ぇ': 'ェ', 'ぉ': 'ォ',
        'ゃ': 'ャ', 'ゅ': 'ュ', 'ょ': 'ョ', 'っ': 'ッ',
        'ゎ': 'ヮ',
        'ゐ': 'ヰ', 'ゑ': 'ヱ',
        'ゔ': 'ヴ',
        'ゕ': 'ヵ', 'ゖ': 'ヶ'
    })
    return text.translate(table)


def main():
    print('\n    === Топ символов японской каны по частоте ===')
    while True:
        print(line)
        file_path = 'w.txt'
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        katakana_text = hiragana_to_katakana(text)

        with open(file_path, 'a', encoding='utf-8') as file:
            file.write("\n\n\n=== Катакана ===\n")
            file.write(katakana_text)
            file.write("\n\n\n===== Топ символов этого текста =====\n\n")
            file.write(str(get_char_frequency(katakana_text)))

        print("\n\n\n  ✅ Топ символов составлен и записан в файл.\n")
        input()


if __name__ == "__main__":
	main()