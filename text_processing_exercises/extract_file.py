whole_path = input().split("\\")
file_name, extension = whole_path[-1].split(".")
print(f"File name: {file_name}\nFile extension: {extension}")