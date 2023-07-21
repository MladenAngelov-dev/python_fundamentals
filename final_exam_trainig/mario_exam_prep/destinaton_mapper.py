import re


def valid_destinaton_function(destination_data):

    pattern = r"(\=|\/)([A-Z][A-Za-z]{2,})\1"
    travel_points = 0
    valid_destinations = []
    result = re.finditer(pattern, destination_data)

    if result:
        for current_destination in result:
            valid_destinations.append(current_destination.group(2))
            travel_points += len(current_destination.group(2))

        print(f"Destinations: {', '.join(valid_destinations)}")
        print(f"Travel Points: {travel_points}")


data = input()
valid_destinaton_function(data)