import re


def check_num(code, grp):
    for sym in code[0]:
        if sym.isdigit():
            grp += sym
        if grp == "":
            grp += "00"
    print(f"Product group: {grp}")


number = int(input())
pattern = "@#+[A-Za-z0-9]+@#+"

for _ in range(number):
    grp = ""
    barcode = input()
    match = re.findall(pattern, barcode)
    if match:
        check_num(match, grp)

    else:
        print("Invalid barcode")