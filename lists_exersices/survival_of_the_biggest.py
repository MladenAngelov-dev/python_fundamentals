numbers = input().split(" ")
count_to_remove = int(input())

numbers_digits = []
for digit in numbers:
    numbers_digits.append(int(digit))
filtered_digits = sorted(numbers_digits)[count_to_remove:]

new_list = []
for number in numbers_digits:
    if number in filtered_digits:
        new_list.append(number)

print(*new_list, sep=", ")
