import re


def check_num(code,):
    digit = re.findall("\d", code)
    if digit:
        grp = "".join(digit)
    else:
        grp = "00"

number = int(input())
pattern = "@#+[A-Za-z0-9]+@#+"

for _ in range(number):
    barcode = input()
    match = re.findall(pattern, barcode)
    if match:
        print(f"Product group: {check_num(match)}")

    else:
        print("Invalid barcode")