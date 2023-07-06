first_string = input()
second_string = input()

while first_string in second_string:
    filtered_string = second_string.replace(first_string, "")
    second_string = filtered_string
print(filtered_string)