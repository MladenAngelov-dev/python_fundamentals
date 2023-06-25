def sorted_names(names_sort):
    sorted_name = sorted(names_sort, key=lambda x: (-len(x), x))
    return sorted_name


names = input().split(", ")
print(sorted_names(names))