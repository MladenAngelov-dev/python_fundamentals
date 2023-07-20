def decrypting_message(message):

    while True:
        command = input()

        if command.startswith('Reveal'):
            print(f"You have a new text message: {message}")
            break

        elif command.startswith("InsertSpace"):
            pass

        elif command.startswith("Reverse"):
            pass

        elif command.startswith("ChangeAll"):
            pass



data = input()
decrypting_message(data)