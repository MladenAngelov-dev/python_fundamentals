numbers = input().split()
digits = []
for num in numbers:
    digits.append(int(num))
print(f"The minimum number is {min(digits)}")
print(f"The maximum number is {max(digits)}")
print(f"The sum number is: {sum(digits)}")