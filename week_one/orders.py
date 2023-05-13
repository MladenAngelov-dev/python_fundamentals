num_orders = int(input())

total_price = 0

for i in range(num_orders):
    capsule_price = float(input())
    days = int(input())
    capsules_per_dey = int(input())
    if capsule_price < 0.01 or capsule_price > 100:
        continue
    elif days < 1 or days > 31:
        continue
    elif capsules_per_dey < 1 or capsules_per_dey > 2000:
        continue
    price = capsule_price * days * capsules_per_dey
    total_price += price
    print(f"The price for the coffee is: ${price:.2f}")

print(f"Total: ${total_price:.2f}")
