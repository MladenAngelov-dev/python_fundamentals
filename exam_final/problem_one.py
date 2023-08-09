

spell = input()

command = input()

while command != "Abracadabra":
    command = command.split()
    action = command[0]
    if action == "Abjuration":
        spell = spell.upper()
        print(spell)

    elif action == "Necromancy":
        spell = spell.lower()
        print(spell)

    elif action == "Illusion":
        start_index = int(command[1])
        letter = command[2]
        if 0 <= start_index < len(spell):
            spell = spell[:start_index] + letter + spell[start_index +1:]
            print("Done!")
        else:
            print("The spell was too weak.")

    elif action == "Divination":
        sub_string = command[1]
        replace_string = command[2]
        if sub_string in spell:
            spell = spell.replace(sub_string, replace_string)
            print(spell)

    elif action == "Alteration":
        sub_string = command[1]
        if sub_string in spell:
            spell = spell.replace(sub_string, "")
            print(spell)

    else:
        print("The spell did not work!")

    command = input()