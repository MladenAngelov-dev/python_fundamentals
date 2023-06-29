students_dict = {}
search_line = ''
while True:
    input_data = input()

    if ":" not in input_data:
        if "_" in input_data:
            search_line = input_data.replace("_", " ")
        else:
            search_line = input_data
        break

    name, student_id, course = input_data.split(":")
    if course not in students_dict:
        students_dict[course] = []
    students_dict[course].append((name, student_id))

if search_line in students_dict:
    for name, student_id in students_dict[search_line]:
        print(f"{name} - {student_id}")

