import re

pattern = r"(w{3}\.[a-zA-Z0-9-\.]+\.[a-z]+)"

lines = input()
valid_url = []
while lines:
    extracted_links = re.search(pattern, lines)
    if extracted_links:
        valid_url.append(extracted_links[1])

    lines = input()
for valid in valid_url:
    print(valid)