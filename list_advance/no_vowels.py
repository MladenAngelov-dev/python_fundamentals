word = input()
filtered_word = [w for w in word if w.lower() not in ['a', 'o', 'u', 'e', 'i']]
print("".join(filtered_word))