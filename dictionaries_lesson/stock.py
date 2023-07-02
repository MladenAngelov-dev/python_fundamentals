ingredients = input().split()
products = {}

for i in range(0, len(ingredients), 2):
    product = ingredients[i]
    quantity = ingredients[i + 1]
    products[product] = quantity


serched_product = input().split()
for word in serched_product:
    if word in products:
        print(f"We have {products[word]} of {word} left")
    else:
        print(f"Sorry, we don't have {word}")