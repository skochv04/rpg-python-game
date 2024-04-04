import pygame
from Map import GameMap

pygame.init()

class Window:
    def __init__(self, width, height):
        self.window = pygame.display.set_mode((width, height))
        self.map = GameMap()
        pygame.display.set_caption("FF RPG")

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            # Fill the window with white color
            self.window.fill((255, 255, 255))

            # Update the display
            pygame.display.update()
