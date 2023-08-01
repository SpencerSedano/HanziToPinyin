from pypinyin import pinyin, lazy_pinyin, Style

user_input = input("Enter a Chinese characters word: ")
print(user_input)

user_input_pinyin = pinyin(user_input)
print(type(user_input_pinyin))
user_input_pinyin = str(user_input_pinyin)
print(user_input_pinyin)
user_input_pinyin_formatted = "".join(c for c in user_input_pinyin if c.isalpha())
print(user_input_pinyin_formatted)