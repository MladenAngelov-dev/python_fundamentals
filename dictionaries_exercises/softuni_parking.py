

parking_space = {}
number_commands = int(input())

for command in range(number_commands):
    current_command = input().split()
    if current_command[0] == "register":
        name, reg_number = current_command[1], current_command[2]
        if name not in parking_space:
            parking_space[name] = reg_number
            print(f"{name} registered {reg_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {parking_space[name]}")
    else:
        name = current_command[1]
        if name not in parking_space:
            print(f"ERROR: user {name} not found")
        else:
            print(f"{name} unregistered successfully")
            del parking_space[name]

for key, value in parking_space.items():
    print(f"{key} => {value}")