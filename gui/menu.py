import pygame
import sys
from gui.constants import WINDOW_SIZE, SOLVING, SPLASH
from searchAlgorithms.bfs import bfs
from searchAlgorithms.dfs import dfs
from searchAlgorithms.greedy import greedy
from searchAlgorithms.astar import astar
from searchAlgorithms.utils import manhattan, euclidean

ALGORITHM_MAP = {
    pygame.K_1: (bfs, None, "BFS"),
    pygame.K_2: (dfs, None, "DFS"),
    pygame.K_3: (greedy, manhattan, "Greedy Manhattan"),
    pygame.K_4: (greedy, euclidean, "Greedy Euclidean"),
    pygame.K_5: (astar, manhattan, "A* Manhattan"),
    pygame.K_6: (astar, euclidean, "A* Euclidean"),
}


class MenuScreen:
    def __init__(self, screen, maze):
        self.screen = screen
        self.maze = maze
        image = pygame.image.load("resources/menu.jpg")
        self.image = pygame.transform.scale(image, (WINDOW_SIZE, WINDOW_SIZE))
        self.scanlines = self._build_scanlines()

    def _build_scanlines(self):
        surface = pygame.Surface((WINDOW_SIZE, WINDOW_SIZE), pygame.SRCALPHA)
        for y in range(0, WINDOW_SIZE, 2):
            pygame.draw.line(surface, (0, 0, 0, 80), (0, y), (WINDOW_SIZE, y))
        return surface

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return (SPLASH, None)
                if event.key in ALGORITHM_MAP:
                    algorithm, heuristic, name = ALGORITHM_MAP[event.key]
                    return (SOLVING, (algorithm, heuristic, name))
        return None

    def update(self):
        pass

    def draw(self):
        self.screen.blit(self.image, (0, 0))
        self.screen.blit(self.scanlines, (0, 0))
