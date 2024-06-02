from Settings import *
from Player import Player
from Spritessheet import SpritesSheet
import pygame
import sys
from Button import Button
from os.path import join
from Notification import *


def player_attack(player, enemy):
    enemy.enemy_data.reduce_health(player.player_data.power)
    if enemy.enemy_data.health <= 0:
        return True

def display_player(player, display_surface):
    my_spritesheet = SpritesSheet(join('graphics', 'player', f'{player.skin}', 'texture.png'))
    sprite_down = my_spritesheet.parse_sprite('8.png')
    skin_view = pygame.transform.scale(sprite_down, (200, 200))
    display_surface.blit(skin_view, (150, 300))

def display_enemy(enemy, display_surface):
    enemy_spritesheet = SpritesSheet(join(f'graphics/enemies/{enemy.__class__.__name__}/texture.png'))
    sprite_right = enemy_spritesheet.parse_sprite('5.png')
    skin_view_right = pygame.transform.scale(sprite_right, (200, 200))
    display_surface.blit(skin_view_right, (WINDOW_WIDTH - 350, 300))

def display_items(player, display_surface, button):
    items = player.player_data.inventory.get_item_list()
    items = list(filter(lambda item: item.usable_during_battle, items))

    if len(items) <= 0:
        return None

    # show list of items vertically above the items button
    item_x = button.x
    item_y = button.y - 50
    item_width = items[0].image.get_width()
    item_height = items[0].image.get_height()
    item_list_surface = pygame.Surface((button.width, item_height * len(items)))
    item_list_surface.fill((0, 110, 250))
    for i, item in enumerate(items):
        # Draw item image
        item_image_position = (0, 0)
        item_list_surface.blit(item.image, item_image_position)
        # Draw item amount to the right of the item image
        font = pygame.font.Font(None, 36)
        text_surface = font.render(str(item.amount), True, 'black')
        text_position = (item_image_position[0] + item_width, item_image_position[1] + item_height // 2 - text_surface.get_height() // 2)
        item_list_surface.blit(text_surface, text_position)
        # Draw item name to the right of the item amount
        text_surface = font.render(item.name, True, 'black')
        text_position = (text_position[0] + 30, text_position[1])
        item_list_surface.blit(text_surface, text_position)


    return item_list_surface

def display_health(player, enemy, display_surface):
    # Create health Bars for player and enemy
    player_max_health = pygame.Surface((200, 10))
    player_max_health.fill('black')
    player_health = pygame.Surface((200 * (player.get_health()/player.get_max_health()) , 10))
    player_health.fill('green')
    player_health_rect = player_health.get_rect(topleft=(150, 250))

    enemy_max_health = pygame.Surface((200, 10))
    enemy_max_health.fill('black')
    enemy_health = pygame.Surface((200 * (enemy.get_health()/enemy.get_max_health()), 10))
    enemy_health.fill('green')
    enemy_health_rect = enemy_health.get_rect(topleft=(WINDOW_WIDTH - 350, 250))

    display_surface.blit(player_max_health, player_health_rect)
    display_surface.blit(player_health, player_health_rect)
    display_surface.blit(enemy_max_health, enemy_health_rect)
    display_surface.blit(enemy_health, enemy_health_rect)

def create_buttons():
    button_width, button_height = 250, 50
    button_y = WINDOW_HEIGHT - button_height - 40
    spacing = 40
    button1 = Button(spacing, button_y, button_width, button_height, 'Attack')
    button2 = Button(spacing * 2 + button_width, button_y, button_width, button_height, 'Skills')
    button3 = Button(spacing * 3 + button_width * 2, button_y, button_width, button_height, 'Items')
    button4 = Button(spacing * 4 + button_width * 3, button_y, button_width, button_height, 'Escape')

    return button1, button2, button3, button4

def fight(enemy, player, dt):
    display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    background_image = pygame.image.load('graphics/map/background/1.png').convert()

    # Create buttons
    buttons = create_buttons()

    item_list_surface = None
    notification = None

    while True:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if buttons[0].is_over(pos):
                    if player_attack(player, enemy):
                        enemy.kill()
                        return
                    enemy.fight_ai(player)
                    print('button 1 clicked')
                if buttons[1].is_over(pos):
                    notification = Notification('Not implemented yet')
                    print('button 2 clicked')
                if buttons[2].is_over(pos):
                    if item_list_surface:
                        item_list_surface = None
                    else:
                        item_list_surface = display_items(player, display_surface, buttons[2])
                    notification = Notification('Not implemented yet')
                    print('button 3 clicked')
                if buttons[3].is_over(pos):
                    print('button 4 clicked')
                    enemy.escape()
                    return

        display_surface.fill((30, 30, 30))

        # Display player sprite
        display_player(player, display_surface)

        # Display enemy sprite
        display_enemy(enemy, display_surface)

        # Display squares above player and enemy
        display_health(player, enemy, display_surface)

        # Draw buttons
        for button in buttons:
            button.draw(display_surface)

        if item_list_surface:
            display_surface.blit(item_list_surface, (buttons[2].x, buttons[2].y - buttons[2].height - 15))

        if notification:
            notification.draw(display_surface)
            if notification.update(dt):
                notification = None

        pygame.display.flip()
        clock.tick(30)
