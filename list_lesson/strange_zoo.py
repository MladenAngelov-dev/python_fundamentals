tail = input()
body = input()
head = input()

correct_arrangement = [tail, body, head]
correct_arrangement[0], correct_arrangement[2] = correct_arrangement[2], correct_arrangement[0]
print(correct_arrangement)