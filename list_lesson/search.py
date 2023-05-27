number_lines = int(input())
password = input()

lines = []
filtered_lines = []

for line in range(number_lines):
    new_line = input()
    lines.append(new_line)
    if password in new_line:
        filtered_lines.append(new_line)

print(lines)
print(filtered_lines)
