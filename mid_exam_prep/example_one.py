
starting_energy = int(input())
distance = input()
battles_won = 0

while distance != "End of battle":
    distance = int(distance)
    if starting_energy >= distance and starting_energy > 0:
        starting_energy -= distance
        battles_won += 1

        if battles_won % 3 == 0:
            starting_energy += battles_won

    else:
        print(f"Not enough energy! Game ends with {battles_won} won battles and {starting_energy} energy")
        break

    distance = input()
else:
    print(f"Won battles: {battles_won}. Energy left: {starting_energy}")
