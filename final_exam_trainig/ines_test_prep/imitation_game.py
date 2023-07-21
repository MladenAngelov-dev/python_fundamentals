decrypted_message = input()

data = input()

while data !="Decode":
    splitted_data = data.split()
    command = splitted_data[0]

    if command == "Move":
        n_letters = int(splitted_data[1])
        decrypted_message = decrypted_message[n_letters:] + decrypted_message[:n_letters]

    if command == "Insert":
        index = int(splitted_data[1])
        substing = splitted_data[2]
        decrypted_message = decrypted_message[:index] + substing + decrypted_message[index:]

    if command == "ChangeAll":
        sub_string = splitted_data[1]
        replacement = splitted_data[2]
        decrypted_message = decrypted_message.replace(sub_string, replacement)
    data = input()

print(f"The decrypted message is: {decrypted_message} ")
