
from heapq import heappush, heappop

# Initial and goal states
start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


# Manhattan distance heuristic
def heuristic(state):
    distance = 0

    for i, tile in enumerate(state):
        if tile != 0:
            goal_pos = goal.index(tile)
            x1, y1 = divmod(i, 3)
            x2, y2 = divmod(goal_pos, 3)
            distance += abs(x1 - x2) + abs(y1 - y2)

    return distance


# A* search algorithm
def solve(start):
    pq = []
    heappush(pq, (heuristic(start), 0, start, []))
    visited = set()

    while pq:
        f, g, state, path = heappop(pq)

        if state in visited:
            continue

        visited.add(state)
        path = path + [state]

        if state == goal:
            return path

        zero = state.index(0)
        row, col = divmod(zero, 3)

        moves = []
        if row > 0:
            moves.append(zero - 3)
        if row < 2:
            moves.append(zero + 3)
        if col > 0:
            moves.append(zero - 1)
        if col < 2:
            moves.append(zero + 1)

        for pos in moves:
            new_state = list(state)
            new_state[zero], new_state[pos] = (
                new_state[pos], new_state[zero]
            )
            new_state = tuple(new_state)

            if new_state not in visited:
                heappush(
                    pq,
                    (g + 1 + heuristic(new_state),
                     g + 1, new_state, path)
                )

    return None


# Print solution
solution = solve(start)

if solution:
    print("Solution found!")
    print("Number of moves:", len(solution) - 1)

    for step, state in enumerate(solution):
        print("\nStep", step)
        for i in range(0, 9, 3):
            print(state[i:i + 3])
else:
    print("No solution found.")
