import timeit
from bfs_only import bfs
from dfs_only import dfs

start = 'A'
goal = 'M'

bfs_time = timeit.timeit(lambda: bfs(start, goal), number=1000)
dfs_time = timeit.timeit(lambda: dfs(start, goal), number=1000)

bfs_average = bfs_time / 1000
dfs_average = dfs_time / 1000

_, bfs_nodes = bfs(start, goal)
_, dfs_nodes = dfs(start, goal)

print("BFS")
print("Average Time:", bfs_average, "seconds")
print("Nodes Expanded:", bfs_nodes)

print("\nDFS")
print("Average Time:", dfs_average, "seconds")
print("Nodes Expanded:", dfs_nodes)