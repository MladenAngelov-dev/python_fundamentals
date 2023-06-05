from math import floor

def closes_to_center(x1, y1, x2, y2):
    distance_one = (x1**2 + y1**2) + (x2**2 + y2**2)
    distance_two = (x2**2 + y2**2) + (x1**2 + y1**2)
    if distance_one <= distance_two:
        closest_point = f"({floor(x1)}, {floor(y1)})({floor(x2)}, {floor(y2)})"
    else:
        closest_point = f"({floor(x2)}, {floor(y2)})({floor(x1)}, {floor(y1)})"


    return closest_point


for line in range(2):
    x_one = float(input())
    y_one = float(input())
    x_two = float(input())
    y_two = float(input())
center = closes_to_center(x_one, y_one, x_two, y_two)
print(center)