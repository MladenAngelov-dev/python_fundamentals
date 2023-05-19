number_of_characters = int(input())
total_sum = 0

for i in range(number_of_characters):
    characters = input()
    total_sum += ord(characters)

print(f"The sum equals: {total_sum}")