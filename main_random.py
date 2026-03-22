from loadMaze.maze import Maze
from loadMaze.randomMaze import generate_random_start

# Maze to randomize
maze = Maze("test_maze.txt")
generate_random_start(maze)
