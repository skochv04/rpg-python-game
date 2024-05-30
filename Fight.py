from Settings import *
from Player import Player
from Spritessheet import SpritesSheet
import pygame
import sys
from Button import Button
from os.path import join


def fight(enemy, player):
    current_skin = player.skin
    display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    background_image = pygame.image.load('graphics/map/background/1.png').convert()

    # Create buttons
    button_width, button_height = 250, 50
    button_y = WINDOW_HEIGHT - button_height - 40
    spacing = 40
    button1 = Button(spacing, button_y, button_width, button_height, 'Attack')
    button2 = Button(spacing * 2 + button_width, button_y, button_width, button_height, 'Button 2')
    button3 = Button(spacing * 3 + button_width * 2, button_y, button_width, button_height, 'Button 3')
    button4 = Button(spacing * 4 + button_width * 3, button_y, button_width, button_height, 'Escape')

    while True:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button1.is_over(pos):
                    print('button 1 clicked')
                if button2.is_over(pos):
                    print('button 2 clicked')
                if button3.is_over(pos):
                    print('button 3 clicked')
                if button4.is_over(pos):
                    print('button 4 clicked')

        display_surface.fill((30, 30, 30))

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

        button1.draw(display_surface)
        button2.draw(display_surface)
        button3.draw(display_surface)
        button4.draw(display_surface)

        pygame.display.flip()
        clock.tick(30)
