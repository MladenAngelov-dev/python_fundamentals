cards = input().split(" ")
shuffles = int(input())

for index in range(shuffles):
    half = len(cards) // 2
    left_side = cards[:half]
    right_side = cards[half:]

    shuffled_cards = []
    for shuffle in range(half):
        shuffled_cards.append(left_side[shuffle])
        shuffled_cards.append(right_side[shuffle])
    cards = shuffled_cards
print(cards)