from Settings import *
from Player import Player
from Spritessheet import SpritesSheet
import pygame
import sys
from os.path import join


def fight(enemy, player):
    font = pygame.font.Font(None, 36)
    input_box = pygame.Rect(50, 150, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    current_skin = player.skin
    display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    text = ''
    default_text = font.render(player.name, True, color)
    background_image = pygame.image.load('graphics/map/background/1.png').convert()

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
                if event.key == pygame.K_RETURN:
                    return text, current_skin
                if active:
                    if event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        display_surface.fill((30, 30, 30))

        # Display the input box
        if len(text) == 0:
            txt_surface = default_text
        else:
            txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        display_surface.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(display_surface, color, input_box, 2)

        # Display player sprite
        my_spritesheet = SpritesSheet(join('graphics', 'player', f'{current_skin}', 'texture.png'))
        sprite_down = my_spritesheet.parse_sprite('8.png')
        skin_view = pygame.transform.scale(sprite_down, (200, 200))
        display_surface.blit(skin_view, (150, 300))

        # Display enemy sprite
        enemy_spritesheet = SpritesSheet(join(f'graphics/enemies/{enemy.__class__.__name__}/texture.png'))
        sprite_right = enemy_spritesheet.parse_sprite('5.png')
        skin_view_right = pygame.transform.scale(sprite_right, (200, 200))
        display_surface.blit(skin_view_right, (WINDOW_WIDTH - 350, 300))

        # Display squares above player and enemy
        square_size = 20
        for i in range(5):
            pygame.draw.rect(display_surface, (255, 0, 0), (150 + i * 40, 280, square_size, square_size))
            pygame.draw.rect(display_surface, (255, 0, 0), (WINDOW_WIDTH - 350 + i * 40, 280, square_size, square_size))

        pygame.display.flip()
        clock.tick(30)
