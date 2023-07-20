import re


def find_numbers(text):
    number_pattern = r'\d'
    numbers = re.findall(number_pattern, text)
    return [int(num) for num in numbers]


def find_emojis(text):
    emoji_pattern = r'(:{2}[A-Z][a-z]{2,}:{2})|(\*{2}[A-Z][a-z]{2,}\*{2})'
    emojis = re.findall(emoji_pattern, text)
    return ["".join(emoji) for emoji in emojis]


def filter_words(emoji_list):
    filtered_words = [re.sub(r'[:*]+', '', string) for string in emoji_list]
    return [word for word in filtered_words if word]


def calculate_cool_threshold(numbers):
    cool_threshold = 0
    for num in numbers:
        if cool_threshold == 0:
            cool_threshold += num
        else:
            cool_threshold *= num
    return cool_threshold


def is_cool_emoji(word, cool_threshold):
    current_count = sum(ord(char) for char in word)
    return current_count >= cool_threshold


def print_cool_emojis(emoji_list, cool_emojis):
    print(f"{len(emoji_list)} emojis found in the text. The cool ones are:")
    for cool in cool_emojis:
        for emo in emoji_list:
            if cool in emo:
                print(emo)


def main():
    text = input()
    numbers = find_numbers(text)
    emojis = find_emojis(text)

    cool_threshold = calculate_cool_threshold(numbers)
    print(f"Cool threshold: {cool_threshold}")

    filtered_words = filter_words(emojis)
    cool_emojis = [word for word in filtered_words if is_cool_emoji(word, cool_threshold)]

    print_cool_emojis(emojis, cool_emojis)


if __name__ == "__main__":
    main()
