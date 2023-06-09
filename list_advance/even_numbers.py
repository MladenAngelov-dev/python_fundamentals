def even_index(numbers):
    even_indexes = []
    for index, number in enumerate(numbers):
        if int(number) % 2 == 0:
            even_indexes.append(index)
    return even_indexes


list_numbers = input().split(", ")
result = even_index(list_numbers)
print(result)