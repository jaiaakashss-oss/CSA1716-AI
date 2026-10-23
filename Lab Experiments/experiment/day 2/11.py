
# Map Colouring using CSP and Backtracking

# Regions and their neighbours
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

colours = ['Red', 'Green', 'Blue']
colouring = {}

def is_safe(region, colour):
    for neighbour in graph[region]:
        if neighbour in colouring and colouring[neighbour] == colour:
            return False
    return True

def solve(regions):
    if not regions:
        return True

    region = regions[0]

    for colour in colours:
        if is_safe(region, colour):
            colouring[region] = colour

            if solve(regions[1:]):
                return True

            del colouring[region]

    return False

if solve(list(graph.keys())):
    print("Map Colouring Solution:")
    for region, colour in colouring.items():
        print(region, ":", colour)
else:
    print("No solution exists")
