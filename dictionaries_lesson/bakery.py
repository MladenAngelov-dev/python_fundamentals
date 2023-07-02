ingredients = input().split()
bakery = {}

for i in range(0, len(ingredients), 2):
    product = ingredients[i]
    quantity = ingredients[i + 1]
    bakery[product] = int(quantity)

print(bakery)