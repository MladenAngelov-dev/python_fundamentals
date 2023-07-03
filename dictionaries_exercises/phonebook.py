phonebook = {}

while True:
    command = input()
    if "-" not in command:
        break
    name, phone_number = command.split("-")
    phonebook[name] = phone_number

for search in range(int(command)):
    search_name = input()
    if search_name in phonebook.keys():
        print(f"{search_name} -> {phonebook[search_name]}")
    else:
        print(f"Contact {search_name} does not exist.")
