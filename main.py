import sys

import pygame.sprite

from Settings import *
from Level import Level
from pytmx.util_pygame import load_pygame
from CharacterCreator import create_character
from PlayerData import PlayerData

#Klasa okienka z grą
class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('No Title RPG Game')
        self.clock = pygame.time.Clock()

        self.player_data = PlayerData(100, 5, 1)
        self.tmx_maps = {0: load_pygame(join('data', 'levels', 'omni.tmx'))}

        self.current_stage = None

        self.current_skin = 0
        self.skin_font = pygame.font.Font(None, 24)

    def run(self):
        player_name, self.current_skin = create_character()
        self.current_stage = Level(self.tmx_maps[0], player_name, self.current_skin + 1, self.player_data)

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
