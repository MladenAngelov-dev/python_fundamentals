line = input().split()
word_container = {}

for word in line:
    word_lower = word.lower()
    if word_lower not in word_container:
        word_container[word_lower] = 0
    word_container[word_lower] += 1
for key, value in word_container.items():
    if value % 2 != 0:
        print(key, end=" ")

