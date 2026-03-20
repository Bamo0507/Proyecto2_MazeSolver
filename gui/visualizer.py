import pygame
import sys
from gui.constants import WINDOW_SIZE, MENU
from gui.constants import COLOR_BG, COLOR_WALL, COLOR_PATH, COLOR_EXPLORED, COLOR_SOLUTION, COLOR_START, COLOR_GOAL, COLOR_TEXT
from loadMaze.maze import Maze

ANIMATING = "animating"
SHOWING_PATH = "showing_path"
DONE = "done"


class VisualizerScreen:
    def __init__(self, screen, maze, data):
        self.screen = screen
        self.maze = maze

        algorithm, heuristic, name = data
        if heuristic:
            self.result = algorithm(maze, maze.start, maze.goal, heuristic)
        else:
            self.result = algorithm(maze, maze.start, maze.goal)

        self.name = name
        self.phase = ANIMATING
        self.animation_index = 0
        self.animation_speed = 5 # nodos por frame

        self.cell_size = min(WINDOW_SIZE // maze.num_rows, WINDOW_SIZE // maze.num_cols)
        self.offset_x = (WINDOW_SIZE - maze.num_cols * self.cell_size) // 2
        self.offset_y = (WINDOW_SIZE - maze.num_rows * self.cell_size) // 2

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE and self.phase == DONE:
                    return (MENU, None)
        return None

    def update(self):
        if self.phase == ANIMATING:
            for _ in range(self.animation_speed):
                if self.animation_index < len(self.result.explored_order):
                    self.animation_index += 1
                else:
                    self.phase = SHOWING_PATH
                    break

    def draw(self):
        self.screen.fill(COLOR_BG)
        self._draw_maze()
        self._draw_border()

        if self.phase == ANIMATING:
            self._draw_explored(self.result.explored_order[:self.animation_index])
        elif self.phase == SHOWING_PATH:
            self._draw_explored(self.result.explored_order)
            self._draw_path()
            self.phase = DONE
        elif self.phase == DONE:
            self._draw_explored(self.result.explored_order)
            self._draw_path()
            self._draw_metrics()

        self._draw_scanlines()

    def _draw_maze(self):
        for row in range(self.maze.num_rows):
            for col in range(self.maze.num_cols):
                cell = self.maze.grid[row][col]
                x = self.offset_x + col * self.cell_size
                y = self.offset_y + row * self.cell_size

                if cell == 1:
                    color = COLOR_WALL
                elif cell == 2:
                    color = COLOR_START
                elif cell == 3:
                    color = COLOR_GOAL
                else:
                    color = COLOR_PATH

                pygame.draw.rect(self.screen, color, (x, y, self.cell_size, self.cell_size))

    def _draw_explored(self, nodes):
        for (row, col) in nodes:
            x = self.offset_x + col * self.cell_size
            y = self.offset_y + row * self.cell_size
            pygame.draw.rect(self.screen, COLOR_EXPLORED, (x, y, self.cell_size, self.cell_size))

    def _draw_path(self):
        for (row, col) in self.result.path:
            x = self.offset_x + col * self.cell_size
            y = self.offset_y + row * self.cell_size
            pygame.draw.rect(self.screen, COLOR_SOLUTION, (x, y, self.cell_size, self.cell_size))

    def _draw_metrics(self):
        font = pygame.font.Font("resources/fonts/PressStart2P.ttf", 12)
        overlay = pygame.Surface((WINDOW_SIZE, 80))
        overlay.set_alpha(200)
        overlay.fill((0, 0, 0))
        self.screen.blit(overlay, (0, WINDOW_SIZE - 80))

        lines = [
            f"{self.name}",
            f"Nodes: {self.result.nodes_explored}  |  Path: {len(self.result.path)}  |  Time: {self.result.execution_time:.4f}s  |  BF: {self.result.branching_factor:.2f}"
        ]

        for i, line in enumerate(lines):
            text = font.render(line, True, COLOR_TEXT)
            self.screen.blit(text, (10, WINDOW_SIZE - 75 + i * 25))

    def _draw_border(self):
        maze_width = self.maze.num_cols * self.cell_size
        maze_height = self.maze.num_rows * self.cell_size
        border_rect = (
            self.offset_x - 4,
            self.offset_y - 4,
            maze_width + 8,
            maze_height + 8
        )
        pygame.draw.rect(self.screen, COLOR_TEXT, border_rect, 2)

    def _draw_scanlines(self):
        scanline_surface = pygame.Surface((WINDOW_SIZE, WINDOW_SIZE), pygame.SRCALPHA)
        for y in range(0, WINDOW_SIZE, 2):
            pygame.draw.line(scanline_surface, (0, 0, 0, 80), (0, y), (WINDOW_SIZE, y))
        self.screen.blit(scanline_surface, (0, 0))
