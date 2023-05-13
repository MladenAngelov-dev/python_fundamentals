command = input()

while command != "End":
    if command != "SoftUni":
        new_command = ""
        for char in command:
            new_command += char * 2
        print(new_command)
    command = input()
