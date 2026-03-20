class Maze:
    def __init__(self, file_path: str):
        self.grid = load_maze_from_file(file_path)
        self.num_rows = len(self.grid)
        self.num_cols = len(self.grid[0])
        self.start = self._find_cell(2)
        self.goal = self._find_cell(3)

    def _find_cell(self, category: int) -> tuple[int, int]:
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if self.grid[row][col] == category:
                    return (row, col)

    def is_walkable(self, row: int, col: int) -> bool:
        # validar que no se salga de los limites de ancho y alto del laberinto
        if row < 0 or row >= self.num_rows:
            return False
        if col < 0 or col >= self.num_cols:
            return False
        # se puede pasar si es camino libre, partida o salida
        return self.grid[row][col] != 1


def load_maze_from_file(file_path: str) -> list[list[int]]:
    grid = []
    with open(file_path, 'r') as file:
        for line in file:
            row = [int(cell) for cell in line.strip()]
            grid.append(row)
    return grid
