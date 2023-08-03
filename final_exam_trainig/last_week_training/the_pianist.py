
lines = int(input())
pieces = {}
for _ in range(lines):
    piece, composer, key = input().split("|")
    pieces[piece] = [composer, key]

command = input()
while command != "Stop":
    command = command.split("|")

    if command[0] == "Add":
        new_piece = command[1]
        new_composer = command[2]
        new_key = command[3]
        if new_piece not in pieces:
            pieces[new_piece] = [new_composer, new_key]
            print(f"{new_piece} by {new_composer} in {new_key} added to the collection!")
        else:
            print(f"{new_piece} is already in the collection!")

    elif command[0] == "Remove":
        piece_to_remove = command[1]
        if piece_to_remove in pieces:
            del pieces[piece_to_remove]
            print(f"Successfully removed {piece_to_remove}!")
        else:
            print(f"Invalid operation! {piece_to_remove} does not exist in the collection.")

    elif command[0] == "ChangeKey":
        new_piece = command[1]
        new_key = command[2]
        if new_piece in pieces:
            pieces[new_piece][1] = new_key
            print(f"Changed the key of {new_piece} to {new_key}!")
        else:
            print(f"Invalid operation! {new_piece} does not exist in the collection.")

    command = input()

for names, value in pieces.items():
    compser = value[0]
    tone = value[1]
    print(f"{names} -> Composer: {compser}, Key: {tone}")