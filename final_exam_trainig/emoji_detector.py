import re

emoji_pattern = r'(:{2}[A-Z][a-z]{2,}:{2})|(\*{2}[A-Z][a-z]{2,}\*{2})'
number_pattern = r'\d'
word_pattern = r'[A-Z][a-z]+'

text = input()
numbers = re.findall(number_pattern, text)
emojis = re.findall(emoji_pattern, text)

cool_treshold = 0
for num in numbers:
    if cool_treshold == 0:
        cool_treshold += int(num)
    elif num != 0:
        cool_treshold *= int(num)
print(f"Cool threshold: {cool_treshold}")

emoji_list = ["".join(emoji) for emoji in emojis]
print(f"{len(emoji_list)} emojis found in the text. The cool ones are:")

filtered_words = [re.sub(r'[:*]+', '', string) for string in emoji_list]
cool_emojis = []
for word in filtered_words:
    current_count = 0
    for char in word:
        current_count += ord(char)
    if current_count >= cool_treshold:
        cool_emojis.append(word)
for emo in cool_emojis:
    for cool in emoji_list:
        if emo in cool:
            print(cool)
