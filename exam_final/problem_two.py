import re

pattern = r"^^(\S+)\>(\d{3})\|([a-z]{3})\|([A-Z]{3})\|([^<>]{3})\<\1$"

lines = int(input())
valid_password = []
for _ in range(lines):
    password = input()
    matched = re.findall(pattern, password)
    if matched:
        for match in matched:
            print(f"Password: {match[1] + match[2] + match[3] + match[4]}")
    else:
        print("Try another password!")
