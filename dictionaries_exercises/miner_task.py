resources = {}

while True:
    resource_type = input()

    if resource_type == "stop":
        break
    if resource_type not in resources:
        resources[resource_type] = 0
    quantity = int(input())
    resources[resource_type] += quantity

for resource, value in resources.items():
    print(f"{resource} -> {value}")

