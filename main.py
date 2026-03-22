import pygame
from loadMaze.maze import Maze
from gui.constants import WINDOW_SIZE, SPLASH, MENU, SOLVING
from gui.splash import SplashScreen
from gui.menu import MenuScreen
from gui.visualizer import VisualizerScreen

MAZE_FILE = "184806_maze.txt"


def get_screen(state, screen, maze, data=None):
    if state == SPLASH:
        return SplashScreen(screen)
    if state == MENU:
        return MenuScreen(screen, maze)
    if state == SOLVING:
        return VisualizerScreen(screen, maze, data)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("Maze Solver")
    clock = pygame.time.Clock()

    maze = Maze(MAZE_FILE)

    current_state = SPLASH
    current_screen = SplashScreen(screen)

    while True:
        result = current_screen.handle_events()
        current_screen.update()
        current_screen.draw()
        pygame.display.flip()
        clock.tick(60)

        if result:
            new_state, data = result
            if new_state != current_state:
                current_state = new_state
                current_screen = get_screen(current_state, screen, maze, data)


main()
