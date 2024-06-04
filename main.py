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

        self.player_data = None
        self.tmx_maps = {1: load_pygame(join('data', 'maps', 'level1.tmx'))}

        self.audio_files = {
            'background': pygame.mixer.Sound(join('audio', 'background.mp3')),
            'npc': pygame.mixer.Sound(join('audio', 'npc.mp3')),

            'coin': pygame.mixer.Sound(join('audio', 'coin.wav')),
            'jump': pygame.mixer.Sound(join('audio', 'jump.wav')),
            'up_level': pygame.mixer.Sound(join('audio', 'up_level.wav')),
            'quest_done': pygame.mixer.Sound(join('audio', 'quest_done.mp3')),
            'fight_win': pygame.mixer.Sound(join('audio', 'fight_win.mp3')),
            'skill_activate': pygame.mixer.Sound(join('audio', 'skill_activate.mp3')),
            'timer': pygame.mixer.Sound(join('audio', 'timer.mp3')),
            'fortune_fail': pygame.mixer.Sound(join('audio', 'fortune_fail.wav')),
            'fortune_health': pygame.mixer.Sound(join('audio', 'fortune_health.mp3')),
            'fortune_coin': pygame.mixer.Sound(join('audio', 'fortune_coin.mp3')),
            'fortune_equipment': pygame.mixer.Sound(join('audio', 'fortune_equipment.mp3')),
            'skill_small': pygame.mixer.Sound(join('audio', 'skill_small.mp3')),
            'mouse_click': pygame.mixer.Sound(join('audio', 'mouse_click.mp3'))
        }

        self.background_sound = pygame.mixer.Sound(join('audio', 'background.mp3'))
        self.background_sound.set_volume(0.05)

        self.menu_sound = pygame.mixer.Sound(join('audio', 'menu_button.mp3'))
        self.arrow_sound = pygame.mixer.Sound(join('audio', 'arrows.flac'))

        self.current_stage = None

        self.current_skin = 0
        self.skin_font = pygame.font.Font(None, 24)
        self.dt = DT(self.clock)

    def run(self):
        menu = MainMenu(self.menu_sound)
        option = menu.run()

        if option == 'Exit':
            pygame.quit()
            sys.exit()
        elif option == 'Settings':
            pass

        player_name, self.current_skin = create_character(self.arrow_sound)
        level = 1
        self.player_data = PlayerData(100, 30, 3, 1, 10, self.current_skin + 1, self.audio_files, self.background_sound)
        self.current_stage = Level(self.tmx_maps[level], player_name, self.current_skin + 1, self.player_data)
        self.background_sound.play(-1)
        self.player_data.level = level


        self.dt.update()
        while True:
            self.dt.update()
            if self.player_data.level != level:
                level = self.player_data.level
                self.current_stage = Level(self.tmx_maps[level], player_name, self.current_skin + 1, self.player_data)
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
