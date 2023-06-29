products = {}

while True:
    command = input()
    if command == "statistics":
        break

    product, quantity = command.split(': ')
    quantity = int(quantity)

    if product in products:
        products[product] += quantity
    else:
        products[product] = quantity

products_count = len(products)
total_quantity = sum(products.values())

print("Products in stock:")
for product, quantity in products.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {products_count}")
print(f"Total Quantity: {total_quantity}")