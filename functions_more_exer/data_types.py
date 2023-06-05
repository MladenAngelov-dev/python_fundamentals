def data_process(type_of_data, char):
    if type_of_data == "int":
        char = int(char)
        return char * 2
    elif type_of_data == "real":
        char = float(char) * 1.5
        formated_char = "{:.2f}".format(char)
        return formated_char
    else:
        char = '$' + f"{char}" + '$'
        return char


data_type = input()
characters = input()
result = data_process(data_type, characters)
print(result)