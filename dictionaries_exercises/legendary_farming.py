legendary_items = {"shards": 0, "fragments": 0, "motes": 0}

is_optained = False
legendary = ''
lines_of_materials = input().split()

while not is_optained:
    for index in range(0, len(lines_of_materials), 2):
        value = int(lines_of_materials[index])
        key = lines_of_materials[index + 1].lower()
        if key not in legendary_items.keys():
            legendary_items[key] = 0
        legendary_items[key] += value

        if legendary_items["shards"] >= 250:
            is_optained = True
            legendary_items["shards"] -= 250
            legendary = "Shadowmourne"

        elif legendary_items["fragments"] >= 250:
            is_optained = True
            legendary = "Valanyr"
            legendary_items["fragments"] -=250

        elif legendary_items["motes"] >= 250:
            is_optained = True
            legendary = "Dragonwrath"
            legendary_items["motes"] -= 250
        if is_optained:
            break
    if is_optained:
        break
    lines_of_materials = input().split()

print(f"{legendary} obtained!")
for key, value in legendary_items.items():
    print(f"{key}: {value}")
