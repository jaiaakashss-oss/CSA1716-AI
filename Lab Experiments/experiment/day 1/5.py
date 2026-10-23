
from collections import deque

def solve():
    # State: (missionaries_left, cannibals_left, boat_position)
    # boat_position: 0 = left bank, 1 = right bank

    start = (3, 3, 0)
    goal = (0, 0, 1)

    moves = [
        (1, 0),  # One missionary
        (2, 0),  # Two missionaries
        (0, 1),  # One cannibal
        (0, 2),  # Two cannibals
        (1, 1)   # One missionary and one cannibal
    ]

    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        state, path = queue.popleft()
        m, c, boat = state

        if state == goal:
            print("Solution found:")
            for s in path:
                print(s)
            return

        for dm, dc in moves:
            if boat == 0:
                new_state = (m - dm, c - dc, 1)
            else:
                new_state = (m + dm, c + dc, 0)

            nm, nc, nb = new_state

            # Check population limits
            if not (0 <= nm <= 3 and 0 <= nc <= 3):
                continue

            # Check safety on both banks
            if nm > 0 and nc > nm:
                continue

            mr, cr = 3 - nm, 3 - nc
            if mr > 0 and cr > mr:
                continue

            # Check that the boat carries at least one person
            if dm + dc == 0:
                continue

            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [new_state]))

    print("No solution exists.")

solve()
