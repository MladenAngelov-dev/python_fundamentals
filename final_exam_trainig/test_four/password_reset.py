def take_odd(passw):
    result = ''
    for index in range(len(passw)):
        if index % 2 != 0:
            result += passw[index]
    return result


def cut(passw, start, remove):
    result = ""
    stop = start + remove
    result += passw[:start] + passw[stop:]
    return result


def substitute(pasw, sub, rep):
    new_pass = pasw
    if sub in pasw:
        new_pass = pasw.replace(sub, rep)
        print(new_pass)
    else:
        print("Nothing to replace!")
    return new_pass


password = input()
command = input()
while command != "Done":
    command = command.split()
    if command[0] == "TakeOdd":
        password = take_odd(password)
        print(password)

    elif command[0] == "Cut":
        start_index = int(command[1])
        signs_to_cut = int(command[2])
        password = cut(password, start_index, signs_to_cut)
        print(password)

    elif command[0] == "Substitute":
        substring = command[1]
        replace = command[2]
        password = substitute(password, substring, replace)

    command = input()
print(f"Your password is: {password}")