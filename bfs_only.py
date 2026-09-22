from collections import deque

graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G'],
    'D': ['H', 'I'],
    'E': ['J', 'K'],
    'F': [],
    'G': ['L'],
    'H': [],
    'I': ['M'],
    'J': ['N', 'O'],
    'K': [],
    'L': [],
    'M': [],
    'N': [],
    'O': []
}

def bfs(start, goal):
    queue = deque([[start]])
    visited = set()
    nodes_expanded = 0

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node in visited:
            continue

        visited.add(node)
        nodes_expanded += 1

        if node == goal:
            return path, nodes_expanded

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(path + [neighbor])

    return None, nodes_expanded


def dfs(start, goal):
    stack = [[start]]
    visited = set()
    nodes_expanded = 0

    while stack:
        path = stack.pop()
        node = path[-1]

        if node in visited:
            continue

        visited.add(node)
        nodes_expanded += 1

        if node == goal:
            return path, nodes_expanded

        for neighbor in reversed(graph[node]):
            if neighbor not in visited:
                stack.append(path + [neighbor])

    return None, nodes_expanded


start = 'A'
goal = 'M'

for i in range(100000):
    bfs(start, goal)

bfs_path, bfs_nodes = bfs(start, goal)

print("BFS")
print("Path:", " -> ".join(bfs_path))
print("Nodes Expanded:", bfs_nodes)