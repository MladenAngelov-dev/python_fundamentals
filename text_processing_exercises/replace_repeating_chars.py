text = input()
filtered_text = ""
new_char = ""
for char in text:
    if char != new_char:
        new_char = char
        filtered_text += char
print(filtered_text)