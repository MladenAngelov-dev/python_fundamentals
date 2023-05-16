word = input()
coffe_needed = 0

while word != "END":
    if word == "dog" or word == "cat" or word == "coding" or word == "movie":
        coffe_needed += 1
    elif word == "DOG" or word == "CAT" or word == "CODING" or word == "MOVIE":
        coffe_needed += 2
    else:
        pass
    word = input()
    if coffe_needed > 5:
        print("You need extra sleep")
        exit()

print(coffe_needed)
