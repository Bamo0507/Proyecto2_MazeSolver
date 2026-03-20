import pygame
import sys
from gui.constants import WINDOW_SIZE, MENU


class SplashScreen:
    def __init__(self, screen):
        self.screen = screen
        image = pygame.image.load("resources/splash.png")
        self.image = pygame.transform.scale(image, (WINDOW_SIZE, WINDOW_SIZE))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_RETURN, pygame.K_SPACE):
                    return (MENU, None)
        return None

    def update(self):
        pass

    def draw(self):
        self.screen.blit(self.image, (0, 0))
