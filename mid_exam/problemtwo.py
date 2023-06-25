def travel(distance, fuel):
    if fuel >= distance:
        return f"The spaceship travelled {distance} light-years."
    else:
        return "Mission failed."


def enemy(enemy_armor, ammunition, fuel):
    if ammunition > enemy_armor:
        return f"An enemy with {enemy_armor} armour is defeated."
    else:
        if fuel >= 2 * enemy_armor:
            fuel -= 2 * enemy_armor
            return f"An enemy with {enemy_armor} armour is outmaneuvered."
        else:
            return "Mission failed."


def repair(number, ammunition, fuel):
    ammunition += number * 2
    fuel += number
    return f"Ammunitions added: {number * 2}. Fuel added: {number}."


commands = input().split("||")
starting_fuel = int(input())
starting_ammo = int(input())
output = []

for command in commands:
    action, value = command.split()

    if action == "Titan":
        output.append("Mission failed.")
        output.append("You have reached Titan, all passengers are safe.")
        break

    elif action == "Travel":
        output.append(travel(int(value), starting_fuel))
        starting_fuel -= int(value)

    elif action == "Enemy":
        output.append(enemy(int(value), starting_ammo, starting_fuel))
        starting_ammo -= int(value)

    elif action == "Repair":
        repair_output = repair(int(value), starting_ammo, starting_fuel)
        output.append(repair_output)
        repair_values = repair_output.split()def travel(distance, fuel):
    if fuel >= distance:
        print(f"The spaceship travelled {distance} light-years.")
        return fuel - distance
    else:
        print("Mission failed.")
        return fuel


def enemy(enemy_armor, ammunition, fuel):
    if ammunition >= enemy_armor:
        print(f"An enemy with {enemy_armor} armour is defeated.")
    else:
        if fuel >= 2 * enemy_armor:
            fuel -= 2 * enemy_armor
            print(f"An enemy with {enemy_armor} armour is outmaneuvered.")
        else:
            print("Mission failed.")
    return ammunition, fuel


def repair(number, ammunition, fuel):
    ammunition += number * 2
    fuel += number
    print(f"Ammunitions added: {number * 2}.")
    print(f"Fuel added: {number}.")
    return ammunition, fuel


commands = input().split("||")
starting_fuel = int(input())
starting_ammo = int(input())

for command in commands:
    command_parts = command.split()
    action = command_parts[0]

    if len(command_parts) == 2:
        value = int(command_parts[1])
    else:
        value = None

    if action == "Titan":
        print("You have reached Titan, all passengers are safe.")
        break

    elif action == "Travel":
        if value is not None:
            starting_fuel = travel(value, starting_fuel)

    elif action == "Enemy":
        if value is not None:
            starting_ammo, starting_fuel = enemy(value, starting_ammo, starting_fuel)

    elif action == "Repair":
        if value is not None:
            starting_ammo, starting_fuel = repair(value, starting_ammo, starting_fuel)

        starting_ammo = int(repair_values[2].rstrip("."))
        starting_fuel = int(repair_values[6].rstrip("."))

print(" ".join(output))
