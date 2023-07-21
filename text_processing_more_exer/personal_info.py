def cleaning(name_to_clean):
    clean = ""
    for letter in name_to_clean:
        if letter == "|" or letter == "*":
            break
        clean += letter
    return clean


number_lines = int(input())

for line in range(number_lines):
    data = input().split()
    name = ""
    age = ""
    for word in data:
        if word.startswith("@") and "|" in word:
            name += word[1:]
            clean_name = cleaning(name)

        elif word.startswith("#") and "*" in word:
            age += word[1:]
            clean_age = cleaning(age)

    print(f"{clean_name} is {clean_age} years old.")