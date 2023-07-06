while True:
    command = input()
    if command == "end":
        break
    reverse_string = command[::-1]
    print(f"{command} = {reverse_string}")