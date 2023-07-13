number_of_students = int(input())
students_grades = {}

for _ in range(number_of_students):
    name = input()
    grade = float(input())
    if name not in students_grades:
        students_grades[name] = []
    students_grades[name].append(grade)

for key, values in students_grades.items():
    avarage = sum(values)/ len(values)
    if avarage >= 4.50:
        print(f"{key} -> {avarage:.2f}")
