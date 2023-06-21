#   orn_set =  2$ and 5 points
#   tree_skirt = 5$ and 3 points
#   garland = 3$ and 10 points
#   lights  = 15 $ and 17 points
ORNAMENT_PRICE = 2
SKIRT_PRICE = 5
GARLAND_PRICE = 3
LIGHTS_PRICE = 15

ORNAMENT_POINTS = 5
SKIRT_POINTS = 3
GARLAND_POINTS = 10
LIGHTS_POINTS = 17

quantity = int(input())
days_to_christmas = int(input())

total_price = 0
total_spirit = 0


for day in range(1, days_to_christmas + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        total_price += ORNAMENT_PRICE * quantity
        total_spirit += ORNAMENT_POINTS
    if day % 3 == 0:
        total_price += SKIRT_PRICE * quantity + GARLAND_PRICE * quantity
        total_spirit += SKIRT_POINTS + GARLAND_POINTS
    if day % 5 == 0:
        total_price += LIGHTS_PRICE * quantity
        total_spirit += LIGHTS_POINTS
        if day % 3 == 0:
            total_spirit += 30
    if day % 10 == 0:
        total_spirit -= 20
        total_price += GARLAND_PRICE + SKIRT_PRICE + LIGHTS_PRICE

if days_to_christmas % 10 == 0:
    total_spirit -= 30
print(f"Total cost: {total_price}")
print(f"Total spirit: {total_spirit}")
