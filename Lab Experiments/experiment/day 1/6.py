
def vacuum_cleaner():
    # 0 = Clean, 1 = Dirty
    room = {
        'A': 1,
        'B': 1
    }

    position = 'A'

    print("Initial state:", room)

    while 1 in room.values():
        if room[position] == 1:
            print("Room", position, "is Dirty. Cleaning...")
            room[position] = 0
        else:
            print("Room", position, "is Clean.")

        # Move to the other room
        if position == 'A':
            position = 'B'
        else:
            position = 'A'

    print("All rooms are clean!")
    print("Final state:", room)

vacuum_cleaner()
