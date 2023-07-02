text = [symb for symb in input() if symb != " "]
characters = {}
for char in text:
    if char not in characters:
        characters[char] = 0
    characters[char] += 1
for key, value in characters.items():
    print(f"{key} -> {value}")