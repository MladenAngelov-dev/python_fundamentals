def length(username):
    if 3 <= len(username) <= 16:
        return True
    return False


def correct_syntax(username):
    for char in username:
        if not (char.isalnum() or char == "-" or char == "_"):
            return False
    return True


def no_redundant_symbol(username):
    if " " in username:
        return False
    return True


def is_valid(username):
    if no_redundant_symbol(username) and correct_syntax(username) and length(username):
        return True
    return False


user_names = input().split(", ")

for user_name in user_names:
    if is_valid(user_name):
        print(user_name)