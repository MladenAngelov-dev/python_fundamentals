def next_version(number):
    numbers = int("".join(number)) + 1
    number_digits = [num for num in str(numbers)]
    return number_digits


version = input().split(".")
print(".".join(next_version(version)))