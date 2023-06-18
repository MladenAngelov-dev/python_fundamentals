def travel(fuel, distance):
    if fuel >= distance:
        fuel -= distance
        print(f"The spaceship travelled {distance} light-years.")
    else:
        print("Mission failed.")
    return fuel


def enemy():
    pass


def repair():
    pass


commands_list = input().split("||")
starting_fuel = int(input())
starting_ammo = int(input())


for commands in commands_list:
    command = commands.split()
    target = command[0]
    if target == "Titan":
        break
    number = command[1]
    if target == "Travel":
        travel(starting_fuel, int(number))

print(starting_fuel)