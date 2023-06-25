def travel_to_titan(input_lines):
    commands = input_lines[0].split("||")
    fuel = int(input_lines[1])
    ammo = int(input_lines[2])

    if commands[0] == "Travel":
        distance = int(commands[1])
        if fuel >= distance:
            fuel -= distance
            print(f"Spaceship traveled {distance} light years.")
        else:
            print("Mission failed.")
            return

    elif commands[0] == "Enemy":
        enemy_armor = int(commands[1])
        if ammo >= enemy_armor:
            ammo -= enemy_armor
            print(f"An enemy with {enemy_armor} defeated.")
        else:
            fuel_needed = 2 * (enemy_armor - ammo)
            if fuel >= fuel_needed:
                fuel -= fuel_needed
                print(f"An enemy with {enemy_armor} outmaneuvered.")
            else:
                print("Mission failed.")
                return

    elif commands[0] == "Repair":
        fuel_added = int(commands[1])
        ammo_added = 2 * fuel_added
        fuel += fuel_added
        ammo += ammo_added
        print(f"Ammo added: {ammo_added}")
        print(f"Fuel added: {fuel_added}")

    if fuel >= 0:
        print("All passengers are safe.")

input_lines = []
for i in range(3):
    line = input()
    input_lines.append(line)

travel_to_titan(input_lines)
