num_lines = int(input())
tank_capacity = 255
total_water = 0

for current_line in range(num_lines):
    litters_water = int(input())
    if tank_capacity - litters_water < 0:
        print("Insufficient capacity!")
        continue
    tank_capacity -= litters_water
    total_water += litters_water
print(total_water)
