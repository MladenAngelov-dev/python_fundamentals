def first_in_second(first,  second):
    filtered_line = []
    for string in first:
        for second_string in second:
            if string in second_string:
                filtered_line.append(string)
                break
    return filtered_line


first_line = input().split(", ")
second_line = input().split(", ")
print(first_in_second(first_line, second_line))