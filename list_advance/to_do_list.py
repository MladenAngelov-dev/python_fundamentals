def filtered_tasks():
    tasks = []
    while True:
        new_tasks = input()
        if new_tasks == "End":
            break
        tasks.append(new_tasks)
    sorted_tasks = sorted(tasks, key=lambda x: int(x.split("-")[0]))
    filtered_sorted_tasks = [task.split('-')[1] for task in sorted_tasks]
    return filtered_sorted_tasks


print(filtered_tasks())