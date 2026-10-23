
from collections import deque

def water_jug(capacity1, capacity2, target):
    visited = set()
    queue = deque([(0, 0, [])])

    while queue:
        jug1, jug2, path = queue.popleft()

        if (jug1, jug2) in visited:
            continue

        visited.add((jug1, jug2))
        path = path + [(jug1, jug2)]

        if jug1 == target or jug2 == target:
            print("Solution found:")
            for step in path:
                print(step)
            return

        states = [
            (capacity1, jug2),  # Fill jug 1
            (jug1, capacity2),  # Fill jug 2
            (0, jug2),          # Empty jug 1
            (jug1, 0),          # Empty jug 2
        ]

        # Pour jug 1 into jug 2
        pour = min(jug1, capacity2 - jug2)
        states.append((jug1 - pour, jug2 + pour))

        # Pour jug 2 into jug 1
        pour = min(jug2, capacity1 - jug1)
        states.append((jug1 + pour, jug2 - pour))

        for state in states:
            if state not in visited:
                queue.append((state[0], state[1], path))

    print("No solution exists.")

water_jug(4, 3, 2)
