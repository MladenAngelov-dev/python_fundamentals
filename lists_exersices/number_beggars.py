income = input().split(", ")
num_beggars = int(input())

income_digits = []

for symbol in income:
    income_digits.append(int(symbol))

total_income =[]
start_index = 0

while start_index < num_beggars:

