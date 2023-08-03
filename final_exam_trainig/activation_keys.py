def contains(raw, substring):
    if substring in raw:
        return f"{raw} contains {substring}"
    return "Substring not found!"


def flip_upper(raw, start, end):
    new_string = ""
    for index in range(len(raw)):
        if start <= index < end:
            new_string += raw[index].upper()
        else:
            new_string += raw[index]
    return new_string


def flip_lower(raw, start, end):
    new_string = ""
    for index in range(len(raw)):
        if start <= index < end:
            new_string += raw[index].lower()
        else:
            new_string += raw[index]
    return new_string


def remove_characters(raw, start, end):
    new_string = ""
    for index in range(len(raw)):
        if start <= index < end:
            continue
        else:
            new_string += raw[index]
    return new_string


raw_key = input()

command = input()

while command != "Generate":
    working_command = command.split(">>>")

    if working_command[0] == "Contains":
        sub_string = working_command[1]
        result = contains(raw_key, sub_string)
        print(result)

    elif working_command[0] == "Flip":
        if working_command[1] == "Upper":
            start_index = int(working_command[2])
            end_index = int(working_command[3])
            raw_key = flip_upper(raw_key, start_index, end_index)
            print(raw_key)

        else:
            start_index = int(working_command[2])
            end_index = int(working_command[3])
            raw_key = flip_lower(raw_key, start_index, end_index)
            print(raw_key)

    elif working_command[0] == "Slice":
        start_index = int(working_command[1])
        end_index = int(working_command[2])
        raw_key = remove_characters(raw_key, start_index, end_index)
        print(raw_key)

    command = input()

activationkey = raw_key
print(f"Your activation key is: {activationkey}")