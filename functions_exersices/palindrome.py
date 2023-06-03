def check_palindrome(some_number):
    if some_number == some_number[::-1]:
        return True
    return False


numbers = input().split(", ")
for nuber in numbers:
    print(check_palindrome(nuber))
