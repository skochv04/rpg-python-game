import pygame
import sys

from Settings import *
from Level import Level
from pytmx.util_pygame import load_pygame
from os.path import join


class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Super Pirate World')
        self.clock = pygame.time.Clock()

        self.tmx_maps = {0: load_pygame(join('data', 'levels', 'omni.tmx'))}

        # self.current_stage = Level(self.tmx_maps[0])
        self.current_stage = None

        self.current_skin = 0
        self.skin_font = pygame.font.Font(None, 24)

    def read_input(self):
        font = pygame.font.Font(None, 36)
        input_box = pygame.Rect(100, 100, 140, 32)
        color_inactive = pygame.Color('lightskyblue3')
        color_active = pygame.Color('dodgerblue2')
        color = color_inactive
        active = False
        text = ''
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box.collidepoint(event.pos):
                        active = not active
                    else:
                        active = False
                    color = color_active if active else color_inactive
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            return text
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode

                    if event.key == pygame.K_LEFT:
                        self.current_skin = (self.current_skin - 1) % 8
                    elif event.key == pygame.K_RIGHT:
                        self.current_skin = (self.current_skin + 1) % 8

            self.display_surface.fill((30, 30, 30))
            txt_surface = font.render(text, True, color)
            width = max(200, txt_surface.get_width() + 10)
            input_box.w = width
            self.display_surface.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
            pygame.draw.rect(self.display_surface, color, input_box, 2)

            skin_text = self.skin_font.render(f"Current skin: {self.current_skin + 1}", True, (255, 255, 255))
            self.display_surface.blit(skin_text, (100, 150))

            pygame.display.flip()
            self.clock.tick(30)

    def run(self):
        player_name = self.read_input()
        self.current_stage = Level(self.tmx_maps[0], player_name, self.current_skin + 1)

        while True:
            dt = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.current_stage.run(dt)

            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()
