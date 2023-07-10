text = input().split()
new_text = [word * len(word) for word in text]
print("".join(new_text))