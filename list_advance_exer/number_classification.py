def sorted_numbers(some_number):
    positive_number = [numb for numb in some_number if int(numb) >= 0]
    print (f"Positive: {', '.join(positive_number)}")
    negative_number = [numb for numb in some_number if int(numb) < 0]
    print (f"Negative: {', '.join(negative_number)}")
    even = [numb for numb in some_number if int(numb) % 2 == 0]
    print (f"Even: {', '.join(even)}")
    odd = [numb for numb in some_number if int(numb) % 2 != 0]
    print (f"Odd: {', '.join(odd)}")


numbers = input().split(", ")
sorted_numbers(numbers)
