from math import ceil

num_of_people = int(input())
capacity = int(input())

courses = ceil(num_of_people / capacity)
print(courses)