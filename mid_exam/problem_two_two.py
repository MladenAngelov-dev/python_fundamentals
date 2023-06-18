def travel(distance, fuel):
    if fuel >= distance:
        print(f"The spaceship travelled {distance} light-years.")
        return fuel - distance
    else:
        print("Mission failed.")
        return fuel


def enemy(enemy_armor, ammunition, fuel):
    if ammunition > enemy_armor:
        print(f"An enemy with {enemy_armor} armour is defeated.")
    else:
        if fuel > 2 * enemy_armor:
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
fuel = int(input())
ammunition = int(input())

for command in commands:
    comm = command.split(" ")
    action = comm[0]
    value = comm[1]
    if action == "Titan":
        print("You have reached Titan, all passengers are safe.")
        break
    elif action == "Travel":
        fuel = travel(int(value), fuel)
    elif action == "Enemy":
        enemy_armor = int(value)
        ammunition, fuel = enemy(enemy_armor, ammunition, fuel)
    elif action == "Repair":
        number = int(value)
        ammunition, fuel = repair(number, ammunition, fuel)
