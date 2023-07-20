some_string = input()
new_string = ""
explosion = 0

for index in range(len(some_string)):
    if explosion > 0 and some_string[index] != ">":
        explosion -= 1
    elif some_string[index] == ">":
        new_string += some_string[index]
        explosion += int(some_string[index + 1])
    else:
        new_string += some_string[index]

print(new_string)