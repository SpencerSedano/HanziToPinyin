from pypinyin import pinyin, lazy_pinyin, Style

user_input = input("Enter a Chinese characters word: ")
print(user_input)

user_input_pinyin = pinyin(user_input)

user_input_pinyin_str = str(user_input_pinyin)

print(user_input_pinyin)
print(' '.join(' '.join(l) for l in user_input_pinyin))
user_input_pinyin_formatted = " ".join(c for c in user_input_pinyin_str if c.isalpha())
print(user_input_pinyin_formatted)