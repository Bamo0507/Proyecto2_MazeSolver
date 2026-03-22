import csv
import os
from loadMaze.maze import Maze
from searchAlgorithms.bfs import bfs
from searchAlgorithms.dfs import dfs
from searchAlgorithms.greedy import greedy
from searchAlgorithms.astar import astar
from searchAlgorithms.utils import manhattan, euclidean

MAZE_FILE = "test_maze.txt"

ALGORITHMS = [
    ("BFS", bfs, None),
    ("DFS", dfs, None),
    ("Greedy Manhattan", greedy, manhattan),
    ("Greedy Euclidean", greedy, euclidean),
    ("A* Manhattan", astar, manhattan),
    ("A* Euclidean", astar, euclidean),
]

maze = Maze(MAZE_FILE)

results = []
for name, algorithm, heuristic in ALGORITHMS:
    if heuristic:
        result = algorithm(maze, maze.start, maze.goal, heuristic)
    else:
        result = algorithm(maze, maze.start, maze.goal)

    results.append({
        "algorithm": name,
        "path_length": len(result.path),
        "nodes_explored": result.nodes_explored,
        "execution_time": round(result.execution_time, 6),
        "branching_factor": round(result.branching_factor, 4),
    })
    print(f"{name}: path={len(result.path)}, nodes={result.nodes_explored}, time={result.execution_time:.4f}s, bf={result.branching_factor:.2f}")

output_file = os.path.splitext(MAZE_FILE)[0] + "_RESULTS.csv"
with open(output_file, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=["algorithm", "path_length", "nodes_explored", "execution_time", "branching_factor"])
    writer.writeheader()
    writer.writerows(results)

print(f"\nResultados guardados en: {output_file}")
