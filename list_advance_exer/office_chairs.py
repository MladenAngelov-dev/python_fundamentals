def check_the_rooms(number_of_rooms):
    free_chairs = 0
    needed_chairs = 0
    for room in range(1, count_of_rooms + 1):
        chairs, visitors = input().split()
        difference = len(chairs) - int(visitors)
        if difference < 0:
            print(f"{abs(difference)} more chairs needed in room {room}")
            needed_chairs += abs(difference)
        else:
            free_chairs += difference
    return free_chairs, needed_chairs


count_of_rooms = int(input())
total_free_chairs , total_needed_chairs= check_the_rooms(count_of_rooms)
if total_free_chairs >= total_needed_chairs:
    print(f"Game On, {total_free_chairs} free chairs left")