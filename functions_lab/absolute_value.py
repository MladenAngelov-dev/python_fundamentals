list_numbers = input().split(" ")
list_num = []
for number in list_numbers:
    list_num.append(abs(float(number)))
print(list_num)