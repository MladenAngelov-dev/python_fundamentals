number = int(input())
count = int(input())

new_list = []

for numb in range(1, count+1):
    new_list.append(numb * number)

print(new_list)