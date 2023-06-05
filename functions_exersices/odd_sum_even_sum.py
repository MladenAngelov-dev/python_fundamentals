def odd_even_sum(some_number):
    sum_of_odd = 0
    sum_of_even = 0
    for digit in some_number:
        if int(digit) % 2 == 0:
            sum_of_even += int(digit)
        else:
            sum_of_odd += int(digit)
    return sum_of_odd, sum_of_even


number = input()
odd_digits, even_digits = odd_even_sum(number)
print(f"Odd sum = {odd_digits}, Even sum = {even_digits}")