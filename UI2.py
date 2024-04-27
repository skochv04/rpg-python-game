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
        self.response_keys = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5,
                              pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9, pygame.K_0]
        self.run()

    def get_text(self):
        return self.dialogue_data.parse_text(self.current_dialogue)

    def render_text(self, text):
        self.image.fill('black')
        font = pygame.freetype.Font(None, 36)
        text_surface, _ = font.render(text, 'white', 'black')
        self.image.blit(text_surface, (10, 10))

    def show(self):
        self.image.blit(self.display_surface, self.rect)
        pygame.display.flip()


    def run(self):
        end, text_ended = False, False
        text, responses = self.get_text()
        self.render_text(text)

        answer = None

        while not end:
            self.show()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            keys = pygame.key.get_pressed()

            if len(responses) > 0:
                for i in range(len(responses)):
                    if keys[self.response_keys[i]]:
                        answer = i
            else:
                text_ended = True


            if text_ended:
                if keys[pygame.K_RETURN]:
                    end = True
            else:
                selected_response = list(responses.keys())[answer]
                if responses[selected_response]['next'] is not None:
                    text, responses = self.get_text(responses[selected_response]['next'])
                else:
                    text_ended = True
