# 1 loaf =  1pack of eggs + 1kg flour + 0.250 l milk

budget = float(input())
flour = float(input())

eggs = flour * 0.75
milk = (1.25 * flour) / 4
one_loaf = flour + milk + eggs
counter = 0
colored_eggs = 0

while True:
    if budget >= one_loaf:
        counter += 1
        colored_eggs += 3
        budget -= one_loaf
        if counter % 3 == 0:
            colored_eggs -= counter - 2
    else:
        break

print(f"You made {counter} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")