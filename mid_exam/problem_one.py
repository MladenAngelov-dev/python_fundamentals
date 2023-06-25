number_of_cites = int(input())
total_profit = 0
city_counter = 0
for num in range(number_of_cites):
    city_name = input()
    profit = float(input())
    expenses = float(input())
    city_counter += 1
    if city_counter % 3 == 0 and city_counter % 5 != 0:
        expenses = expenses * 1.50
    elif city_counter % 5 == 0:
        profit = profit * 0.9
    current_city_profit = profit - expenses
    total_profit += current_city_profit

    print(f"In {city_name} Burger Bus earned {current_city_profit:.2f} leva.")
print(f"Burger Bus total profit: {total_profit:.2f} leva.")