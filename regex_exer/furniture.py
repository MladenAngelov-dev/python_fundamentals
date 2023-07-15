import re

pattern = r">>([a-zA-z]+)<<([0-9\.]+)!([0-9]+)"
furniture = []
total_price = 0
command = input()
while command != "Purchase":
    match = re.search(pattern, command)
    if match:
        item, price, quantity = match.groups()
        total_price += float(price) * int(quantity)
        furniture.append(item)
    command = input()
print("Bought furniture:")
for one in furniture:
    print(one)
print(f"Total money spend: {total_price:.2f}")