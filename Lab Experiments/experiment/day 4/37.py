
import heapq

def best_first_search(graph, heuristic, start, goal):
    visited = set()
    priority_queue = []

    heapq.heappush(priority_queue, (heuristic[start], start))
    parent = {start: None}

    while priority_queue:
        h, current = heapq.heappop(priority_queue)

        if current in visited:
            continue

        print("Visiting:", current)
        visited.add(current)

        if current == goal:
            path = []
            node = goal

            while node is not None:
                path.append(node)
                node = parent[node]

            path.reverse()
            print("Goal Found!")
            print("Path:", " -> ".join(path))
            return

        for neighbor in graph[current]:
            if neighbor not in visited:
                parent[neighbor] = current
                heapq.heappush(
                    priority_queue,
                    (heuristic[neighbor], neighbor)
                )

    print("Goal not found!")


# Graph representation
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

# Heuristic values
heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 5,
    'E': 3,
    'F': 2,
    'G': 0
}

start = 'A'
goal = 'G'

best_first_search(graph, heuristic, start, goal)
