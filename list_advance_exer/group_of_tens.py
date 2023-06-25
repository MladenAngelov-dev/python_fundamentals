list_of_numbers = input().split(", ")
group = 10

while True:

    current_list = []

    for num in list_of_numbers:
        if int(num) <= group:
            current_list.append(num)
            list_of_numbers.remove(num)
            continue

    print(f"Group of {group}'s: {current_list}")
    group += 10

    if len(list_of_numbers) <=0:
        break