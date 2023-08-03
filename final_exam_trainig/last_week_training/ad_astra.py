import re

data = input()
pattern = r"([#|\|])([A-Za-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d{1,5})\1"
matches = re.findall(pattern, data)

total_calories = 0
food_supply = 0
if matches:
    for match in matches:
        calories = int(match[3])
        total_calories += calories
        food_supply = total_calories // 2000
print(f"You have food to last you for: {food_supply} days!")

for match in matches:
    calories = int(match[3])
    food_name = match[1]
    exp_date = match[2]
    print(f"Item: {food_name}, Best before: {exp_date}, Nutrition: {calories}")
