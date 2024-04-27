import pygame

from Settings import *

class UI:
    def __init__(self, dialogue_data, current_dialogue):
        self.display_surface = pygame.display.get_surface()
        self.image = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT / 4))
        self.image.fill('black')
        self.rect = self.image.get_frect(topleft=(0, WINDOW_HEIGHT * 3 / 4))

        self.dialogue_data = dialogue_data
        self.current_dialogue = current_dialogue
        self.run()

    def get_text(self):
        return self.dialogue_data.parse_text(self.current_dialogue)


    def run(self):
        end = False
        text, responses = self.get_text()
        answer = None

        while not end:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            keys = pygame.key.get_pressed()

            if keys[pygame.K_1]:
                answer = 1
            elif keys[pygame.K_2]:
                answer = 2

            if answer is not None:
