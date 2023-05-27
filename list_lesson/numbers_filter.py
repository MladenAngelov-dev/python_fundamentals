number = int(input())
numbers = []
filtered_numbers = []

for numb in range(number):
    new_number = int(input())
    numbers.append(new_number)

command = input()
if command == "even":
    for numb in numbers:
        if numb % 2 == 0:
            filtered_numbers.append(numb)
elif command == "odd":
    for numb in numbers:
        if numb % 2 != 0:
            filtered_numbers.append(numb)
elif command == "negative":
    for numb in numbers:
        if numb < 0:
            filtered_numbers.append(numb)
elif command == "positive":
    for numb in numbers:
        if numb >= 0:
            filtered_numbers.append(numb)

print(filtered_numbers)