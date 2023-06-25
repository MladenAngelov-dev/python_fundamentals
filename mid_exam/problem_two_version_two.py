def travel_to_titan(input_lines):
    commands = input_lines[0].split("||")
    fuel = int(input_lines[1])
    ammo = int(input_lines[2])

    for command in commands:
        command_parts = command.split()
        if command_parts[0] == "Travel":
            distance = int(command_parts[1])
            if fuel >= distance:
                fuel -= distance
                print(f"The spaceship travelled {distance} light-years.")
            else:
                print("Mission failed.")
                return

        elif command_parts[0] == "Enemy":
            enemy_armor = int(command_parts[1])
            if ammo >= enemy_armor:
                ammo -= enemy_armor
                print(f"An enemy with {enemy_armor} armour is defeated.")
            else:
                fuel_needed = 2 * (enemy_armor - ammo)
                if fuel >= fuel_needed:
                    fuel -= fuel_needed
                    print(f"An enemy with {enemy_armor} armour is outmaneuvered.")
                else:
                    print("Mission failed.")
                    return

        elif command_parts[0] == "Repair":
            fuel_added = int(command_parts[1])
            ammo_added = 2 * fuel_added
            fuel += fuel_added
            ammo += ammo_added
            print(f"Ammunitions added: {ammo_added}.")
            print(f"Fuel added: {fuel_added}.")

        if fuel < 0:
            print("Mission failed.")
            return

        if command_parts[0] == "Titan":
            print("You have reached Titan, all passengers are safe.")
            return

input_lines = []
for i in range(3):
    line = input()
    input_lines.append(line)

travel_to_titan(input_lines)
