# BFS vs DFS Performance Analysis

## Introduction

This project compares the performance of two uninformed search algorithms:

- Breadth-First Search (BFS)
- Depth-First Search (DFS)

Both algorithms are tested on the same 15-node graph to compare their execution time and number of nodes expanded.

## Objective

The objectives of this project are:

1. Implement BFS and DFS.
2. Test both algorithms on the same graph.
3. Measure average execution time.
4. Count the number of nodes expanded.
5. Use py-spy for profiling.
6. Compare the performance using actual results.

## Problem Used

A 15-node graph is used.

- Start Node: A
- Goal Node: M

Both algorithms found the path:

A → D → I → M

## Algorithms

### Breadth-First Search (BFS)

BFS explores the graph level by level using a queue.

### Depth-First Search (DFS)

DFS explores one branch deeply before backtracking. It uses a stack-based approach.

## Profiling Tools

The following tools were used:

- Python timeit module for average execution time
- Manual node counter for nodes expanded
- py-spy 0.4.2 for profiling and flamegraph generation

## Results

| Measurement | BFS | DFS |
|---|---:|---:|
| Average execution time | 4.7723 × 10⁻⁶ seconds | 7.7606 × 10⁻⁶ seconds |
| Nodes expanded | 13 | 15 |
| py-spy profile | bfs_profile.svg | dfs_profile.svg |
| py-spy samples | 8 | 7 |
| Errors | 0 | 0 |

## Project Files

- bfs_dfs.py – BFS and DFS implementation
- bfs_only.py – BFS program used for profiling
- dfs_only.py – DFS program used for profiling
- profiling.py – Measures average execution time and nodes expanded
- bfs_profile.svg – BFS py-spy profile
- dfs_profile.svg – DFS py-spy profile
- .gitignore – Git ignore file

## Analysis

Both BFS and DFS were tested on the same graph with the same start and goal nodes.

BFS expanded 13 nodes, while DFS expanded 15 nodes. The measured average execution time was 4.7723 × 10⁻⁶ seconds for BFS and 7.7606 × 10⁻⁶ seconds for DFS.

The results are specific to the selected graph, implementation, and computer environment.

## How to Run

Run the main program:

python bfs_dfs.py

Run the profiling program:

python profiling.py

Run BFS profiling:

py-spy record --output bfs_profile.svg -- python bfs_only.py

Run DFS profiling:

py-spy record --output dfs_profile.svg -- python dfs_only.py

## Conclusion

This project demonstrates empirical performance analysis of BFS and DFS. Both algorithms successfully found the required path. The experiment used actual execution time, node count, and py-spy profiling to compare their performance.

## GitHub Repository

https://github.com/ArpitaTaradale/BFS-DFS-Performance

## Course Information

Course: 02AML204 – Introduction to Artificial Intelligence

Activity: SLE-2 – Profiling Report

Topic: Empirical Performance Analysis
