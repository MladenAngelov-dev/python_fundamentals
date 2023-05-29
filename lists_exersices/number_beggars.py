income = input().split(", ")
num_beggars = int(input())

income_digits = []

for symbol in income:
    income_digits.append(int(symbol))

total_income = []
start_index = 0

while start_index < num_beggars:
    current_beggar_sum = 0
    for index in range(start_index, len(income_digits), num_beggars):
        current_beggar_sum += income_digits[index]
    total_income.append(current_beggar_sum)
    start_index += 1
print(total_income)
