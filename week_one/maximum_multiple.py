divisor = int(input())
boundary = int(input())

largest_divisor = 0

for number in range(boundary, divisor - 1, -1):
    if number % divisor == 0:
        largest_divisor = number
        break

print(largest_divisor)