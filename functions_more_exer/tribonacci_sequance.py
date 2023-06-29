def tribonacci(some_number):
    first = 1
    second = 1
    third = 2
    print(first, end=" ")
    print(second, end=" ")
    print(third, end=" ")
    for i in range(3, some_number):
        curr = first + second + third
        first = second
        second = third
        third = curr
        print(curr, end=" ")

number = int(input())
numbers = tribonacci(number)

