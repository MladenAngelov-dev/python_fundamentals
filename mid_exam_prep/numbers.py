FIRST_COUNT = 5

numbers = [int(x) for x in input().split()]
average = sum(numbers) / len(numbers)
filtered_numbers = sorted([x for x in numbers if x > average])

if not filtered_numbers:
    print("No")
else:
    for i in range(FIRST_COUNT):
        if filtered_numbers:
            print(filtered_numbers.pop(), end=" ")