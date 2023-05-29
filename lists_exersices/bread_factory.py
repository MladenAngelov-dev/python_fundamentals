events = input().split("|")
total_energy = 100
total_coins = 100
factory_open = True

for event in events:
    clean_event = event.split("-")
    event_name = clean_event[0]
    event_value = int(clean_event[1])

    if event_name == "rest":
        current_energy = total_energy
        total_energy += event_value
        if total_energy > 100:
            total_energy = 100
        gained_energy = total_energy - current_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {total_energy}.")

    elif event_name == "order":
        if total_energy >= 30:
            total_coins += event_value
            total_energy -= 30
            print(f"You earned {event_value} coins.")
        else:
            print("You had to rest!")
            total_energy += 50

    else:
        if total_coins >= event_value:
            total_coins -= event_value
            print(f"You bought {event_name}.")
        else:
            print(f"Closed! Cannot afford {event_name}.")
            factory_open = False
            break

if factory_open:
    print("Day completed!")
    print(f"Coins: {total_coins}")
    print(f"Energy: {total_energy}")
