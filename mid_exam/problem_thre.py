def add_card(cards, new_card):
    if new_card in cards:
        print("Card is already in the deck")
    else:
        cards.append(new_card)
        print("Card successfully added")

def remove_card(cards, new_card):
    if new_card in cards:
        cards.remove(new_card)
        print("Card successfully removed")
    else:
        print("Card not found")

def remove_at_index(cards, index):
    if index < len(cards):
        cards.pop(index)
        print("Card successfully removed")
    else:
        print("Index out of range")

def insert_at_index(cards, index, new_card):
    if index <= len(cards):
        if new_card in cards:
            print("Card is already added")
        else:
            cards.insert(index, new_card)
            print("Card successfully added")
    else:
        print("Index out of range")


cards_list = input().split(", ")
number = int(input())

for _ in range(number):
    command = input().split(", ")
    action = command[0]

    if action == "Add":
        add_card(cards_list, command[1])
    elif action == "Remove":
        remove_card(cards_list, command[1])
    elif action == "Remove At":
        remove_at_index(cards_list, int(command[1]))  # Fix the index to command[1]
    elif action == "Insert":
        insert_at_index(cards_list, int(command[1]), command[2])

print(", ".join(cards_list))
