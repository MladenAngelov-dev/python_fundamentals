
def sum_numbers(a: int, b: int) -> int:
    return a+b


for _ in range(3):
    a = int(input())
    b = int(input())
    result = sum_numbers(a, b)
    print(result)
