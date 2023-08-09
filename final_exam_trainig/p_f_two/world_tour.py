

trip = input()
command = input()

while command != "Travel":
    command = command.split(":")
    if command[0].startswith("Add"):
        index = int(command[1])
        substring = command[2]
        if index in range(len(trip)):
            new_trip = trip[:index] + substring + trip[index:]
            trip = new_trip
        print(trip)

    elif command[0].startswith("Remove"):
        start_index = int(command[1])
        end_index = int(command[2])
        if start_index in range(len(trip)) and end_index in range(len(trip)):
            trip = trip[:start_index] + trip[end_index + 1:]
        print(trip)

    elif command[0].startswith("Switch"):
        string = command[1]
        replacement = command[2]
        if string in trip:
            trip = trip.replace(string, replacement)
        print(trip)

    command = input()
print(f"Ready for world tour! Planned stops: {trip}")
