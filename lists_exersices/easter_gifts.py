gifts = input().split()

while True:
    command = input()
    if command == "No Money":
        break
    type_command = command.split()
    if command[0] == "OutOfStock":
        if command[1] in gifts:
            pass


