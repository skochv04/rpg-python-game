import sys

import pygame.sprite

from Settings import *
from Level import Level
from pytmx.util_pygame import load_pygame
from CharacterCreator import create_character
from PlayerData import PlayerData
from Menu import MainMenu
from DeltaTime import DT

#Klasa okienka z grą
class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('No Title RPG Game')
        self.clock = pygame.time.Clock()

        # self.player_data = None
        self.player_data = PlayerData(6, 6, 2, 3)
        self.tmx_maps = {0: load_pygame(join('data', 'levels', 'omni.tmx'))}

        self.current_stage = None

        self.current_skin = 0
        self.skin_font = pygame.font.Font(None, 24)
        self.dt = DT(self.clock)

    def run(self):
        menu = MainMenu()
        option = menu.run()
        if option == 'Exit':
            pygame.quit()
            sys.exit()
        elif option == 'Settings':
            pass


        player_name, self.current_skin = create_character()
        self.player_data = PlayerData(100, 30, 1, self.current_skin + 1)
        self.current_stage = Level(self.tmx_maps[0], player_name, self.current_skin + 1, self.player_data)

        while True:
            self.dt.update()
            if self.dt.get() > 0.04: print(self.dt.get())
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        option = menu.run()
                        if option == 'Exit':
                            pygame.quit()
                            sys.exit()
                        else:
                            pass
            self.current_stage.run(self.dt)

            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()
