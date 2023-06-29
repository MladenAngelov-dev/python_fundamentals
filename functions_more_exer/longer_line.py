from math import floor


def print_longer_line(x1, y1, x2, y2, x3, y3, x4, y4):
    distance1 = x1**2 + y1**2
    distance2 = x2**2 + y2**2

    if distance1 <= distance2:
        closest_x = x1
        closest_y = y1
        farthest_x = x2
        farthest_y = y2
    else:
        closest_x = x2
        closest_y = y2
        farthest_x = x1
        farthest_y = y1

    distance3 = x3**2 + y3**2
    distance4 = x4**2 + y4**2

    if distance3 <= distance4:
        closest_x2 = x3
        closest_y2 = y3
        farthest_x2 = x4
        farthest_y2 = y4
    else:
        closest_x2 = x4
        closest_y2 = y4
        farthest_x2 = x3
        farthest_y2 = y3

    length1 = (farthest_x - closest_x)**2 + (farthest_y - closest_y)**2
    length2 = (farthest_x2 - closest_x2)**2 + (farthest_y2 - closest_y2)**2

    if length1 >= length2:
        closest_point = f"({floor(closest_x)}, {floor(closest_y)})({floor(farthest_x)}, {floor(farthest_y)})"
    else:
        closest_point = f"({floor(closest_x2)}, {floor(closest_y2)})({floor(farthest_x2)}, {floor(farthest_y2)})"
    return closest_point


x_one = float(input())
y_one = float(input())
x_two = float(input())
y_two = float(input())
x_three = float(input())
y_three = float(input())
x_four = float(input())
y_four = float(input())
center = print_longer_line(x_one, y_one, x_two, y_two, x_three, y_three, x_four, y_four)
print(center)
