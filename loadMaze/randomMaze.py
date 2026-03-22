import random
from datetime import datetime
from searchAlgorithms.bfs import bfs


def generate_random_start(maze):
    # limpiar el start original
    start_row, start_col = maze.start
    maze.grid[start_row][start_col] = 0

    # buscar nuevo start aleatorio con conectividad garantizada al goal
    while True:
        row = random.randint(0, maze.num_rows - 1)
        col = random.randint(0, maze.num_cols - 1)

        if maze.grid[row][col] != 0:
            continue

        # verificar que hay un camino al goal usando BFS
        if bfs(maze, (row, col), maze.goal):
            maze.grid[row][col] = 2
            maze.start = (row, col)
            _save_maze(maze)
            return


def _save_maze(maze):
    timestamp = datetime.now().strftime("%H%M%S")
    filename = f"{timestamp}_maze.txt"
    with open(filename, 'w') as file:
        for row in maze.grid:
            file.write("".join(str(cell) for cell in row) + "\n")
    print(f"Maze guardado como: {filename}")
