def move(msg, number):
    if number in range(len(msg)):
        msg = msg[number:] + msg[:number]
    return msg


def insert_string(msg, number, substring):
    msg = msg[:number] + substring + msg[number:]
    return msg


def change_all(msg, sub, rep):
    if sub in msg:
        msg = msg.replace(sub, rep)
    return msg


message = input()

command = input()
while command != "Decode":
    command = command.split("|")
    if command[0] == "Move":
        number_of_letters = int(command[1])
        message = move(message, number_of_letters)

    elif command[0] == "Insert":
        index = int(command[1])
        string = command[2]
        message = insert_string(message, index, string)
    elif command[0] == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        message = change_all(message, substring, replacement)

    command = input()

print(f"The decrypted message is: {message}")