
# Best First Search Algorithm

import heapq

# Graph with heuristic values
graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('D', 5), ('E', 1)],
    'C': [('F', 3), ('G', 6)],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

def best_first_search(start, goal):
    visited = set()
    priority_queue = []

    heapq.heappush(priority_queue, (0, start))

    while priority_queue:
        heuristic, node = heapq.heappop(priority_queue)

        if node in visited:
            continue

        print("Visited:", node)
        visited.add(node)

        if node == goal:
            print("Goal found:", goal)
            return

        for neighbour, h in graph[node]:
            if neighbour not in visited:
                heapq.heappush(priority_queue, (h, neighbour))

    print("Goal not found")

# Main program
start = input("Enter start node: ").upper()
goal = input("Enter goal node: ").upper()

best_first_search(start, goal)
