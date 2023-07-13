towns = {}

while True:
    command = input()
    if command == "Sail":
        break
    command = command.split("||")
    town_name = command[0]
    population = int(command[1])
    gold = int(command[2])
    if town_name not in towns:
        towns[town_name] = [population, gold]
    else:
        towns[town_name][0] += population
        towns[town_name][1] += gold

while True:
    command = input()
    if command == "End":
        break
    command = command.split("=>")
    if command[0] == "Plunder":
        town = command[1]
        people = int(command[2])
        gold = int(command[3])
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        towns[town][0] -= people
        towns[town][1] -= gold
        if towns[town][0] <= 0 or towns[town][1] <= 0:
            print(f"{town} has been wiped off the map!")
            del towns[town]
    elif command[0] == "Prosper":
        town = command[1]
        gold = int(command[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
            continue
        else:
            towns[town][1] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {towns[town][1]} gold.")

if len(towns) == 0:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(towns)} wealthy settlements to go to:")
    for key, value in towns.items():
        town_population = value[0]
        income = value[1]
        print(f"{key} -> Population: {town_population} citizens, Gold: {income} kg")