

capacity = int(input())

command = input()
users = {}
while command != "Statistics":
    command = command.split("=")
    action = command[0]
    if action == "Add":
        name = command[1]
        sent = int(command[2])
        received = int(command[3])

        if name not in users:
            users[name] = [sent, received]

    elif action == "Message":
        sender = command[1]
        receiver = command[2]
        if sender in users and receiver in users:
            users[sender][0] += 1
            users[receiver][1] += 1
        if users[sender][0] + users[sender][1] >= capacity:
            del users[sender]
            print(f"{sender} reached the capacity!")
        if users[receiver][1] + users[receiver][0] >= capacity:
            del users[receiver]
            print(f"{receiver} reached the capacity!")

    elif action == "Empty":
        user_name = command[1]
        if user_name in users:
            del users[user_name]
        elif user_name == "All":
            del users
            users = {}

    command = input()

total = len(users)
print(f"Users count: {total}")
for key, value in users.items():
    send = value[0]
    recv = value[1]
    total_msg = send + recv
    print(f"{key} - {total_msg}")